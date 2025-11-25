#!/usr/bin/env python3
"""
Sistema de Evaluación Automatizada de Proyectos - Versión Streaming
Utiliza modelos de IA con streaming para evaluar trabajos según rúbrica
Soporta Anthropic Claude, Ollama y OpenAI con timeouts extendidos
"""

import os
import sys
import argparse
import logging
from typing import Dict, Optional, List
from pathlib import Path

# Imports de módulos locales
from utils.config_manager import ConfigManager, EvaluacionConfig
from utils.file_handler import FileHandler
from utils.text_parser import TextParser
from utils.api_client_streaming import APIClient, crear_cliente_api
from utils.report_generator import ReportGenerator

class EvaluadorProyecto:
    """Clase principal para evaluar proyectos usando IA con streaming"""

    # Definir los prompts requeridos
    PROMPTS_REQUERIDOS = [
        "1_1_extraccion_objetivos",
        "1_2_extraccion_requisitos",
        "1_3_extraccion_casos_de_uso",
        "2_1_analisis_trazabilidad",
        "2_2_analisis_completitud",
        "3_1_evaluacion_objetivos",
        "3_1_evaluacion_requisitos_info",
        "3_2_evaluacion_requisitos_info",
        "3_3_evaluacion_requisitos_nf",
        "3_4_evaluacion_caso_uso",
        "3_5_evaluacion_matrices",
        "4_1_generacion_informe"
    ]

    def __init__(self, config: EvaluacionConfig):
        # Validar configuración
        if not ConfigManager.validar_configuracion(config):
            raise ValueError("Configuración inválida")

        self.config = config
        self.logger = ConfigManager.setup_logging(config.directorio_salida)

        # Inicializar módulos utilitarios
        self.file_handler = FileHandler(config.directorio_salida, config.directorio_prompts)
        self.text_parser = TextParser()
        self.api_client = crear_cliente_api(
            provider=config.provider,
            api_key=config.api_key,
            model=config.model
        )
        self.report_generator = ReportGenerator(config.archivo_documento)

        self.resultados_md = {}  # Almacena resultados en formato markdown

        # Validar prompts al inicio
        self._validar_prompts_requeridos()

    def _validar_prompts_requeridos(self):
        """Valida que todos los prompts requeridos existan"""
        self.logger.info("Validando archivos de prompts requeridos...")
        prompts_faltantes = []

        for prompt in self.PROMPTS_REQUERIDOS:
            prompt_path = Path(self.config.directorio_prompts) / f"{prompt}.md"
            if not prompt_path.exists():
                prompts_faltantes.append(prompt)

        if prompts_faltantes:
            self.logger.error(f"Prompts faltantes: {', '.join(prompts_faltantes)}")
            raise FileNotFoundError(f"Los siguientes prompts son requeridos pero no se encontraron: {', '.join(prompts_faltantes)}")

        self.logger.info("Todos los prompts requeridos están presentes")

    def leer_documento(self) -> str:
        """Lee el documento a evaluar"""
        return self.file_handler.leer_documento(self.config.archivo_documento)

    def leer_prompt(self, nombre_prompt: str) -> str:
        """Lee un prompt desde archivo"""
        return self.file_handler.leer_prompt(nombre_prompt)

    def llamar_claude(self, prompt: str, contexto: str = "") -> str:
        """Realiza una llamada a Claude con el prompt dado"""
        return self.api_client.llamar_claude(prompt, contexto)

    def guardar_resultado_md(self, nombre: str, contenido: str):
        """Guarda un resultado en formato markdown"""
        success = self.file_handler.guardar_resultado_md(nombre, contenido)
        if success:
            self.resultados_md[nombre] = contenido
        else:
            raise RuntimeError(f"No se pudo guardar el resultado: {nombre}")

    def extraer_valor_md(self, texto: str, patron: str) -> Optional[str]:
        """Extrae un valor específico del markdown usando regex"""
        return self.text_parser.extraer_valor_md(texto, patron)

    def extraer_seccion_md(self, texto: str, titulo_seccion: str) -> str:
        """Extrae una sección completa del markdown"""
        return self.text_parser.extraer_seccion_md(texto, titulo_seccion)

    def fase1_extraccion(self, documento: str):
        """Fase 1: Extracción de información"""
        self.logger.info("=== FASE 1: EXTRACCIÓN DE INFORMACIÓN ===")

        # 1.1 Extraer objetivos
        self.logger.info("Extrayendo objetivos...")
        prompt_objetivos = self.leer_prompt("1_1_extraccion_objetivos")
        prompt_objetivos = self.text_parser.reemplazar_variables_seguro(
            prompt_objetivos, {"documento": documento}
        )
        respuesta = self.llamar_claude(prompt_objetivos)
        self.guardar_resultado_md("1_1_objetivos", respuesta)

        # 1.2 Extraer requisitos
        self.logger.info("Extrayendo requisitos...")
        prompt_requisitos = self.leer_prompt("1_2_extraccion_requisitos")
        prompt_requisitos = self.text_parser.reemplazar_variables_seguro(
            prompt_requisitos, {"documento": documento}
        )
        respuesta = self.llamar_claude(prompt_requisitos)
        self.guardar_resultado_md("1_2_requisitos", respuesta)

        # 1.3 Extraer casos de uso
        self.logger.info("Extrayendo casos de uso...")
        prompt_casos = self.leer_prompt("1_3_extraccion_casos_de_uso")
        prompt_casos = self.text_parser.reemplazar_variables_seguro(
            prompt_casos, {"documento": documento}
        )
        respuesta = self.llamar_claude(prompt_casos)
        self.guardar_resultado_md("1_3_casos_uso", respuesta)

    def fase2_coherencia(self):
        """Fase 2: Análisis de coherencia"""
        self.logger.info("=== FASE 2: ANÁLISIS DE COHERENCIA ===")

        # 2.1 Análisis de trazabilidad
        self.logger.info("Analizando trazabilidad...")
        prompt_trazabilidad = self.leer_prompt("2_1_analisis_trazabilidad")
        prompt_trazabilidad = self.text_parser.reemplazar_variables_seguro(
            prompt_trazabilidad, {
                "objetivos": self.resultados_md.get('1_1_objetivos', 'No disponible'),
                "requisitos": self.resultados_md.get('1_2_requisitos', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_trazabilidad)
        self.guardar_resultado_md("2_1_trazabilidad", respuesta)

        # 2.2 Análisis de completitud
        self.logger.info("Analizando completitud...")
        prompt_completitud = self.leer_prompt("2_2_analisis_completitud")
        prompt_completitud = self.text_parser.reemplazar_variables_seguro(
            prompt_completitud, {
                "requisitos": self.resultados_md.get('1_2_requisitos', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_completitud)
        self.guardar_resultado_md("2_2_completitud", respuesta)

    def fase3_evaluacion_criterios(self):
        """Fase 3: Evaluación específica por criterio"""
        self.logger.info("=== FASE 3: EVALUACIÓN POR CRITERIOS ===")

        # 3.1 Evaluación de objetivos (20%)
        self.logger.info("Evaluando objetivos...")
        prompt_eval_obj = self.leer_prompt("3_1_evaluacion_objetivos")
        prompt_eval_obj = self.text_parser.reemplazar_variables_seguro(
            prompt_eval_obj, {
                "objetivos": self.resultados_md.get('1_1_objetivos', 'No disponible'),
                "trazabilidad": self.resultados_md.get('2_1_trazabilidad', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_eval_obj)
        self.guardar_resultado_md("3_1_eval_objetivos", respuesta)

        # 3.2 Evaluación de requisitos de información (15%)
        self.logger.info("Evaluando requisitos de información...")
        prompt_eval_req_info = self.leer_prompt("3_2_evaluacion_requisitos_info")
        prompt_eval_req_info = self.text_parser.reemplazar_variables_seguro(
            prompt_eval_req_info, {
                "requisitos": self.resultados_md.get('1_2_requisitos', 'No disponible'),
                "completitud": self.resultados_md.get('2_2_completitud', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_eval_req_info)
        self.guardar_resultado_md("3_2_eval_requisitos_info", respuesta)

        # 3.3 Evaluación de requisitos no funcionales (10%)
        self.logger.info("Evaluando requisitos no funcionales...")
        prompt_eval_req_nf = self.leer_prompt("3_3_evaluacion_requisitos_nf")
        prompt_eval_req_nf = self.text_parser.reemplazar_variables_seguro(
            prompt_eval_req_nf, {
                "requisitos": self.resultados_md.get('1_2_requisitos', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_eval_req_nf)
        self.guardar_resultado_md("3_3_eval_requisitos_nf", respuesta)

        # 3.4 Evaluación de casos de uso (35%)
        self.logger.info("Evaluando casos de uso...")
        prompt_eval_cu = self.leer_prompt("3_4_evaluacion_caso_uso")
        prompt_eval_cu = self.text_parser.reemplazar_variables_seguro(
            prompt_eval_cu, {
                "casos_uso": self.resultados_md.get('1_3_casos_uso', 'No disponible'),
                "objetivos": self.resultados_md.get('1_1_objetivos', 'No disponible'),
                "requisitos": self.resultados_md.get('1_2_requisitos', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_eval_cu)
        self.guardar_resultado_md("3_4_eval_casos_uso", respuesta)

        # 3.5 Evaluación de matrices (20%)
        self.logger.info("Evaluando matrices de trazabilidad...")
        prompt_eval_matrices = self.leer_prompt("3_5_evaluacion_matrices")
        prompt_eval_matrices = self.text_parser.reemplazar_variables_seguro(
            prompt_eval_matrices, {
                "trazabilidad": self.resultados_md.get('2_1_trazabilidad', 'No disponible')
            }
        )
        respuesta = self.llamar_claude(prompt_eval_matrices)
        self.guardar_resultado_md("3_5_eval_matrices", respuesta)

    def extraer_puntuaciones(self) -> Dict[str, float]:
        """Extrae las puntuaciones numéricas de los archivos markdown"""
        return self.text_parser.extraer_todas_puntuaciones(self.resultados_md)

    def calcular_nota_final(self, puntuaciones: Dict[str, float]) -> float:
        """Calcula la nota final ponderada"""
        return self.report_generator.calcular_nota_final(puntuaciones)

    def fase4_sintesis(self):
        """Fase 4: Síntesis y calificación final"""
        self.logger.info("=== FASE 4: SÍNTESIS Y CALIFICACIÓN FINAL ===")

        # Extraer puntuaciones numéricas
        puntuaciones = self.extraer_puntuaciones()
        nota_final = self.calcular_nota_final(puntuaciones)

        # Generar informe final
        prompt_informe = self.leer_prompt("4_1_generacion_informe")

        # Preparar texto de puntuaciones
        puntuaciones_texto = f"""- Objetivos: {puntuaciones.get('objetivos', 0)}/10
- Requisitos de Información: {puntuaciones.get('requisitos_info', 0)}/10
- Requisitos No Funcionales: {puntuaciones.get('requisitos_nf', 0)}/10
- Casos de Uso: {puntuaciones.get('casos_uso', 0)}/10
- Matrices: {puntuaciones.get('matrices', 0)}/10"""

        prompt_informe = self.text_parser.reemplazar_variables_seguro(
            prompt_informe, {
                "eval_objetivos": self.resultados_md.get('3_1_eval_objetivos', 'No disponible'),
                "eval_requisitos_info": self.resultados_md.get('3_2_eval_requisitos_info', 'No disponible'),
                "eval_requisitos_nf": self.resultados_md.get('3_3_eval_requisitos_nf', 'No disponible'),
                "eval_casos_uso": self.resultados_md.get('3_4_eval_casos_uso', 'No disponible'),
                "eval_matrices": self.resultados_md.get('3_5_eval_matrices', 'No disponible'),
                "puntuaciones": puntuaciones_texto,
                "nota_final": str(nota_final)
            }
        )
        respuesta = self.llamar_claude(prompt_informe)

        # Generar documento final con la rúbrica
        self.generar_documento_final(respuesta, puntuaciones)

    def generar_documento_final(self, informe_sintesis: str, puntuaciones: Dict[str, float]):
        """Genera el documento markdown final con la rúbrica completa"""
        self.logger.info("Generando documento final...")

        documento_final = self.report_generator.generar_documento_final(
            informe_sintesis, puntuaciones, self.resultados_md
        )

        # Generar nombre del archivo final basado en el archivo de entrada
        nombre_archivo_entrada = Path(self.config.archivo_documento).stem
        nombre_archivo_final = f"Evaluación-Final-{nombre_archivo_entrada}"

        # Guardar documento final
        self.guardar_resultado_md(nombre_archivo_final, documento_final)

    def validar_configuracion_completa(self) -> bool:
        """Realiza una validación completa de la configuración antes de iniciar"""
        self.logger.info("=== VALIDACIÓN DE CONFIGURACIÓN ===")

        errores = []
        advertencias = []

        # 1. Validar documento de entrada
        try:
            doc_size = self.file_handler.obtener_tamano_archivo(self.config.archivo_documento)
            if doc_size is None:
                errores.append("No se puede leer el archivo de documento")
            elif doc_size == 0:
                errores.append("El archivo de documento está vacío")
            elif doc_size > 10 * 1024 * 1024:  # 10MB
                advertencias.append(f"El archivo es muy grande ({doc_size / 1024 / 1024:.1f}MB), puede tardar más en procesarse")
        except Exception as e:
            errores.append(f"Error verificando documento: {e}")

        # 2. Validar conexión con API
        provider_name = self.config.provider.capitalize()
        self.logger.info(f"Validando conexión con {provider_name}...")
        if not self.api_client.validar_conexion():
            errores.append(f"No se puede conectar con la API de {provider_name}")
        else:
            self.logger.info(f"✓ Conexión con {provider_name} validada")

        # 3. Validar permisos de escritura
        if not self.file_handler.validar_directorio_escribible(self.config.directorio_salida):
            errores.append(f"No se puede escribir en el directorio: {self.config.directorio_salida}")

        # 4. Estimar costo
        info_modelo = self.api_client.obtener_info_modelo()
        costo_estimado = self.api_client.calcular_costo_estimado(
            num_llamadas=len(self.PROMPTS_REQUERIDOS),
            tokens_promedio=3000
        )

        # Mostrar resumen
        print("\n" + "="*60)
        print("RESUMEN DE CONFIGURACIÓN")
        print("="*60)
        print(f"📄 Documento: {os.path.basename(self.config.archivo_documento)}")
        print(f"📁 Salida: {self.config.directorio_salida}")
        print(f"🤖 Modelo: {info_modelo['model']}")
        print(f"🔧 Provider: {info_modelo.get('provider', self.config.provider).upper()}")
        print(f"💰 Costo estimado: ${costo_estimado['costo_total_usd']:.2f} USD")
        if 'nota' in costo_estimado:
            print(f"   {costo_estimado['nota']}")
        print(f"⏱️  Tiempo estimado: 5-10 minutos (con streaming)")
        print(f"🌊 Modo: Streaming activado")

        if advertencias:
            print("\n⚠️  ADVERTENCIAS:")
            for adv in advertencias:
                print(f"   - {adv}")

        if errores:
            print("\n❌ ERRORES ENCONTRADOS:")
            for error in errores:
                print(f"   - {error}")
            print("\nNo se puede continuar con la evaluación.")
            return False

        print("\n✅ Configuración válida")

        # Preguntar confirmación
        respuesta = input("\n¿Desea continuar con la evaluación? (s/n): ").strip().lower()
        return respuesta in ['s', 'si', 'sí', 'yes', 'y']

    def ejecutar_evaluacion(self):
        """Ejecuta el proceso completo de evaluación"""
        try:
            # Validar configuración completa
            if not self.validar_configuracion_completa():
                self.logger.info("Evaluación cancelada por el usuario")
                return

            self.logger.info("Iniciando proceso de evaluación con streaming...")

            # Leer documento
            documento = self.leer_documento()

            # Ejecutar fases
            self.fase1_extraccion(documento)
            self.fase2_coherencia()
            self.fase3_evaluacion_criterios()
            self.fase4_sintesis()

            self.logger.info("Evaluación completada exitosamente")
            nombre_archivo_entrada = Path(self.config.archivo_documento).stem
            nombre_archivo_final = f"Evaluación-Final-{nombre_archivo_entrada}.md"
            self.logger.info(f"Revise el archivo {nombre_archivo_final} en {self.config.directorio_salida}")

        except Exception as e:
            self.logger.error(f"Error durante la evaluación: {e}")
            raise

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description='Sistema de Evaluación Automatizada con Streaming',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s documento.md ./resultados
  %(prog)s documento.md ./resultados --prompts ./mis_prompts
  %(prog)s documento.md ./resultados --api-key sk-ant-...
  %(prog)s documento.md ./resultados --ollama llama2
  %(prog)s documento.md ./resultados --ollama mistral:latest
  %(prog)s documento.md ./resultados --openai gpt-4-turbo-preview
  %(prog)s documento.md ./resultados --openai gpt-3.5-turbo
  %(prog)s --input-dir ./documentos ./resultados
        """
    )
    # Crear grupo mutuamente excluyente para archivo vs directorio
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('archivo', nargs='?', help='Archivo del documento a evaluar')
    group.add_argument('--input-dir', help='Directorio que contiene archivos .md a evaluar')

    parser.add_argument('salida', help='Directorio de salida para resultados')
    parser.add_argument('--prompts', default='./prompts', help='Directorio con archivos de prompts (default: ./prompts)')
    parser.add_argument('--api-key', help='API Key de Anthropic (o usar variable de entorno ANTHROPIC_API_KEY)')
    parser.add_argument('--ollama', metavar='MODEL', help='Usar Ollama con el modelo especificado (ej: llama2, mistral)')
    parser.add_argument('--openai', metavar='MODEL', help='Usar OpenAI con el modelo especificado (ej: gpt-4-turbo-preview)')
    parser.add_argument('--debug', action='store_true', help='Activar modo debug con más información')

    args = parser.parse_args()

    # Configurar nivel de log
    nivel_log = "DEBUG" if args.debug else "INFO"

    try:
        # Determinar si procesamos un archivo individual o un directorio
        archivos_a_procesar = []
        if args.input_dir:
            # Validar que el directorio existe
            if not os.path.exists(args.input_dir):
                print(f"❌ Error: El directorio '{args.input_dir}' no existe")
                sys.exit(1)
            if not os.path.isdir(args.input_dir):
                print(f"❌ Error: '{args.input_dir}' no es un directorio")
                sys.exit(1)

            # Encontrar todos los archivos .md en el directorio
            archivos_md = list(Path(args.input_dir).glob("*.md"))
            if not archivos_md:
                print(f"❌ Error: No se encontraron archivos .md en el directorio '{args.input_dir}'")
                sys.exit(1)

            archivos_a_procesar = [str(f) for f in archivos_md]
            print(f"📁 Procesando {len(archivos_a_procesar)} archivos .md del directorio: {args.input_dir}")
        else:
            # Validar que el archivo existe
            if not os.path.exists(args.archivo):
                print(f"❌ Error: El archivo '{args.archivo}' no existe")
                sys.exit(1)
            archivos_a_procesar = [args.archivo]

        # Validar que el directorio de prompts existe
        if not os.path.exists(args.prompts):
            print(f"❌ Error: El directorio de prompts '{args.prompts}' no existe")
            sys.exit(1)

        # Determinar provider y modelo
        if args.ollama:
            provider = "ollama"
            model = args.ollama
            api_key = None
        elif args.openai:
            provider = "openai"
            model = args.openai
            api_key = args.api_key
        else:
            provider = "anthropic"
            model = None  # Usará el modelo por defecto de Anthropic
            api_key = args.api_key

        # Procesar cada archivo
        for i, archivo in enumerate(archivos_a_procesar, 1):
            archivo_abs = os.path.abspath(archivo)

            if len(archivos_a_procesar) > 1:
                print(f"\n{'='*60}")
                print(f"PROCESANDO ARCHIVO {i}/{len(archivos_a_procesar)}: {os.path.basename(archivo)}")
                print(f"{'='*60}")

            # Crear configuración para este archivo
            config = EvaluacionConfig(
                archivo_documento=archivo_abs,
                directorio_salida=os.path.abspath(args.salida),
                directorio_prompts=os.path.abspath(args.prompts),
                api_key=api_key,
                provider=provider,
                model=model
            )

            # Mostrar banner solo para el primer archivo o cuando procesamos uno solo
            if i == 1:
                print("\n" + "="*60)
                print("SISTEMA DE EVALUACIÓN AUTOMATIZADA DE PROYECTOS")
                print("Versión con Streaming - Timeouts Extendidos")
                if provider == "ollama":
                    print(f"Powered by Ollama ({model})")
                elif provider == "openai":
                    print(f"Powered by OpenAI ({model or 'gpt-4-turbo-preview'})")
                else:
                    print("Powered by Claude 3 Sonnet")
                print("="*60 + "\n")

            # Ejecutar evaluación
            evaluador = EvaluadorProyecto(config)
            evaluador.ejecutar_evaluacion()

        print("\n✅ Evaluación completada exitosamente")
        print(f"📁 Resultados guardados en: {os.path.abspath(args.salida)}")
        if len(archivos_a_procesar) == 1:
            nombre_archivo = Path(archivos_a_procesar[0]).stem
            print(f"📄 Archivo principal: Evaluación-Final-{nombre_archivo}.md")
        else:
            print(f"📄 Archivos generados: {len(archivos_a_procesar)} evaluaciones finales")

    except KeyboardInterrupt:
        print("\n\n⚠️  Evaluación interrumpida por el usuario")
        sys.exit(130)
    except FileNotFoundError as e:
        print(f"\n❌ Error: Archivo no encontrado - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"\n❌ Error de configuración: {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"\n❌ Error de permisos: {e}")
        print("Verifique que tiene permisos de escritura en el directorio de salida")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        print("\nUse --debug para ver más detalles del error")
        sys.exit(1)

if __name__ == "__main__":
    main()
