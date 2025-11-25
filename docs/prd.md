# Project Requirements Document (PRD)
## Sistema de Evaluación Automatizada de Proyectos Ingenieria del Software basado en rúbricas

**Versión:** 1.0  
**Fecha:** 2025/6  
**Proyecto:** Sistema de Evaluación Automatizada con LLM  

---

## 1. Resumen Ejecutivo

### 1.1 Descripción del Proyecto
Sistema automatizado para evaluar documentos de proyectos académicos de ingenieria del software utilizando LLMs (Claude 4 Sonnet de Anthropic). El sistema analiza documentos en formato texto y genera evaluaciones estructuradas basadas en una rúbrica predefinida.

### 1.2 Objetivo Principal
Automatizar el proceso de evaluación de proyectos académicos proporcionando análisis consistentes, objetivos y detallados que cumplan con estándares académicos específicos.

### 1.3 Stakeholders
- **Usuarios Primarios:** Profesores y evaluadores académicos
- **Usuarios Secundarios:** Estudiantes (para retroalimentación)

---

## 2. Funcionalidades Principales

### 2.1 Core Features

#### 2.1.1 Procesamiento de Documentos
- **Entrada:** Archivos de texto con documentos de proyectos
- **Formatos Soportados:** Texto plano (UTF-8)
- **Capacidad:** Documentos de hasta 64K tokens por análisis

#### 2.1.2 Sistema de Evaluación en 4 Fases
1. **Fase 1 - Extracción de Información:**
   - Extracción de objetivos del proyecto
   - Extracción de requisitos (funcionales y no funcionales)
   - Extracción de casos de uso

2. **Fase 2 - Análisis de Coherencia:**
   - Análisis de trazabilidad entre elementos
   - Análisis de completitud de requisitos

3. **Fase 3 - Evaluación por Criterios:**
   - Objetivos (20% del peso total)
   - Requisitos de Información (15%)
   - Requisitos No Funcionales (10%)
   - Casos de Uso (35%)
   - Matrices de Trazabilidad (20%)

4. **Fase 4 - Síntesis y Calificación:**
   - Generación de informe final
   - Cálculo de nota ponderada (0-10)
   - Documento de evaluación completo

#### 2.1.3 Sistema de Prompts Modulares
- Prompts organizados en archivos markdown separados
- Estructura modular para facilitar mantenimiento
- Prompts específicos para cada fase y criterio

#### 2.1.4 Generación de Reportes
- Reportes en formato Markdown
- Tabla de evaluación con rúbrica detallada
- Anexos con evaluaciones detalladas por criterio
- Logging completo del proceso

---

## 3. Requisitos Técnicos

### 3.1 Requisitos Funcionales

#### RF-001: Lectura de Documentos
- El sistema DEBE leer archivos de texto en codificación UTF-8
- El sistema DEBE manejar errores de lectura de archivos
- El sistema DEBE validar la existencia del archivo antes del procesamiento

#### RF-002: Integración con Claude 3 Sonnet
- El sistema DEBE utilizar la API de Anthropic
- El sistema DEBE manejar autenticación mediante API key
- El sistema DEBE gestionar límites de tokens (máximo 4096)

#### RF-003: Procesamiento en Fases
- El sistema DEBE ejecutar las 4 fases en orden secuencial
- Cada fase DEBE completarse antes de la siguiente
- El sistema DEBE mantener estado entre fases

#### RF-004: Sistema de Prompts
- El sistema DEBE leer prompts desde directorio configurable
- Los prompts DEBEN estar en formato markdown
- El sistema DEBE aplicar reemplazos de variables en prompts

#### RF-005: Cálculo de Puntuaciones
- El sistema DEBE extraer puntuaciones numéricas de respuestas
- El sistema DEBE aplicar pesos correctos: Objetivos(20%), Req.Info(15%), Req.NF(10%), Casos Uso(35%), Matrices(20%)
- El sistema DEBE calcular nota final ponderada

#### RF-006: Generación de Reportes
- El sistema DEBE generar archivos markdown de salida
- El sistema DEBE incluir tabla de rúbrica con puntuaciones
- El sistema DEBE generar documento final consolidado

### 3.2 Requisitos No Funcionales

#### RNF-001: Performance
- Tiempo de procesamiento máximo: 10 minutos por documento
- El sistema DEBE procesar documentos de hasta 50KB

#### RNF-002: Reliability
- El sistema DEBE manejar errores de API de forma elegante
- El sistema DEBE proporcionar logging detallado
- El sistema DEBE validar respuestas de Claude antes de procesarlas

