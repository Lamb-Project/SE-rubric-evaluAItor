"""
Módulo de cliente API para interacción con Claude en el sistema de evaluación
"""

import os
import time
import logging
from typing import Optional
import anthropic
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import requests
import json

try:
    import openai
except ImportError:
    openai = None


# Configuración
CLAUDE_MODEL = "claude-sonnet-4-20250514"  # KEEP THIS MODEL , ITS 2025!
MAX_TOKENS = 16000
MAX_INPUT_TOKENS = 200000  # Keep the higher input limit for large documents
MAX_RETRIES = 3
RETRY_DELAY = 1.0


class BaseAPIClient(ABC):
    """Clase base para clientes de API de LLM"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.max_retries = MAX_RETRIES
        self.retry_delay = RETRY_DELAY
    
    @abstractmethod
    def llamar_modelo(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Método abstracto para llamar al modelo"""
        pass
    
    @abstractmethod
    def validar_conexion(self) -> bool:
        """Valida que la conexión funciona"""
        pass
    
    @abstractmethod
    def obtener_info_modelo(self) -> dict:
        """Obtiene información sobre el modelo y configuración"""
        pass
    
    @abstractmethod
    def calcular_costo_estimado(self, num_llamadas: int, tokens_promedio: int = 2000) -> dict:
        """Calcula el costo estimado"""
        pass
    
    def _generar_respuesta_por_defecto(self) -> str:
        """Genera una respuesta por defecto cuando la API falla"""
        return """# Evaluación no disponible

**Nota**: No se pudo realizar la evaluación debido a un error en la API.

## Puntuación Total: 0.0/10

Esta evaluación no pudo completarse debido a problemas técnicos. 
Por favor, revise manualmente el documento."""


