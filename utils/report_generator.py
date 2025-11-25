"""
Módulo de generación de reportes para el sistema de evaluación
"""

import logging
from datetime import datetime
from typing import Dict


class ReportGenerator:
    """Generador de reportes de evaluación"""
    
    def __init__(self, archivo_evaluado: str):
        self.archivo_evaluado = archivo_evaluado
        self.logger = logging.getLogger(__name__)
    
    def calcular_nota_final(self, puntuaciones: Dict[str, float]) -> float:
        """Calcula la nota final ponderada"""
        pesos = {
            'objetivos': 0.20,
            'requisitos_info': 0.15,
            'requisitos_nf': 0.10,
            'casos_uso': 0.35,
            'matrices': 0.20
        }
        
        nota_final = 0.0
        for criterio, peso in pesos.items():
            nota_final += puntuaciones.get(criterio, 0.0) * peso
            
        return round(nota_final, 2)
    
    def generar_tabla_rubrica(self, puntuaciones: Dict[str, float], nota_final: float) -> str:
        """Genera la tabla de rúbrica en formato markdown"""
        return f"""| Criterio | Peso | Descripción | Puntuación | Nota Ponderada |
|----------|------|-------------|------------|----------------|
| **Objetivos** | 20% | Claridad, especificidad y alineación con el problema | {puntuaciones.get('objetivos', 0):.1f}/10 | {puntuaciones.get('objetivos', 0) * 0.20:.2f} |
| **Requisitos de Información** | 15% | Completitud y relevancia de requisitos de información | {puntuaciones.get('requisitos_info', 0):.1f}/10 | {puntuaciones.get('requisitos_info', 0) * 0.15:.2f} |
| **Requisitos No Funcionales** | 10% | Cobertura y especificidad de requisitos no funcionales | {puntuaciones.get('requisitos_nf', 0):.1f}/10 | {puntuaciones.get('requisitos_nf', 0) * 0.10:.2f} |
| **Casos de Uso** | 35% | Completitud, coherencia y calidad de casos de uso | {puntuaciones.get('casos_uso', 0):.1f}/10 | {puntuaciones.get('casos_uso', 0) * 0.35:.2f} |
| **Matrices de Trazabilidad** | 20% | Trazabilidad y coherencia entre elementos | {puntuaciones.get('matrices', 0):.1f}/10 | {puntuaciones.get('matrices', 0) * 0.20:.2f} |
| **TOTAL** | **100%** | | | **{nota_final:.2f}/10** |"""
    
    def generar_seccion_anexos(self, resultados_md: Dict[str, str]) -> str:
        """Genera la sección de anexos con evaluaciones detalladas"""
        anexos = """## Anexo: Evaluaciones Detalladas por Criterio

### 1. Objetivos (20%)
{objetivos}

### 2. Requisitos de Información (15%)
{requisitos_info}

### 3. Requisitos No Funcionales (10%)
{requisitos_nf}

### 4. Casos de Uso (35%)
{casos_uso}

### 5. Matrices de Trazabilidad (20%)
{matrices}""".format(
            objetivos=resultados_md.get('3_1_eval_objetivos', 'No disponible'),
            requisitos_info=resultados_md.get('3_2_eval_requisitos_info', 'No disponible'),
            requisitos_nf=resultados_md.get('3_3_eval_requisitos_nf', 'No disponible'),
            casos_uso=resultados_md.get('3_4_eval_casos_uso', 'No disponible'),
            matrices=resultados_md.get('3_5_eval_matrices', 'No disponible')
        )
        
        return anexos
    
    def generar_documento_final(self, informe_sintesis: str, puntuaciones: Dict[str, float], 
                              resultados_md: Dict[str, str]) -> str:
        """Genera el documento markdown final con la rúbrica completa"""
        nota_final = self.calcular_nota_final(puntuaciones)
        tabla_rubrica = self.generar_tabla_rubrica(puntuaciones, nota_final)
        anexos = self.generar_seccion_anexos(resultados_md)
        
        documento_final = f"""# Evaluación Final del Proyecto

**Fecha de evaluación**: {datetime.now().strftime("%Y-%m-%d %H:%M")}  
**Archivo evaluado**: {self.archivo_evaluado}  
**Modelo utilizado**: Claude 3 Sonnet  

## Tabla de Evaluación - Rúbrica

{tabla_rubrica}

## Síntesis de la Evaluación

{informe_sintesis}

---

{anexos}
"""
        
        self.logger.info(f"Documento final generado con nota: {nota_final}/10")
        return documento_final
    
    def generar_resumen_ejecutivo(self, puntuaciones: Dict[str, float]) -> str:
        """Genera un resumen ejecutivo de la evaluación"""
        nota_final = self.calcular_nota_final(puntuaciones)
        
        # Determinar el nivel de desempeño
        if nota_final >= 9.0:
            nivel = "Excelente"
            descripcion = "El proyecto cumple excepcionalmente con todos los criterios evaluados."
        elif nota_final >= 7.0:
            nivel = "Bueno"
            descripcion = "El proyecto cumple satisfactoriamente con la mayoría de criterios."
        elif nota_final >= 5.0:
            nivel = "Aceptable"
            descripcion = "El proyecto cumple básicamente con los criterios mínimos requeridos."
        else:
            nivel = "Insuficiente"
            descripcion = "El proyecto no cumple con los criterios mínimos establecidos."
        
        # Identificar fortalezas y debilidades
        criterios_ordenados = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
        mejor_criterio = criterios_ordenados[0]
        peor_criterio = criterios_ordenados[-1]
        
        nombres_criterios = {
            'objetivos': 'Objetivos',
            'requisitos_info': 'Requisitos de Información',
            'requisitos_nf': 'Requisitos No Funcionales',
            'casos_uso': 'Casos de Uso',
            'matrices': 'Matrices de Trazabilidad'
        }
        
        resumen = f"""## Resumen Ejecutivo

**Nota Final**: {nota_final}/10 - **{nivel}**

{descripcion}

### Análisis por Criterios:
- **Fortaleza Principal**: {nombres_criterios.get(mejor_criterio[0], mejor_criterio[0])} ({mejor_criterio[1]:.1f}/10)
- **Área de Mejora**: {nombres_criterios.get(peor_criterio[0], peor_criterio[0])} ({peor_criterio[1]:.1f}/10)

### Distribución de Puntuaciones:
"""
        
        for criterio, puntuacion in criterios_ordenados:
            nombre = nombres_criterios.get(criterio, criterio)
            resumen += f"- {nombre}: {puntuacion:.1f}/10\n"
        
        return resumen
    
    def generar_recomendaciones(self, puntuaciones: Dict[str, float]) -> str:
        """Genera recomendaciones basadas en las puntuaciones"""
        recomendaciones = ["## Recomendaciones\n"]
        
        nombres_criterios = {
            'objetivos': 'Objetivos',
            'requisitos_info': 'Requisitos de Información', 
            'requisitos_nf': 'Requisitos No Funcionales',
            'casos_uso': 'Casos de Uso',
            'matrices': 'Matrices de Trazabilidad'
        }
        
        sugerencias = {
            'objetivos': "Mejorar la claridad y especificidad de los objetivos del proyecto.",
            'requisitos_info': "Ampliar y detallar los requisitos de información del sistema.",
            'requisitos_nf': "Incluir más requisitos no funcionales específicos y medibles.",
            'casos_uso': "Desarrollar casos de uso más completos y detallados.",
            'matrices': "Crear matrices de trazabilidad más exhaustivas y coherentes."
        }
        
        # Generar recomendaciones para criterios con puntuación baja
        criterios_bajos = [(k, v) for k, v in puntuaciones.items() if v < 7.0]
        
        if criterios_bajos:
            recomendaciones.append("### Áreas de Mejora Prioritarias:\n")
            for criterio, puntuacion in sorted(criterios_bajos, key=lambda x: x[1]):
                nombre = nombres_criterios.get(criterio, criterio)
                sugerencia = sugerencias.get(criterio, f"Mejorar {nombre.lower()}.")
                recomendaciones.append(f"- **{nombre}** ({puntuacion:.1f}/10): {sugerencia}")
        else:
            recomendaciones.append("### Felicitaciones\n\nTodos los criterios han obtenido puntuaciones satisfactorias.\n")
        
        # Recomendaciones generales
        nota_final = self.calcular_nota_final(puntuaciones)
        if nota_final < 5.0:
            recomendaciones.append("\n### Recomendación General:\n")
            recomendaciones.append("Se sugiere una revisión integral del documento antes de la entrega final.")
        elif nota_final < 7.0:
            recomendaciones.append("\n### Recomendación General:\n")
            recomendaciones.append("El proyecto está en buen camino, enfocarse en las áreas identificadas para mejorarlo.")
        
        return "\n".join(recomendaciones) 