"""
Módulo de parsing y extracción de texto para el sistema de evaluación
"""

import re
import logging
from typing import Optional, Dict


class TextParser:
    """Parser de texto y extractor de información"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def extraer_valor_md(self, texto: str, patron: str) -> Optional[str]:
        """Extrae un valor específico del markdown usando regex"""
        try:
            match = re.search(patron, texto, re.MULTILINE | re.IGNORECASE)
            if match:
                return match.group(1).strip()
            return None
        except Exception as e:
            self.logger.error(f"Error en extraer_valor_md: {e}")
            return None
    
    def extraer_puntuacion_robusta(self, texto: str, criterio: str) -> Optional[str]:
        """Extrae puntuaciones usando múltiples patrones para mayor robustez"""
        # Lista de patrones ordenados por preferencia
        patrones = [
            # Patrón original más específico
            r"Puntuación Total:\s*(\d+\.?\d*)/10",
            r"Puntuación Total:\s*(\d+\.?\d*)\s*/\s*10",
            
            # Variaciones comunes
            r"Puntuación:\s*(\d+\.?\d*)/10",
            r"Puntuación:\s*(\d+\.?\d*)\s*/\s*10",
            r"Nota:\s*(\d+\.?\d*)/10",
            r"Nota:\s*(\d+\.?\d*)\s*/\s*10",
            r"Calificación:\s*(\d+\.?\d*)/10",
            r"Total:\s*(\d+\.?\d*)/10",
            
            # Patrones con texto adicional
            r"(?:Puntuación|Nota|Calificación|Total)(?:\s+(?:Final|Total))?:\s*(\d+\.?\d*)\s*/\s*10",
            
            # Patrones más flexibles
            r"(\d+\.?\d*)\s*/\s*10\s*puntos?",
            r"(\d+\.?\d*)\s*/\s*10\s*(?:sobre|de)\s*10",
            
            # Buscar cualquier número seguido de /10 al final de línea
            r"(\d+\.?\d*)\s*/\s*10\s*$",
            
            # Patrones en tablas o listas
            r"^\s*\|\s*.*?\|\s*(\d+\.?\d*)/10\s*\|",
            r"^\s*-\s*.*?(\d+\.?\d*)/10",
            
            # Último recurso: cualquier X/10 en el texto
            r"(\d+\.?\d*)/10"
        ]
        
        for i, patron in enumerate(patrones):
            try:
                match = re.search(patron, texto, re.MULTILINE | re.IGNORECASE)
                if match:
                    valor = match.group(1).strip()
                    if valor:  # Verificar que no está vacío
                        self.logger.debug(f"Puntuación extraída para {criterio} con patrón {i+1}: {valor}")
                        return valor
            except Exception as e:
                self.logger.debug(f"Error con patrón {i+1} para {criterio}: {e}")
                continue
                
        # Si no se encuentra con ningún patrón, buscar alternativas
        return self._buscar_puntuacion_alternativa(texto, criterio)
    
    def _buscar_puntuacion_alternativa(self, texto: str, criterio: str) -> Optional[str]:
        """Métodos alternativos para extraer puntuaciones cuando fallan los patrones principales"""
        try:
            # Buscar números decimales que podrían ser puntuaciones
            numeros_encontrados = re.findall(r'\b(\d+\.?\d*)\b', texto)
            
            if numeros_encontrados:
                # Filtrar números que estén en rango válido (0-10)
                candidatos = []
                for num_str in numeros_encontrados:
                    try:
                        num = float(num_str)
                        if 0 <= num <= 10:
                            candidatos.append(num_str)
                    except ValueError:
                        continue
                
                if candidatos:
                    # Tomar el último candidato válido (suele ser la puntuación final)
                    resultado = candidatos[-1]
                    self.logger.warning(f"Puntuación para {criterio} extraída usando método alternativo: {resultado}")
                    return resultado
            
            self.logger.warning(f"No se pudo extraer puntuación para {criterio}")
            return None
        except Exception as e:
            self.logger.error(f"Error en búsqueda alternativa para {criterio}: {e}")
            return None
    
    def extraer_seccion_md(self, texto: str, titulo_seccion: str) -> str:
        """Extrae una sección completa del markdown"""
        try:
            # Buscar desde el título hasta el siguiente título del mismo nivel o EOF
            patron = rf"(#{1,3})\s*{re.escape(titulo_seccion)}.*?\n(.*?)(?=\n\1\s|\Z)"
            match = re.search(patron, texto, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(2).strip()
            return ""
        except Exception as e:
            self.logger.error(f"Error extrayendo sección '{titulo_seccion}': {e}")
            return ""
    
    def convertir_a_float_seguro(self, valor: str, criterio: str) -> float:
        """Convierte un string a float de forma segura"""
        if not valor:
            self.logger.warning(f"No se encontró puntuación para {criterio}, usando 0.0")
            return 0.0
        
        try:
            resultado = float(valor)
            if resultado < 0 or resultado > 10:
                self.logger.warning(f"Puntuación fuera de rango para {criterio}: {resultado}, limitando a [0-10]")
                return max(0.0, min(10.0, resultado))
            return resultado
        except (ValueError, TypeError) as e:
            self.logger.error(f"Error convirtiendo puntuación para {criterio}: '{valor}' - {e}")
            return 0.0
    
    def limpiar_texto(self, texto: str) -> str:
        """Limpia el texto de caracteres no deseados"""
        try:
            # Normalizar espacios en blanco
            texto = re.sub(r'\s+', ' ', texto)
            # Eliminar espacios al inicio y final
            texto = texto.strip()
            return texto
        except Exception as e:
            self.logger.error(f"Error limpiando texto: {e}")
            return texto
    
    def extraer_todas_puntuaciones(self, resultados_md: Dict[str, str]) -> Dict[str, float]:
        """Extrae todas las puntuaciones de los resultados markdown"""
        puntuaciones = {}
        
        criterios = {
            'objetivos': '3_1_eval_objetivos',
            'requisitos_info': '3_2_eval_requisitos_info', 
            'requisitos_nf': '3_3_eval_requisitos_nf',
            'casos_uso': '3_4_eval_casos_uso',
            'matrices': '3_5_eval_matrices'
        }
        
        for criterio, clave_resultado in criterios.items():
            texto_eval = resultados_md.get(clave_resultado, '')
            punt_str = self.extraer_puntuacion_robusta(texto_eval, criterio)
            puntuaciones[criterio] = self.convertir_a_float_seguro(punt_str, criterio)
        
        return puntuaciones
    
    def reemplazar_variables_seguro(self, template: str, variables: Dict[str, str]) -> str:
        """Reemplaza variables en templates usando marcadores seguros"""
        resultado = template
        
        # Diccionario de reemplazos con marcadores seguros
        for variable, valor in variables.items():
            # Marcador seguro formato: --{VARIABLE}--
            marcador_seguro = f"--{{{variable.upper()}}}--"
            
            # También soportar el formato anterior por compatibilidad
            marcador_legacy = f"[{variable.upper()}]"
            
            # Reemplazar ambos formatos
            resultado = resultado.replace(marcador_seguro, valor)
            resultado = resultado.replace(marcador_legacy, valor)
            
            self.logger.debug(f"Reemplazado {marcador_seguro} -> {len(valor)} caracteres")
        
        return resultado
    
    def validar_template(self, template: str) -> Dict[str, list]:
        """Valida un template y devuelve información sobre las variables encontradas"""
        import re
        
        # Buscar marcadores seguros: --{VARIABLE}--
        marcadores_seguros = re.findall(r'--\{([A-Z_]+)\}--', template)
        
        # Buscar marcadores legacy: [VARIABLE]
        marcadores_legacy = re.findall(r'\[([A-Z_]+)\]', template)
        
        return {
            'marcadores_seguros': marcadores_seguros,
            'marcadores_legacy': marcadores_legacy,
            'total_variables': len(set(marcadores_seguros + marcadores_legacy))
        } 