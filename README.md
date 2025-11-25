# Sistema de Evaluación Automatizada de Proyectos

Un sistema automatizado para evaluar proyectos académicos de Ingeniería del Software utilizando modelos de lenguaje (LLMs). El sistema analiza documentos de proyectos y genera evaluaciones estructuradas basadas en una rúbrica predefinida.

## 🚀 Características Principales

- **Evaluación Automatizada**: Procesamiento completo de documentos con análisis detallado
- **Múltiples Proveedores**: Soporte para Anthropic (Claude), OpenAI y Ollama
- **Análisis en 4 Fases**: Extracción → Coherencia → Evaluación → Síntesis
- **Rúbrica Completa**: 5 criterios con pesos específicos (Objetivos 20%, Requisitos Info 15%, Req. No Func. 10%, Casos Uso 35%, Matrices 20%)
- **Salida Markdown**: Reportes estructurados y legibles
- **Logging Detallado**: Seguimiento completo del proceso de evaluación

## 📋 Requisitos del Sistema

- **Python**: 3.11 o superior
- **Dependencias**: Ver `requirements.txt`
- **API Keys**: Dependiendo del proveedor seleccionado

## 🛠️ Instalación

1. **Clona o descarga el proyecto**
   ```bash
   cd prototipo-2
   ```

2. **Instala las dependencias**
   ```bash
   # Instalar dependencias básicas (Anthropic + utilidades)
   pip install -r requirements.txt

   # O instalar todo (incluyendo OpenAI) de una vez
   pip install -r requirements_all.txt
   ```

3. **Para soporte OpenAI (opcional, si no usaste requirements_all.txt)**
   ```bash
   pip install openai>=1.0.0
   ```

## 📖 Uso Básico

### Sintaxis General
```bash
python evaluador.py <archivo_documento> <directorio_salida> [opciones]
```

### Parámetros Obligatorios
- `archivo_documento`: Ruta al documento del proyecto a evaluar (formato texto/Markdown)
- `directorio_salida`: Directorio donde se guardarán los resultados

### Opciones Principales
- `--prompts <directorio>`: Directorio con archivos de prompts (por defecto: `./prompts`)
- `--api-key <key>`: API key (o usar variables de entorno)
- `--ollama <modelo>`: Usar Ollama con el modelo especificado
- `--openai <modelo>`: Usar OpenAI con el modelo especificado
- `--debug`: Modo debug con información detallada

## 🌐 Proveedores Soportados

### Anthropic (Claude) - Por Defecto
```bash
# Usando variable de entorno
export ANTHROPIC_API_KEY=sk-ant-...
python evaluador.py documento.md ./resultados

# Usando parámetro
python evaluador.py documento.md ./resultados --api-key sk-ant-...
```

### Ollama (Local)
```bash
# Instalar y ejecutar Ollama primero
ollama pull mistral:latest
ollama serve

# Usar en el evaluador
python evaluador.py documento.md ./resultados --ollama mistral:latest
```

### OpenAI (GPT)
```bash
# Instalar dependencia adicional
pip install openai

# Usar GPT-4
export OPENAI_API_KEY=sk-...
python evaluador.py documento.md ./resultados --openai gpt-4-turbo-preview

# Usar GPT-3.5 (más económico)
python evaluador.py documento.md ./resultados --openai gpt-3.5-turbo
```

## 📊 Proceso de Evaluación

El sistema ejecuta 4 fases secuenciales:

### Fase 1: Extracción de Información
- **1.1**: Extracción de objetivos del proyecto
- **1.2**: Extracción de requisitos (funcionales y no funcionales)
- **1.3**: Extracción de casos de uso

### Fase 2: Análisis de Coherencia
- **2.1**: Análisis de trazabilidad entre elementos
- **2.2**: Análisis de completitud de requisitos

### Fase 3: Evaluación por Criterios
- **3.1**: Evaluación de objetivos (20% del peso total)
- **3.2**: Evaluación de requisitos de información (15%)
- **3.3**: Evaluación de requisitos no funcionales (10%)
- **3.4**: Evaluación de casos de uso (35%)
- **3.5**: Evaluación de matrices de trazabilidad (20%)

