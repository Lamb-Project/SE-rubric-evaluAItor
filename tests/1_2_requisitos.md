<think>
Okay, I need to identify all the information requirements (IRQ) and non-functional requirements (NFR) from the provided document. Let me start by going through each section carefully.

First, the user mentioned a table with some requirements like IRQ-1 to IRQ-10 and NFR-1 to NFR-5. The task is to extract all fields for each, including data specifics, time of life, occurrences, importance, urgency, state, and stability. 

Looking at the "Glosario de términos" and "Propuesta de arquitectura" sections, there's a lot of information about the system's structure, components, and data flow. For example, the three-tier architecture with frontend, backend, and database layers. The C4 model also shows containers and components, which might relate to non-functional requirements like scalability and security.

In the "Requisitos del Sistema" section, the user wants each IRQ and NFR listed with specific details. For example, under information requirements, each entry should have a description, associated objectives, specific data, time of life, occurrences, importance, urgency, state, and stability. 

I need to make sure not to miss any fields. Let me check each part again. The data específicos would be the data elements needed, like user information, game data, statistics, etc. Time of life is how long the data is relevant. Occurrences could be how often the data is accessed or processed. Importance and urgency are straightforward. State could be whether it's implemented or not. Stability might refer to how likely the requirement is to change.

For non-functional requirements, similar fields apply but without data specifics. They might relate to performance, security, scalability, reliability, etc. The C4 model mentions HTTPS, which relates to security. The use of caching (Redis) and database optimization could relate to performance and scalability.

I need to go through each section again to ensure all requirements are captured. For example, the "Propuesta de arquitectura" mentions REST APIs, which might relate to NFRs about interoperability. The use of a three-tier architecture suggests separation of concerns, which is a non-functional requirement.

The "Glosario de términos" includes terms like "Retroalimentación," "Analíticas," "Gamificación," which might correspond to specific functional requirements. For example, real-time feedback for students would be an information requirement, while analytics for performance tracking might be another.

I also need to check the "Glosario de términos" for any terms that might indicate requirements. For example, "Retroalimentación" (feedback) could be an IRQ about providing immediate responses after game answers. "Analíticas" (analytics) might relate to processing student performance data.

In the "Propuesta de arquitectura," the backend components like the "Controlador de Autenticación" and "Servicio de Análisis IA" would correspond to various information requirements for user authentication and data analysis.

I need to make sure each requirement is uniquely identified with the correct numbering as per the original document. For example, if there are 10 IRQs and 5 NFRs, they should be listed accordingly.

Also, the user wants the data in a specific Markdown format, so I need to structure each section properly without any explanations. Just the facts as per the document.

Let me start compiling the list now, ensuring each requirement is correctly categorized and all required fields are filled out.
</think>

# Requisitos del Sistema

## Requisitos de Información

### IRQ-1: Gestión de Usuarios
- **Descripción:** Registro, autenticación y administración de datos personales de profesores y alumnos.
- **Objetivos asociados:** OBJ-1, OBJ-2
- **Datos específicos:** nombre, correo electrónico, contraseña, rol (profesor/alumno), fecha de registro
- **Tiempo de vida:**
  - Medio: 30 días
  - Máximo: 1 año
- **Ocurrencias:**
  - Medio: 500/día
  - Máximo: 2000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### IRQ-2: Gestión de Juegos Educativos
- **Descripción:** Creación, edición y almacenamiento de juegos con preguntas y respuestas.
- **Objetivos asociados:** OBJ-3, OBJ-4
- **Datos específicos:** título, descripción, preguntas, respuestas, tiempo de juego, nivel de dificultad
- **Tiempo de vida:**
  - Medio: 6 meses
  - Máximo: 2 años
- **Ocurrencias:**
  - Medio: 100/día
  - Máximo: 500/día
- **Importancia:** Alta
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Media

### IRQ-3: Procesamiento de Respuestas
- **Descripción:** Captura y evaluación automática de respuestas de los alumnos.
- **Objetivos asociados:** OBJ-4, OBJ-5
- **Datos específicos:** juego_id, alumno_id, pregunta_id, respuesta, tiempo_de_respuesta, calificación
- **Tiempo de vida:**
  - Medio: 10 minutos
  - Máximo: 1 hora
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 5000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### IRQ-4: Generación de Estadísticas
- **Descripción:** Cálculo de métricas de rendimiento individual y grupal.
- **Objetivos asociados:** OBJ-5, OBJ-6
- **Datos específicos:** alumno_id, juego_id, puntuación, tiempo_medio, aciertos, errores
- **Tiempo de vida:**
  - Medio: 30 días
  - Máximo: 3 años
- **Ocurrencias:**
  - Medio: 200/día
  - Máximo: 1000/día
- **Importancia:** Alta
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Media

