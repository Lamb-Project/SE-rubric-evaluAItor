# Documento de Prueba

## Objetivos
- Probar el sistema de evaluación con múltiples proveedores
- Verificar que el sistema funciona correctamente

## Requisitos

### Requisitos de Información
- REQ001: El sistema debe permitir evaluar documentos
- REQ002: El sistema debe generar informes en formato Markdown

### Requisitos No Funcionales
- RNF001: El sistema debe ser compatible con múltiples proveedores de LLM
- RNF002: El sistema debe ser configurable mediante línea de comandos

## Casos de Uso

### CU001: Evaluar Documento
**Actor:** Usuario evaluador
**Descripción:** El usuario utiliza el sistema para evaluar un documento
**Flujo Principal:**
1. El usuario ejecuta el comando de evaluación
2. El sistema procesa el documento
3. El sistema genera un informe de evaluación

### CU002: Seleccionar Proveedor
**Actor:** Usuario evaluador
**Descripción:** El usuario selecciona el proveedor de LLM a utilizar
**Flujo Principal:**
1. El usuario especifica el proveedor mediante parámetros
2. El sistema utiliza el proveedor seleccionado

## Matrices de Trazabilidad

### Objetivos vs Requisitos
- Objetivo 1 -> REQ001, REQ002
- Objetivo 2 -> RNF001, RNF002

### Requisitos vs Casos de Uso
- REQ001 -> CU001
- RNF001 -> CU002 