### Fase 4: Síntesis y Calificación Final
- Generación del informe consolidado
- Cálculo de nota ponderada (0-10)
- Documento final con rúbrica completa

!(docs/Evaluaitor.png)[]

## 📁 Estructura de Archivos Generados

```
<directorio_salida>/
├── evaluacion.log              # Log detallado del proceso
├── 1_1_objetivos.md           # Objetivos extraídos
├── 1_2_requisitos.md          # Requisitos extraídos
├── 1_3_casos_uso.md           # Casos de uso extraídos
├── 2_1_trazabilidad.md        # Análisis de trazabilidad
├── 2_2_completitud.md         # Análisis de completitud
├── 3_1_eval_objetivos.md      # Evaluación de objetivos
├── 3_2_eval_requisitos_info.md # Evaluación req. info
├── 3_3_eval_requisitos_nf.md  # Evaluación req. no func.
├── 3_4_eval_casos_uso.md      # Evaluación casos de uso
├── 3_5_eval_matrices.md       # Evaluación matrices
└── EVALUACION_FINAL.md        # Informe consolidado final
```

## 💰 Costos Estimados

| Proveedor | Modelo | Costo por 1k tokens | Notas |
|-----------|--------|-------------------|-------|
| Anthropic | Claude 3 Sonnet | $0.003 entrada / $0.015 salida | Alta calidad (por defecto) |
| OpenAI | GPT-4 Turbo | $0.01 entrada / $0.03 salida | Muy alta calidad |
| OpenAI | GPT-3.5 Turbo | $0.0005 entrada / $0.0015 salida | Buena calidad, económico |
| Ollama | Cualquier modelo | Gratuito | Calidad variable, ejecución local |

**Costo estimado por evaluación completa**: ~$0.50-2.00 USD (dependiendo del proveedor y tamaño del documento)

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Anthropic
export ANTHROPIC_API_KEY=sk-ant-...

# OpenAI
export OPENAI_API_KEY=sk-...

# Ollama (opcional, por defecto localhost:11434)
export OLLAMA_BASE_URL=http://localhost:11434
```

### Personalización de Prompts
Los prompts se almacenan en el directorio `./prompts/` y pueden ser modificados para:
- Ajustar criterios de evaluación
- Cambiar el idioma de evaluación
- Modificar el formato de salida

### Configuración del Sistema
- **Límite de tokens**: Máximo 4096 tokens por llamada API
- **Tiempo estimado**: 2-5 minutos por evaluación completa
- **Tamaño máximo**: Documentos hasta 10MB (recomendado < 50KB)

## 🧪 Testing y Validación

### Probar Proveedores
```bash
python test_providers.py
```

### Documento de Prueba
Se incluye `test_doc.md` para pruebas rápidas del sistema.

## 📋 Ejemplos de Uso

### Evaluación Básica con Claude
```bash
python evaluador.py proyecto_final.md ./evaluacion_proyecto
```

### Evaluación con Modelo Local (Ollama)
```bash
python evaluador.py proyecto_final.md ./evaluacion_proyecto --ollama mistral:latest
```

### Evaluación con OpenAI GPT-4
```bash
python evaluador.py proyecto_final.md ./evaluacion_proyecto --openai gpt-4-turbo-preview
```

### Evaluación con Prompts Personalizados
```bash
python evaluador.py proyecto_final.md ./evaluacion_proyecto --prompts ./mis_prompts
```

### Modo Debug
```bash
python evaluador.py proyecto_final.md ./evaluacion_proyecto --debug
```

## 🌊 Versión Streaming (Recomendada)

La versión streaming (`evaluador_streaming.py`) ofrece mejoras significativas sobre la versión estándar:

### 🚀 Características de la Versión Streaming

- **Streaming activado** para Anthropic Claude, Ollama y OpenAI
- **Timeouts extendidos**: 15 minutos (vs 5 minutos en la versión estándar)
- **Reintentos aumentados**: Hasta 5 reintentos (vs 3 en la versión estándar)
- **Mejor feedback** durante la evaluación con actualizaciones en tiempo real
- **Menor uso de memoria** gracias al procesamiento por fragmentos
- **Fallback automático** si el streaming falla

### 🛠️ Uso de la Versión Streaming

#### Con Anthropic Claude (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados
# O con API key explícita
python evaluador_streaming.py documento.md ./resultados --api-key sk-ant-...
```