### IRQ-5: Retroalimentación Inmediata
- **Descripción:** Proporcionar explicaciones y correcciones en tiempo real.
- **Objetivos asociados:** OBJ-4, OBJ-5
- **Datos específicos:** pregunta_id, respuesta_correcta, explicación, alumno_id
- **Tiempo de vida:**
  - Medio: 5 segundos
  - Máximo: 30 segundos
- **Ocurrencias:**
  - Medio: 1500/día
  - Máximo: 7000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### IRQ-6: Integración con IA
- **Descripción:** Análisis de patrones de desempeño con algoritmos de machine learning.
- **Objetivos asociados:** OBJ-6, OBJ-7
- **Datos específicos:** alumno_id, historial_respuestas, patrones_de_error, recomendaciones
- **Tiempo de vida:**
  - Medio: 1 hora
  - Máximo: 24 horas
- **Ocurrencias:**
  - Medio: 50/día
  - Máximo: 200/día
- **Importancia:** Media
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Baja

### IRQ-7: Generación de Reportes
- **Descripción:** Creación de informes personalizados para profesores.
- **Objetivos asociados:** OBJ-6, OBJ-7
- **Datos específicos:** alumno_id, juego_id, resumen_estadístico, recomendaciones, gráficos
- **Tiempo de vida:**
  - Medio: 7 días
  - Máximo: 1 mes
- **Ocurrencias:**
  - Medio: 30/día
  - Máximo: 150/día
- **Importancia:** Media
- **Urgencia:** Baja
- **Estado:** Implementado
- **Estabilidad:** Media

### IRQ-8: Gestión de Archivos Multimedia
- **Descripción:** Almacenamiento y recuperación de imágenes, videos y sonidos.
- **Objetivos asociados:** OBJ-3, OBJ-4
- **Datos específicos:** archivo_id, tipo_de_archivo, ruta_de_acceso, tamaño, juego_id
- **Tiempo de vida:**
  - Medio: 6 meses
  - Máximo: 5 años
- **Ocurrencias:**
  - Medio: 200/día
  - Máximo: 1000/día
- **Importancia:** Media
- **Urgencia:** Baja
- **Estado:** Implementado
- **Estabilidad:** Alta

### IRQ-9: Sistema de Notificaciones
- **Descripción:** Envío de alertas a profesores y alumnos sobre actividades recientes.
- **Objetivos asociados:** OBJ-2, OBJ-5
- **Datos específicos:** usuario_id, tipo_de_notificación, mensaje, fecha_envío
- **Tiempo de vida:**
  - Medio: 10 minutos
  - Máximo: 1 hora
- **Ocurrencias:**
  - Medio: 500/día
  - Máximo: 2000/día
- **Importancia:** Media
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Media

### IRQ-10: Gestión de Sesiones
- **Descripción:** Control de inicio y cierre de sesiones de usuarios.
- **Objetivos asociados:** OBJ-1, OBJ-2
- **Datos específicos:** usuario_id, fecha_inicio, fecha_fin, duración, dispositivo
- **Tiempo de vida:**
  - Medio: 1 hora
  - Máximo: 8 horas
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 5000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

## Requisitos No Funcionales

### NFR-1: Seguridad de Datos
- **Descripción:** Protección de información sensible mediante encriptación y autenticación.
- **Objetivos asociados:** OBJ-1, OBJ-2
- **Tiempo de vida:**
  - Medio: Indefinido
  - Máximo: Indefinido
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 5000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### NFR-2: Escalabilidad
- **Descripción:** Capacidad del sistema para manejar aumento de usuarios y datos.
- **Objetivos asociados:** OBJ-3, OBJ-4
- **Tiempo de vida:**
  - Medio: 1 año
  - Máximo: 5 años
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 10000/día
- **Importancia:** Alta
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Media

### NFR-3: Disponibilidad
- **Descripción:** Tiempo de actividad del sistema con cero tiempos de inactividad.
- **Objetivos asociados:** OBJ-1, OBJ-2
- **Tiempo de vida:**
  - Medio: 99.9%
  - Máximo: 99.99%
- **Ocurrencias:**
  - Medio: 24/7
  - Máximo: 24/7
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### NFR-4: Rendimiento
- **Descripción:** Velocidad de respuesta para operaciones críticas.
- **Objetivos asociados:** OBJ-3, OBJ-4
- **Tiempo de vida:**
  - Medio: 1 segundo
  - Máximo: 3 segundos
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 5000/día
- **Importancia:** Alta
- **Urgencia:** Alta
- **Estado:** Implementado
- **Estabilidad:** Alta

### NFR-5: Interoperabilidad
- **Descripción:** Compatibilidad con dispositivos y sistemas operativos.
- **Objetivos asociados:** OBJ-1, OBJ-2
- **Tiempo de vida:**
  - Medio: 1 año
  - Máximo: 3 años
- **Ocurrencias:**
  - Medio: 1000/día
  - Máximo: 5000/día
- **Importancia:** Media
- **Urgencia:** Media
- **Estado:** Implementado
- **Estabilidad:** Media