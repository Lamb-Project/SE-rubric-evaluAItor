# Plan de Mejora del Evaluador - Evaluación con Claude Code y AAC

**Proyecto:** Implementar un sistema de evaluación automática de trabajos estudiantiles usando rúbricas.  
**Enfoque:** Iterar con Claude Code → Validar → Migrar a AAC  
**Fecha:** April 2026

---

## 📋 TABLA DE CONTENIDOS

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Análisis de Estado Actual](#análisis-de-estado-actual)
3. [Visión del Nuevo Sistema](#visión-del-nuevo-sistema)
4. [Arquitectura Propuesta](#arquitectura-propuesta)
5. [Plan de Fases](#plan-de-fases)
6. [Especificaciones Detalladas](#especificaciones-detalladas)
7. [Criterios de Éxito](#criterios-de-éxito)
8. [Roadmap y Timeline](#roadmap-y-timeline)

---

## 1. Resumen Ejecutivo

### Objetivo Principal
Extender LAMB con un **sistema de evaluación automática de trabajos estudiantiles** que use rúbricas predefinidas para generar puntuaciones y retroalimentación mediante LLM. El desarrollo será **iterativo con Claude Code como agente de prueba**, validando el proceso completo antes de migración a AAC.

### Lo que Hace Tu Profesor
Tu profesor sugiere:
1. ✅ **Usar Claude Code como agente** — Yo ejecuto el proceso completo del evaluador
2. ✅ **Crear `evaluator-cli`** — Herramienta CLI para automatizar la evaluación
3. ✅ **Aplicar mismos juegos de prueba** — Validar con datos reales que ya tienen
4. ✅ **Crear prompts y skills** — Definir cómo evaluar, qué mejorar
5. ✅ **Proponer mejoras** — Yo mismo valido y sugiero optimizaciones
6. ✅ **Portarlo a AAC** — Una vez validado, tu sistema AAC lo ejecuta

### Beneficios
- **Validación sin riesgo** — Pruebas exhaustivas antes de producción
- **Automatización de evaluación** — Reducir carga manual de docentes
- **Consistencia** — Rúbricas aplicadas uniformemente
- **Escalabilidad** — Evaluar muchos trabajos en paralelo
- **Trazabilidad** — Registro completo de decisiones de evaluación

---

## 2. Análisis de Estado Actual

### 2.1 ¿Qué ya existe?

✅ **Evaluaitor (Gestor de Rúbricas)**
- Ubicación: `/backend/lamb/evaluaitor/`
- Estado: Phase 1 (MVP) completo
- Características:
  - Crear/leer/actualizar/eliminar rúbricas
  - Exportar a JSON y Markdown
  - Interfaz web para editar rúbricas
  - Asistente de IA para generar rúbricas
  - Rúbricas privadas/públicas por organización

✅ **Estructura de Rúbrica**
```json
{
  "rubricId": "uuid",
  "title": "Nombre de la rúbrica",
  "criteria": [
    {
      "id": "criterion-1",
      "name": "Criterio 1",
      "weight": 30,
      "levels": [
        {
          "id": "level-1-1",
          "score": 4,
          "label": "Exemplar",
          "description": "..."
        }
      ]
    }
  ],
  "scoringType": "points",
  "maxScore": 10
}
```

### 2.2 ¿Qué NO existe?

❌ **Sistema de Evaluación de Trabajos**
- No hay proceso para evaluar trabajos estudiantiles
- No hay formato estándar para "trabajos" (submissions)
- No hay pipeline de evaluación LLM → puntuación
- No hay `evaluator-cli`
- No hay juegos de prueba integrados

❌ **Integración con AAC**
- AAC no puede ejecutar evaluaciones aún
- No hay API entre LAMB y AAC para este proceso
- No hay shared prompts/skills

### 2.3 Dependencias Existentes

- **Backend FastAPI**: `/backend` (puerto 9099) ✅
- **LLM providers**: OpenAI, Anthropic, Ollama (ya configurados) ✅
- **Base de datos LAMB**: SQLite WAL (`lamb_v4.db`) ✅
- **Frontend Svelte**: `/frontend/svelte-app` ✅

---

## 3. Visión del Nuevo Sistema

### 3.1 Flujo Completo Propuesto

```
┌─────────────────────────────────────────────────────────────────┐
│                   Proceso de Evaluación                         │
└─────────────────────────────────────────────────────────────────┘

1. ENTRADA
   ├─ Rúbrica (JSON)
   ├─ Trabajo Estudiantil (texto/documento)
   ├─ Criterios de Evaluación
   └─ Contexto (curso, estudiante, etc.)

2. PREPARACIÓN
   ├─ Validar rúbrica
   ├─ Validar formato de trabajo
   ├─ Generar contexto de evaluación
   └─ Seleccionar LLM

3. EVALUACIÓN (LLM)
   ├─ Enviar prompt estructurado al L

ump-zvft-qrf