#### Con Ollama (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados --ollama llama2
python evaluador_streaming.py documento.md ./resultados --ollama mistral:latest
```

#### Con OpenAI (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados --openai gpt-4-turbo-preview
python evaluador_streaming.py documento.md ./resultados --openai gpt-3.5-turbo
```

#### Procesamiento por Lotes (Directorio)
```bash
python evaluador_streaming.py --input-dir ./documentos ./resultados
```

#### Opciones Avanzadas
```bash
# Modo debug con información detallada
python evaluador_streaming.py documento.md ./resultados --debug

# Con prompts personalizados
python evaluador_streaming.py documento.md ./resultados --prompts ./mis_prompts
```

### 📊 Comparación de Versiones

| Característica | Versión Estándar | Versión Streaming |
|----------------|------------------|-------------------|
| Streaming Ollama | ❌ Desactivado | ✅ **Activado** |
| Streaming Anthropic | ❌ No disponible | ✅ **Activado** |
| Streaming OpenAI | ❌ No disponible | ✅ **Activado** |
| Timeout máximo | 5 minutos | **15 minutos** |
| Reintentos | 3 | **5** |
| Uso de memoria | Alto | **Optimizado** |
| Feedback | Básico | **En tiempo real** |

### 💡 Recomendación

**Use la versión streaming para:**
- Documentos largos que requieren más tiempo de procesamiento
- Mejor experiencia de usuario con feedback en tiempo real
- Procesamiento más eficiente de memoria
- Mayor estabilidad con reintentos automáticos

## 🚨 Solución de Problemas

### Errores Comunes

**Archivo no encontrado**
```
❌ Error: El archivo 'documento.md' no existe
```
*Solución*: Verificar la ruta del archivo de entrada

**API Key no configurada**
```
❌ Error: No se puede conectar con la API
```
*Solución*: Configurar API key en variable de entorno o parámetro `--api-key`

**Ollama no ejecutándose**
```
❌ Error: No se puede conectar con Ollama
```
*Solución*: Ejecutar `ollama serve` y verificar que el modelo esté descargado

**Directorio de prompts faltante**
```
❌ Error: El directorio de prompts no existe
```
*Solución*: Verificar que existe el directorio `./prompts/` con todos los archivos requeridos

### Logs y Depuración
- Usar `--debug` para información detallada
- Revisar `evaluacion.log` en el directorio de salida
- Verificar conectividad de red para proveedores en la nube

## 📚 Documentación Adicional

- [PRD - Product Requirements Document](docs/prd.md)
- [Soporte Multi-Proveedor](README_PROVIDERS.md)
- [Arquitectura del Sistema](docs/) - Más documentación técnica

## 🤝 Contribución

Para contribuir al proyecto:
1. Revisar la documentación en `docs/`
2. Seguir la estructura modular del código
3. Añadir tests para nuevas funcionalidades
4. Actualizar documentación según cambios

## 📄 Licencia

Sistema de Evaluación Automatizada de Proyectos - Un sistema automatizado para evaluar proyectos académicos de Ingeniería del Software utilizando modelos de lenguaje (LLMs).

Copyright (C) 2025 Marc Alier, Francisco Garcia-Peñalvo, Alicia Garcia-Holgado, Andrea Vázquez Ingelmo, Maria José Casañ, Juanan Pereira

Este proyecto es parte de un trabajo académico para la evaluación automatizada de proyectos de Ingeniería del Software.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## © Copyright

**Autores:**
- Marc Alier
- Francisco Garcia-Peñalvo
- Alicia Garcia-Holgado
- Andrea Vázquez Ingelmo
- Maria José Casañ
- Juanan Pereira

**Universidades:**
- Universitat Politècnica de Catalunya (UPC)
- Universidad de Salamanca (USAL)
- Universitat Politècnica de València (UPV)

---

**Versión**: Prototipo 2.0
**Fecha**: Noviembre 2025
**Autor**: Sistema de Evaluación Automatizada con LLM