#### RNF-003: Usability
- Interfaz de línea de comandos intuitiva
- Mensajes de error claros y descriptivos
- Documentación de uso disponible

#### RNF-004: Maintainability
- Código modular y bien documentado
- Separación clara de responsabilidades
- Configuración externalizada

#### RNF-005: Security
- API key DEBE ser configurable por variable de entorno
- No DEBE almacenar credenciales en código
- Logging NO DEBE incluir información sensible

---

## 4. Arquitectura del Sistema

### 4.1 Componentes Principales

#### 4.1.1 EvaluadorProyecto (Clase Principal)
- Orquesta todo el proceso de evaluación
- Gestiona configuración y estado
- Maneja comunicación con Claude

#### 4.1.2 EvaluacionConfig (Configuración)  
- Almacena parámetros de configuración
- Rutas de archivos y directorios
- Credenciales de API

#### 4.1.3 Sistema de Logging
- Logging a archivo y consola
- Niveles de log configurables
- Trazabilidad completa del proceso

### 4.2 Flujo de Datos
```
Documento Input → Fase 1 Extracción → Fase 2 Coherencia → Fase 3 Evaluación → Fase 4 Síntesis → Reporte Final
```

### 4.3 Dependencias Externas
- **anthropic:** Cliente para API de Claude
- **pathlib:** Manejo de rutas de archivos
- **logging:** Sistema de logging
- **argparse:** Parsing de argumentos CLI
- **dataclasses:** Estructuras de datos
- **re:** Expresiones regulares para parsing

---

## 5. Interfaces

### 5.1 Interfaz de Línea de Comandos
```bash
python evaluador.py <archivo> <directorio_salida> [--prompts <dir_prompts>] [--api-key <key>]
```

**Parámetros:**
- `archivo`: Ruta al documento a evaluar (requerido)
- `directorio_salida`: Directorio para guardar resultados (requerido)
- `--prompts`: Directorio con archivos de prompts (opcional, default: ./prompts)
- `--api-key`: API Key de Anthropic (opcional, usa variable de entorno)

### 5.2 Variables de Entorno
- `ANTHROPIC_API_KEY`: API Key para acceso a Claude

### 5.3 Estructura de Archivos de Salida
```
<directorio_salida>/
├── evaluacion.log
├── 1_1_objetivos.md
├── 1_2_requisitos.md
├── 1_3_casos_uso.md
├── 2_1_trazabilidad.md
├── 2_2_completitud.md
├── 3_1_eval_objetivos.md
├── 3_2_eval_requisitos_info.md
├── 3_3_eval_requisitos_nf.md
├── 3_4_eval_casos_uso.md
├── 3_5_eval_matrices.md
└── EVALUACION_FINAL.md
```

---

## 6. Consideraciones de Implementación

### 6.1 Manejo de Errores
- Validación de archivos de entrada
- Manejo de errores de API
- Recuperación elegante ante fallos

### 6.2 Configuración
- Parámetros configurables externamente
- Valores por defecto sensatos
- Validación de configuración

### 6.3 Extensibilidad
- Sistema de prompts modular
- Criterios de evaluación configurables
- Pesos de evaluación ajustables

---

## 7. Criterios de Aceptación

### 7.1 Funcionalidad
- [ ] El sistema procesa documentos de texto correctamente
- [ ] Genera evaluaciones para todos los criterios definidos
- [ ] Calcula nota final ponderada correctamente
- [ ] Genera reportes en formato markdown

### 7.2 Calidad
- [ ] Manejo robusto de errores
- [ ] Logging completo y útil
- [ ] Código bien documentado y mantenible

### 7.3 Usabilidad
- [ ] Interfaz CLI intuitiva
- [ ] Mensajes de error claros
- [ ] Documentación de uso disponible

---

## 8. Riesgos y Limitaciones

### 8.1 Riesgos Técnicos
- **Dependencia de API externa:** Fallos en la API de Anthropic pueden interrumpir el servicio
- **Límites de tokens:** Documentos muy largos pueden requerir fragmentación
- **Calidad de prompts:** La efectividad depende de la calidad de los prompts

### 8.2 Limitaciones
- Solo soporta archivos de texto plano
- Dependiente de la disponibilidad de la API de Claude
- Evaluaciones en español únicamente

### 8.3 Mitigaciones
- Implementar retry logic para llamadas a API
- Validar longitud de documentos antes del procesamiento  
- Versionar y testear prompts regularmente
