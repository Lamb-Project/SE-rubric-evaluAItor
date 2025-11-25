"""
Módulo de gestión de configuración y logging para el sistema de evaluación
"""

import os
import logging
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()


@dataclass
class EvaluacionConfig:
    """Configuración para el proceso de evaluación"""
    archivo_documento: str
    directorio_salida: str
    directorio_prompts: str = "./prompts"
    api_key: Optional[str] = None
    provider: str = "anthropic"  # anthropic, ollama, openai
    model: Optional[str] = None  # Model name for the provider


class ConfigManager:
    """Gestor de configuración y validación del sistema"""
    
    @staticmethod
    def setup_logging(directorio_salida: str, nivel_log: str = "INFO") -> logging.Logger:
        """Configura el sistema de logging"""
        # Crear directorio de salida si no existe
        Path(directorio_salida).mkdir(parents=True, exist_ok=True)
        
        # Configurar nivel de logging
        nivel_mapping = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR
        }
        nivel = nivel_mapping.get(nivel_log.upper(), logging.INFO)
        
        # Crear un logger único para este proceso
        logger_name = f"evaluador_{os.getpid()}"
        logger = logging.getLogger(logger_name)
        logger.setLevel(nivel)
        
        # Limpiar handlers existentes para evitar duplicados
        logger.handlers.clear()
        
        # Crear archivo de log con timestamp para evitar conflictos
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"evaluacion_{timestamp}.log"
        log_path = os.path.join(directorio_salida, log_filename)
        
        # Configurar handlers
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        console_handler = logging.StreamHandler()
        
        # Configurar formato
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Añadir handlers al logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        logger.info(f"Logging configurado. Archivo de log: {log_path}")
        
        return logger
    
    @staticmethod
    def validar_configuracion(config: EvaluacionConfig) -> bool:
        """Valida que la configuración sea correcta"""
        logger = logging.getLogger(__name__)
        
        # Validar archivo de documento
        if not os.path.exists(config.archivo_documento):
            logger.error(f"Archivo de documento no encontrado: {config.archivo_documento}")
            return False
        
        if not os.path.isfile(config.archivo_documento):
            logger.error(f"La ruta especificada no es un archivo: {config.archivo_documento}")
            return False
        
        # Validar directorio de prompts
        if not os.path.exists(config.directorio_prompts):
            logger.error(f"Directorio de prompts no encontrado: {config.directorio_prompts}")
            return False
        
        if not os.path.isdir(config.directorio_prompts):
            logger.error(f"La ruta de prompts no es un directorio: {config.directorio_prompts}")
            return False
        
        # Validar que se pueda crear el directorio de salida
        try:
            Path(config.directorio_salida).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"No se puede crear directorio de salida: {e}")
            return False
        
        # Validar API key
        if not ConfigManager.validar_api_key(config.api_key, config.provider):
            logger.error(f"API key no configurada o inválida para el provider: {config.provider}")
            return False
        
        logger.info("Configuración validada correctamente")
        return True
    
    @staticmethod
    def validar_api_key(api_key: Optional[str] = None, provider: str = "anthropic") -> bool:
        """Valida que la API key esté disponible y tenga formato válido"""
        # Ollama no necesita API key
        if provider.lower() == "ollama":
            return True
        
        # OpenAI
        if provider.lower() == "openai":
            key = api_key or os.environ.get("OPENAI_API_KEY")
            if not key:
                return False
            # OpenAI keys generalmente empiezan con sk-
            if not key.startswith("sk-"):
                return False
            if len(key) < 20:
                return False
            return True
        
        # Anthropic (default)
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        
        if not key:
            return False
        
        # Validar formato básico de API key de Anthropic
        if not key.startswith("sk-ant-"):
            return False
        
        if len(key) < 20:  # Longitud mínima razonable
            return False
        
        return True
    
    @staticmethod
    def crear_estructura_directorios(directorio_salida: str):
        """Crea la estructura de directorios necesaria"""
        output_path = Path(directorio_salida)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Crear subdirectorios si es necesario (para futuras extensiones)
        # (output_path / "temp").mkdir(exist_ok=True)
        # (output_path / "reports").mkdir(exist_ok=True) 