"""
Modelos de datos para el sistema de evaluación
"""

from dataclasses import dataclass
from typing import Optional, Dict
from datetime import datetime


@dataclass
class EvaluacionConfig:
    """Configuración para el proceso de evaluación"""
    archivo_documento: str
    directorio_salida: str
    directorio_prompts: str = "./prompts"
    api_key: Optional[str] = None


@dataclass
class PuntuacionResult:
    """Resultado de puntuación para un criterio específico"""
    criterio: str
    puntuacion: float
    peso: float
    nota_ponderada: float
    descripcion: str
    
    @property
    def es_aprobatorio(self) -> bool:
        """Indica si la puntuación es aprobatoria (>= 5.0)"""
        return self.puntuacion >= 5.0


@dataclass
class CriterioEvaluacion:
    """Definición de un criterio de evaluación"""
    nombre: str
    peso: float
    descripcion: str
    puntuacion_minima: float = 0.0
    puntuacion_maxima: float = 10.0 