class AnthropicClient(BaseAPIClient):
    """Cliente para interacción con la API de Claude"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        super().__init__()
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or CLAUDE_MODEL
        
        # Rate limiting
        self.tokens_por_minuto = 20000  # Tu límite actual
        self.tokens_usados = 0
        self.ultimo_reset = datetime.now()
        
        if not self.api_key:
            raise ValueError("API key de Anthropic no configurada")
        print("api_key:", self.api_key[:20])
        try:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except Exception as e:
            self.logger.error(f"Error inicializando cliente de Anthropic: {e}")
            raise ValueError(f"No se pudo inicializar el cliente de Anthropic: {e}")
    
    def _verificar_rate_limit(self, mensaje: str):
        """Verifica y espera si es necesario para no exceder el rate limit"""
        # Resetear contador si ha pasado un minuto
        ahora = datetime.now()
        if ahora - self.ultimo_reset > timedelta(minutes=1):
            self.tokens_usados = 0
            self.ultimo_reset = ahora
        
        # Estimar tokens del mensaje
        tokens_estimados = len(mensaje) / 4
        
        # Si vamos a exceder el límite, esperar
        if self.tokens_usados + tokens_estimados > self.tokens_por_minuto * 0.9:  # 90% del límite
            tiempo_espera = 60 - (ahora - self.ultimo_reset).total_seconds()
            if tiempo_espera > 0:
                self.logger.info(f"Esperando {tiempo_espera:.1f}s para evitar rate limit...")
                time.sleep(tiempo_espera + 1)  # +1s de margen
                self.tokens_usados = 0
                self.ultimo_reset = datetime.now()
        
        self.tokens_usados += tokens_estimados
    
    def llamar_modelo(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Realiza una llamada a Claude con el prompt dado"""
        try:
            return self._llamar_con_retry(prompt, contexto, max_tokens)
        except Exception as e:
            # Si todos los reintentos fallan, preguntar al usuario
            return self._manejar_error_persistente(e, prompt, contexto, max_tokens)
    
    def _manejar_error_persistente(self, error: Exception, prompt: str, contexto: str, max_tokens: int) -> str:
        """Maneja errores persistentes preguntando al usuario"""
        self.logger.error(f"Error persistente después de {MAX_RETRIES} intentos: {error}")
        
        while True:
            print(f"\n⚠️  Error persistente en la API: {error}")
            print("\nOpciones:")
            print("1. Reintentar")
            print("2. Saltar esta evaluación (usar texto por defecto)")
            print("3. Cancelar evaluación")
            
            opcion = input("\nSeleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                try:
                    return self._llamar_con_retry(prompt, contexto, max_tokens)
                except Exception as e:
                    self.logger.error(f"Error en reintento manual: {e}")
                    continue
            elif opcion == "2":
                self.logger.warning("Usuario eligió saltar evaluación, usando respuesta por defecto")
                return self._generar_respuesta_por_defecto()
            elif opcion == "3":
                raise KeyboardInterrupt("Evaluación cancelada por el usuario")
            else:
                print("Opción inválida. Por favor seleccione 1, 2 o 3.")
    
    def _llamar_con_retry(self, prompt: str, contexto: str, max_tokens: int) -> str:
        """Llama a Claude con lógica de retry"""
        ultimo_error = None
        
        for intento in range(MAX_RETRIES):
            try:
                return self._realizar_llamada(prompt, contexto, max_tokens)
            except anthropic.RateLimitError as e:
                ultimo_error = e
                delay = RETRY_DELAY * (2 ** intento)  # Backoff exponencial
                self.logger.warning(f"Rate limit alcanzado, reintentando en {delay}s (intento {intento + 1}/{MAX_RETRIES})")
                time.sleep(delay)
            except anthropic.APIConnectionError as e:
                ultimo_error = e
                delay = RETRY_DELAY * (intento + 1)
                self.logger.warning(f"Error de conexión, reintentando en {delay}s (intento {intento + 1}/{MAX_RETRIES})")
                time.sleep(delay)
            except anthropic.APIStatusError as e:
                # Errores 5xx son retriables, 4xx no
                if e.status_code >= 500:
                    ultimo_error = e
                    delay = RETRY_DELAY * (intento + 1)
                    self.logger.warning(f"Error del servidor ({e.status_code}), reintentando en {delay}s (intento {intento + 1}/{MAX_RETRIES})")
                    time.sleep(delay)
                else:
                    # Error del cliente, no reintentar
                    self.logger.error(f"Error del cliente ({e.status_code}): {e}")
                    raise
            except Exception as e:
                # Para otros errores, no reintentar
                self.logger.error(f"Error no recuperable en llamada a Claude: {e}")
                raise
        
        # Si llegamos aquí, se agotaron los reintentos
        self.logger.error(f"Se agotaron los reintentos después de {MAX_RETRIES} intentos")
        raise ultimo_error
    
    def _realizar_llamada(self, prompt: str, contexto: str, max_tokens: int) -> str:
        """Realiza la llamada actual a Claude"""
        try:
            # Construir el mensaje con contexto si existe
            mensaje_completo = prompt
            if contexto:
                mensaje_completo = f"{prompt}\n\n{contexto}"
            
            # Validar longitud del mensaje
            self._validar_longitud_mensaje(mensaje_completo)
            
            # Verificar rate limit antes de hacer la llamada
            self._verificar_rate_limit(mensaje_completo)
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": mensaje_completo
                }]
            )
            
            # Validar que la respuesta tiene contenido
            if not response or not hasattr(response, 'content'):
                raise ValueError("La respuesta de Claude no tiene el formato esperado")
            
            if not response.content or len(response.content) == 0:
                raise ValueError("La respuesta de Claude está vacía")
            
            # Manejar diferentes tipos de contenido
            if isinstance(response.content, list):
                if len(response.content) == 0:
                    raise ValueError("La lista de contenido de Claude está vacía")
                contenido = response.content[0].text if hasattr(response.content[0], 'text') else str(response.content[0])
            else:
                contenido = response.content.text if hasattr(response.content, 'text') else str(response.content)
            
            # Validar contenido de respuesta
            if not contenido or not contenido.strip():
                raise ValueError("El contenido de respuesta de Claude está vacío")
            
            self.logger.debug(f"Respuesta de Claude recibida ({len(contenido)} caracteres)")
            return contenido
            
        except Exception as e:
            self.logger.error(f"Error en llamada a Claude: {e}")
            raise
    
    def _validar_longitud_mensaje(self, mensaje: str):
        """Valida que el mensaje no exceda límites razonables"""
        # Estimación aproximada: ~4 caracteres por token
        estimacion_tokens = len(mensaje) / 4
        
        if estimacion_tokens > MAX_INPUT_TOKENS * 0.9:  # Usar 90% del límite de entrada como umbral
            self.logger.warning(f"Mensaje muy largo (estimado: {estimacion_tokens:.0f} tokens), puede exceder el límite")
        
        # Límite absoluto de caracteres basado en tokens de entrada
        # Claude 3.5 Sonnet soporta 200K tokens, ~800K caracteres
        max_caracteres = MAX_INPUT_TOKENS * 4  # 800,000 caracteres aproximadamente
        if len(mensaje) > max_caracteres:
            raise ValueError(f"Mensaje demasiado largo: {len(mensaje)} caracteres (máximo: {max_caracteres})")
    
    def validar_conexion(self) -> bool:
        """Valida que la conexión con Claude funciona"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{
                    "role": "user", 
                    "content": "Test"
                }]
            )
            return bool(response.content)
        except Exception as e:
            self.logger.error(f"Error validando conexión con Claude: {e}")
            return False
    
    def obtener_info_modelo(self) -> dict:
        """Obtiene información sobre el modelo y configuración"""
        return {
            "model": self.model,
            "max_output_tokens": MAX_TOKENS,
            "max_input_tokens": MAX_INPUT_TOKENS,
            "max_retries": MAX_RETRIES,
            "retry_delay": RETRY_DELAY,
            "api_key_configured": bool(self.api_key)
        }
    
    def llamar_claude(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Método de compatibilidad"""
        return self.llamar_modelo(prompt, contexto, max_tokens)
    
    def calcular_costo_estimado(self, num_llamadas: int, tokens_promedio: int = 2000) -> dict:
        """Calcula el costo estimado basado en el número de llamadas"""
        # Precios de Claude Sonnet (pueden cambiar)
        precio_input_por_1k = 0.003  # USD por 1K tokens de entrada
        precio_output_por_1k = 0.015  # USD por 1K tokens de salida
        
        tokens_input_total = num_llamadas * tokens_promedio
        tokens_output_estimado = num_llamadas * (tokens_promedio * 0.5)  # Estimación conservadora
        
        costo_input = (tokens_input_total / 1000) * precio_input_por_1k
        costo_output = (tokens_output_estimado / 1000) * precio_output_por_1k
        costo_total = costo_input + costo_output
        
        return {
            "llamadas": num_llamadas,
            "tokens_input_estimados": tokens_input_total,
            "tokens_output_estimados": tokens_output_estimado,
            "costo_input_usd": round(costo_input, 4),
            "costo_output_usd": round(costo_output, 4),
            "costo_total_usd": round(costo_total, 4)
        } 


