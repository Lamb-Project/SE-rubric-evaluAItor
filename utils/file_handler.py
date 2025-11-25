"""
Módulo de manejo de archivos para el sistema de evaluación
"""

import os
import logging
from pathlib import Path
from typing import Optional


class FileHandler:
    """Manejador de operaciones de archivos"""
    
    def __init__(self, directorio_salida: str, directorio_prompts: str = "./prompts"):
        self.directorio_salida = directorio_salida
        self.directorio_prompts = directorio_prompts
        self.logger = logging.getLogger(__name__)
    
    def leer_documento(self, archivo_documento: str) -> str:
        """Lee el documento a evaluar"""
        try:
            with open(archivo_documento, 'r', encoding='utf-8') as f:
                contenido = f.read()
                if not contenido.strip():
                    raise ValueError("El documento está vacío")
                return contenido
        except FileNotFoundError:
            self.logger.error(f"Archivo no encontrado: {archivo_documento}")
            raise
        except UnicodeDecodeError:
            self.logger.error(f"Error de codificación al leer: {archivo_documento}")
            raise
        except Exception as e:
            self.logger.error(f"Error leyendo documento: {e}")
            raise
    
    def leer_prompt(self, nombre_prompt: str) -> str:
        """Lee un prompt desde archivo"""
        prompt_path = Path(self.directorio_prompts) / f"{nombre_prompt}.md"
        
        # Validar que el archivo existe
        if not prompt_path.exists():
            raise FileNotFoundError(f"Archivo de prompt no encontrado: {prompt_path}")
        
        if not prompt_path.is_file():
            raise ValueError(f"La ruta especificada no es un archivo: {prompt_path}")
            
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                contenido = f.read().strip()
                if not contenido:
                    raise ValueError(f"El archivo de prompt está vacío: {prompt_path}")
                return contenido
        except Exception as e:
            self.logger.error(f"Error leyendo prompt {nombre_prompt}: {e}")
            raise
    
    def guardar_resultado_md(self, nombre: str, contenido: str) -> bool:
        """Guarda un resultado en formato markdown"""
        try:
            output_path = Path(self.directorio_salida)
            output_path.mkdir(parents=True, exist_ok=True)
            
            file_path = output_path / f"{nombre}.md"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(contenido)
                    
            self.logger.info(f"Guardado: {file_path}")
            return True
            
        except PermissionError:
            self.logger.error(f"Sin permisos para escribir en: {self.directorio_salida}")
            return False
        except OSError as e:
            self.logger.error(f"Error del sistema al guardar {nombre}: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Error inesperado guardando {nombre}: {e}")
            return False
    
    def validar_archivo_existe(self, ruta_archivo: str) -> bool:
        """Valida que un archivo existe y es accesible"""
        try:
            path = Path(ruta_archivo)
            return path.exists() and path.is_file() and os.access(path, os.R_OK)
        except Exception:
            return False
    
    def validar_directorio_escribible(self, ruta_directorio: str) -> bool:
        """Valida que un directorio es escribible"""
        try:
            path = Path(ruta_directorio)
            path.mkdir(parents=True, exist_ok=True)
            return os.access(path, os.W_OK)
        except Exception:
            return False
    
    def listar_prompts_disponibles(self) -> list:
        """Lista todos los prompts disponibles en el directorio"""
        try:
            prompt_path = Path(self.directorio_prompts)
            if not prompt_path.exists():
                return []
            
            prompts = []
            for archivo in prompt_path.glob("*.md"):
                prompts.append(archivo.stem)
            
            return sorted(prompts)
        except Exception as e:
            self.logger.error(f"Error listando prompts: {e}")
            return []
    
    def obtener_tamano_archivo(self, ruta_archivo: str) -> Optional[int]:
        """Obtiene el tamaño de un archivo en bytes"""
        try:
            return os.path.getsize(ruta_archivo)
        except Exception:
            return None 