class OllamaClient(BaseAPIClient):
    """Cliente para interacción con Ollama local"""
    
    def __init__(self, model: str, base_url: str = "http://localhost:11434"):
        super().__init__()
        self.model = model
        self.base_url = base_url
        self.logger.info(f"Inicializando cliente Ollama con modelo: {model}")
        
        # Verificar que Ollama esté disponible
        if not self._verificar_ollama_disponible():
            raise ValueError(f"No se puede conectar con Ollama en {base_url}")
    
    def _verificar_ollama_disponible(self) -> bool:
        """Verifica que Ollama esté ejecutándose"""
        try:
            response = requests.get(f"{self.base_url}/api/version", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def llamar_modelo(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Realiza una llamada a Ollama"""
        try:
            mensaje_completo = prompt
            if contexto:
                mensaje_completo = f"{prompt}\n\n{contexto}"
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": mensaje_completo,
                    "stream": False,
                    "options": {
                        "num_predict": max_tokens
                    }
                },
                timeout=300  # 5 minutos para respuestas largas
            )
            
            if response.status_code != 200:
                raise Exception(f"Error de Ollama: {response.status_code} - {response.text}")
            
            result = response.json()
            return result.get('response', '')
            
        except Exception as e:
            self.logger.error(f"Error en llamada a Ollama: {e}")
            raise
    
    def validar_conexion(self) -> bool:
        """Valida que la conexión con Ollama funciona"""
        try:
            # Verificar que el modelo esté disponible
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                model_names = [m['name'] for m in models]
                
                # Verificar si el modelo existe (con o sin versión)
                model_base = self.model.split(':')[0]
                return any(model_base in name for name in model_names)
            return False
        except Exception as e:
            self.logger.error(f"Error validando conexión con Ollama: {e}")
            return False
    
    def obtener_info_modelo(self) -> dict:
        """Obtiene información sobre el modelo"""
        return {
            "model": self.model,
            "provider": "ollama",
            "base_url": self.base_url,
            "max_output_tokens": MAX_TOKENS,
            "local": True
        }
    
    def calcular_costo_estimado(self, num_llamadas: int, tokens_promedio: int = 2000) -> dict:
        """Calcula el costo estimado (gratis para Ollama)"""
        return {
            "llamadas": num_llamadas,
            "tokens_input_estimados": num_llamadas * tokens_promedio,
            "tokens_output_estimados": num_llamadas * (tokens_promedio * 0.5),
            "costo_input_usd": 0.0,
            "costo_output_usd": 0.0,
            "costo_total_usd": 0.0,
            "nota": "Ollama es gratuito (ejecución local)"
        }
    
    def llamar_claude(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Método de compatibilidad"""
        return self.llamar_modelo(prompt, contexto, max_tokens)


class OpenAIClient(BaseAPIClient):
    """Cliente para interacción con la API de OpenAI"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        super().__init__()
        
        if openai is None:
            raise ImportError("OpenAI library not installed. Please install with: pip install openai")
        
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model or "gpt-4-turbo-preview"
        
        if not self.api_key:
            raise ValueError("API key de OpenAI no configurada")
        
        self.logger.info(f"Inicializando cliente OpenAI con modelo: {self.model}")
        
        # Configurar cliente
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def llamar_modelo(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Realiza una llamada a OpenAI"""
        try:
            mensaje_completo = prompt
            if contexto:
                mensaje_completo = f"{prompt}\n\n{contexto}"
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Eres un asistente experto en evaluación de documentos técnicos."},
                    {"role": "user", "content": mensaje_completo}
                ],
                max_tokens=max_tokens,
                temperature=0.1  # Más determinístico para evaluaciones
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error en llamada a OpenAI: {e}")
            raise
    
    def validar_conexion(self) -> bool:
        """Valida que la conexión con OpenAI funciona"""
        try:
            # Hacer una llamada simple de prueba
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=10
            )
            return bool(response.choices)
        except Exception as e:
            self.logger.error(f"Error validando conexión con OpenAI: {e}")
            return False
    
    def obtener_info_modelo(self) -> dict:
        """Obtiene información sobre el modelo"""
        return {
            "model": self.model,
            "provider": "openai",
            "max_output_tokens": MAX_TOKENS,
            "api_key_configured": bool(self.api_key)
        }
    
    def calcular_costo_estimado(self, num_llamadas: int, tokens_promedio: int = 2000) -> dict:
        """Calcula el costo estimado basado en precios de OpenAI"""
        # Precios aproximados (pueden variar según el modelo)
        precios = {
            "gpt-4-turbo-preview": {"input": 0.01, "output": 0.03},
            "gpt-4": {"input": 0.03, "output": 0.06},
            "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015}
        }
        
        # Usar precio de GPT-4 Turbo por defecto
        precio = precios.get(self.model, precios["gpt-4-turbo-preview"])
        
        tokens_input_total = num_llamadas * tokens_promedio
        tokens_output_estimado = num_llamadas * (tokens_promedio * 0.5)
        
        costo_input = (tokens_input_total / 1000) * precio["input"]
        costo_output = (tokens_output_estimado / 1000) * precio["output"]
        costo_total = costo_input + costo_output
        
        return {
            "llamadas": num_llamadas,
            "tokens_input_estimados": tokens_input_total,
            "tokens_output_estimados": tokens_output_estimado,
            "costo_input_usd": round(costo_input, 4),
            "costo_output_usd": round(costo_output, 4),
            "costo_total_usd": round(costo_total, 4)
        }
    
    def llamar_claude(self, prompt: str, contexto: str = "", max_tokens: int = MAX_TOKENS) -> str:
        """Método de compatibilidad"""
        return self.llamar_modelo(prompt, contexto, max_tokens)


def crear_cliente_api(provider: str = "anthropic", api_key: Optional[str] = None, model: Optional[str] = None) -> BaseAPIClient:
    """Factory function para crear el cliente API apropiado"""
    
    if provider.lower() == "anthropic":
        return AnthropicClient(api_key=api_key, model=model)
    elif provider.lower() == "ollama":
        if not model:
            raise ValueError("Debe especificar un modelo para Ollama (ej: --ollama llama2)")
        return OllamaClient(model=model)
    elif provider.lower() == "openai":
        return OpenAIClient(api_key=api_key, model=model)
    else:
        raise ValueError(f"Provider no soportado: {provider}. Use 'anthropic', 'ollama' o 'openai'")


# Mantener compatibilidad con código existente
class APIClient(AnthropicClient):
    """Alias para mantener compatibilidad con código existente"""
    pass 