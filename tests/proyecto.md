# Memoria Trabajo Final - Aplicación de Juego Educativo

**Versión: 1**  
**02/05/2024**

## Registro de cambios

### HITO 1 (SEGUNDA ENTREGA)

Primero, hemos fusionado los Objetivos 1 y 2 en uno solo y añadimos un quinto objetivo sobre el registro de usuarios.

En las tablas de requisitos de información, actualizamos los datos faltantes o incorrectos y eliminamos el requisito de historial de puntuaciones, agregando uno nuevo relacionado con el juego.

También actualizamos los requisitos no funcionales, añadiendo dos nuevos sobre ética y políticas de privacidad.

En los casos de uso, modificamos los diagramas, añadiendo abrir y cerrar sesión en el registro. En el caso de juego, permitimos al profesor crear y publicar juegos. En progreso, eliminamos casos de uso innecesarios y actualizamos las relaciones con los actores.

Corregimos las tablas de casos de uso, principalmente en los requisitos y objetivos, afectados por los cambios.

Finalmente, ajustamos las matrices finales, incluyendo casos de uso omitidos y actualizando con los nuevos objetivos y requisitos de información.

### HITO 2 (TERCERA ENTREGA)

Del hito 1 hemos vuelto a corregir el diagrama de casos de uso.

Hemos actualizado la memoria técnica, cuidando más el formato y añadiendo los contenidos que faltaba.

Hemos cambiado el diagrama de clases, añadiendo una nueva clase "Progreso". Además hemos cambiado la clase asociación "Estadísticas", a una clase normal para poder guardar los registros de una forma adecuada.

## Tabla de contenidos

1. [Descripción](#descripción)
   - 1.1. [Introducción](#introducción)
   - 1.2. [Objetivos](#objetivos)
   - 1.3. [Técnicas y herramientas](#técnicas-y-herramientas)
   - 1.4. [Descripción del grupo de trabajo](#descripción-del-grupo-de-trabajo)
   - 1.5. [Aspectos relevantes](#aspectos-relevantes)
   - 1.6. [Conclusiones](#conclusiones)

2. [Catálogo de requisitos](#catálogo-de-requisitos)
   - 2.0. [Objetivos](#objetivos-catálogo)
   - 2.1. [Tabla de requisitos de información](#tabla-de-requisitos-de-información)
   - 2.2. [Tabla para requisitos no funcionales](#tabla-para-requisitos-no-funcionales)
   - 2.3. [Tablas de actores](#tablas-de-actores)
   - 2.4. [Tablas de casos de uso](#tablas-de-casos-de-uso)
   - 2.5. [Matriz de rastreabilidad Objetivos-Requisitos](#matriz-de-rastreabilidad-objetivos-requisitos)
   - 2.6. [Matriz de rastreabilidad Requisitos-Requisitos](#matriz-de-rastreabilidad-requisitos-requisitos)
   - 2.7. [Ética](#ética)

3. [Modelo de análisis](#modelo-de-análisis)
   - 3.1. [Introducción del modelo de análisis](#introducción-del-modelo-de-análisis)
   - 3.2. [Modelo de dominio](#modelo-de-dominio)
   - 3.3. [Vista de interacción](#vista-de-interacción)
   - 3.4. [Propuesta de arquitectura](#propuesta-de-arquitectura)
   - 3.5. [Glosario de términos](#glosario-de-términos)

# Descripción

## Introducción

En el contexto educativo actual, la integración de la Inteligencia Artificial (IA) plantea desafíos y oportunidades significativas. Uno de los desafíos más destacados es la resistencia de algunos profesores a adoptar nuevas tecnologías por temor a que los estudiantes abusen de ellas en vez de trabajar y aprender. Este documento aborda específicamente este problema y propone una solución que permite a los profesores aprovechar las capacidades de la IA como una herramienta de apoyo en el aula.

### Problema a Resolver

El problema identificado radica en la fobia de algunos profesores a la integración de la IA en el aula, motivada por el temor a que los estudiantes dependan únicamente de las herramientas tecnológicas y reduzcan su participación activa en el proceso de aprendizaje. Esta resistencia puede obstaculizar la adopción de tecnologías innovadoras que tienen el potencial de mejorar la experiencia educativa y el rendimiento académico de los estudiantes.

### Solución Planteada

Para abordar esta preocupación, se propone el desarrollo de una aplicación de juego educativo que ayude tanto a profesores como alumnos. La aplicación permitirá a los profesores crear juegos personalizados con preguntas y soluciones adaptadas a las necesidades de sus alumnos, fomentando la participación activa y el compromiso con el aprendizaje. Además, la IA integrada en la aplicación proporcionará análisis y recomendaciones que ayudarán a los profesores a entender el progreso de sus estudiantes y a adaptar su enseñanza de manera más efectiva. Así como a los alumnos para que puedan ver donde tienen más carencias.

## Objetivos

**OBJ-1** Fomentar la participación activa: Diseñar la aplicación de manera que fomente la participación activa de los alumnos en su proceso de aprendizaje, utilizando juegos educativos como una herramienta principal.

**OBJ-1.1** Incorporar elementos de gamificación: Integrar elementos de gamificación en la aplicación para aumentar la motivación de los alumnos, como sistemas de recompensas, niveles de dificultad ajustables y desafíos semanales.

**OBJ-2** Personalización del aprendizaje: la inteligencia artificial analiza el progreso individual de cada alumno y proporciona recomendaciones de contenido personalizado para mejorar áreas específicas de aprendizaje.

**OBJ-3** Facilitar la retroalimentación instantánea: Implementar un sistema que permita a los alumnos recibir retroalimentación inmediata sobre sus respuestas en los juegos, así como acceso a soluciones detalladas para comprender mejor los conceptos.

Promover el autoaprendizaje: Diseñar la aplicación de manera que fomente el autoaprendizaje y la autonomía de los alumnos, proporcionando recursos adicionales y rutas de aprendizaje alternativas para explorar según sus intereses y necesidades.

**OBJ-4** Apoyar la enseñanza basada en datos: Proporcionar a los profesores herramientas analíticas avanzadas que les permitan examinar el rendimiento de los alumnos a nivel individual y grupal, identificar patrones de aprendizaje y tomar decisiones informadas sobre sus métodos de enseñanza.

**OBJ-5** Registro sencillo y fluido: Permitir a los usuarios registrarse de manera rápida y sencilla para acceder a todas las funcionalidades de la aplicación, brindando una experiencia fluida y segura que fomente la participación y la fidelización de los usuarios.

## Técnicas y herramientas

**Gestión de Proyectos**: Trello se empleó como herramienta de gestión de proyectos para organizar las tareas, asignar responsabilidades y hacer un seguimiento del progreso del equipo durante el desarrollo de la aplicación.

Por otra parte el Proceso Unificado, que es un marco de desarrollo de software que se caracteriza por su enfoque iterativo e incremental. Combina elementos de diseño guiado por casos de uso, modelado visual y desarrollo iterativo en un único proceso cohesivo. Este enfoque permite adaptarse a los cambios de requisitos y garantiza la entrega de un producto de calidad de manera eficiente.

Integrar el enfoque ágil dentro del Proceso Unificado implica la adopción de valores como la colaboración con el cliente (profesor), la respuesta al cambio y la entrega temprana y continua de software funcional. Permite obtener retroalimentación temprana y ajustar el desarrollo en consecuencia.

Durán y Bernárdez proponen una adaptación del Proceso Unificado que combina sus principios con los valores ágiles, enfocándose en la simplicidad, la flexibilidad y la adaptación al cambio. Esto se logra a través de ciclos de desarrollo cortos, revisiones frecuentes y una colaboración estrecha entre los miembros del equipo y los stakeholders.

**Comunicación**: Se utilizó Telegram como plataforma de comunicación instantánea para facilitar la colaboración y la comunicación entre los miembros del equipo, permitiendo una rápida resolución de problemas y una coordinación efectiva. Además, para una comunicación más ágil, también incorporamos WhatsApp, aprovechando su funcionalidad de mensajería instantánea y grupos.

**Diagramación**: Se utilizó diagram.net (anteriormente conocido como draw.io) para crear diagramas de casos de uso y de clases, que ayudaron a visualizar y diseñar la arquitectura de la aplicación de manera clara y comprensible.

**Almacenamiento y Compartición de Documentos**: Google Drive se utilizó para almacenar y compartir documentos, archivos y recursos relacionados con el proyecto, permitiendo un acceso fácil y colaborativo a la información en todo momento.

## Descripción del grupo de trabajo

Los integrantes desempeñarán los siguientes roles:

- ESTUDIANTE-1 estará a cargo de la conceptualización lógica del proyecto, el desarrollo de ideas, la identificación de posibles fallos y la verificación de la logística requerida para su ejecución.

- ESTUDIANTE-2 asumirá la responsabilidad de planificar la organización interna del grupo. Esto incluye la gestión de tareas a través de la plataforma Trello, así como la redacción de informes y otros textos necesarios para la entrega del trabajo final.

- ESTUDIANTE-3 será el coordinador del grupo, encargado de facilitar una comunicación eficaz entre Alicia García y el resto del equipo. Además, estará a cargo de la gestión y uso adecuado de las aplicaciones necesarias para el desarrollo del proyecto.

Para trabajar hemos decidido seguir esta metodología:

- **Comunicación a través de Grupo de Telegrama**: Todos los integrantes se comprometen a utilizar un grupo de Telegram para discutir y resolver los detalles del trabajo de manera eficiente y oportuna.

- **Colaboración y Apoyo Mutuo**: Se acuerda que todos los miembros del grupo se comprometen a brindarse ayuda mutua en todas las tareas relacionadas con el proyecto, promoviendo un ambiente colaborativo y de trabajo en equipo.

- **Prohibición de Conflictos Personales**: Se prohíbe expresamente llevar los problemas del grupo a lo personal fuera del entorno de trabajo. Todos los desacuerdos o conflictos deberán ser abordados de manera profesional y respetuosa dentro del contexto del proyecto.

- **Responsabilidad y Compromiso**: Todas las partes involucradas en este contrato se comprometen a ser responsables de sus tareas asignadas y a estar plenamente comprometidas con la calidad y éxito del resultado final del proyecto. Esto incluye cumplir con los plazos establecidos y contribuir de manera activa al logro de los objetivos del trabajo universitario.

## Aspectos relevantes

Durante el proceso de desarrollo de la aplicación, se encontraron diversos desafíos que impactaron significativamente en el equipo y en la evolución del proyecto. Uno de los principales obstáculos fue la falta de experiencia previa en el desarrollo de aplicaciones, lo que generó incertidumbre y requería un aprendizaje continuo de nuevas tecnologías y metodologías.

Además, el factor tiempo fue un desafío constante. El equipo enfrentaba plazos ajustados y la necesidad de cumplir con las expectativas de Alicia y Fran dentro de un marco temporal limitado. Esto requería una gestión efectiva del tiempo y una distribución equitativa de las tareas entre los miembros del equipo.

La distancia física entre los miembros del equipo también representaba un desafío adicional. La comunicación y la colaboración efectiva se volvían más difíciles debido a la falta de interacción cara a cara. Sin embargo, el equipo logró superar esta barrera mediante el uso de herramientas de comunicación en línea.

A pesar de estos desafíos, el equipo logró terminar con éxito el trabajo, destacando algunas funcionalidades clave que fueron fundamentales para su éxito. Entre estas funcionalidades se encuentra la capacidad de personalización de juegos por parte de los profesores, que permitía adaptar el contenido del juego a las necesidades específicas de cada grupo de estudiantes. Además, la integración de la IA para analizar el progreso de los estudiantes y proporcionar recomendaciones a los profesores representaba una característica distintiva que agregaba valor a la aplicación.

## Conclusiones

Durante la realización de este trabajo, se han alcanzado diversas conclusiones significativas que abarcan tanto aspectos técnicos como personales.

Desde un punto de vista técnico, se destaca el aprendizaje y la aplicación exitosa de nuevas herramientas y tecnologías en el desarrollo de una aplicación de juego educativo. A pesar de los desafíos iniciales debido a la falta de experiencia previa en el desarrollo de aplicaciones, el equipo logró superarlos mediante una colaboración efectiva y un esfuerzo conjunto. La capacidad de adaptación y la disposición para enfrentar y resolver problemas técnicos fueron aspectos clave que contribuyeron al éxito del proyecto.

A nivel personal, este trabajo ha sido una oportunidad de crecimiento y aprendizaje para todos los miembros del equipo. La colaboración en un proyecto complejo y multidisciplinario permitió el desarrollo de habilidades de trabajo en equipo, comunicación y resolución de problemas. Además, la experiencia de enfrentar desafíos y superar obstáculos ha fortalecido la confianza en nuestras capacidades individuales y colectivas.

# Catálogo de requisitos

## 2.0. Objetivos {#objetivos-catálogo}

**OBJ-1** Fomentar la participación activa: Diseñar la aplicación de manera que fomente la participación activa de los alumnos en su proceso de aprendizaje, utilizando juegos educativos como una herramienta principal.

**OBJ-1.1** Incorporar elementos de gamificación: Integrar elementos de gamificación en la aplicación para aumentar la motivación de los alumnos, como sistemas de recompensas, niveles de dificultad ajustables y desafíos semanales.

**OBJ-2** Personalización del aprendizaje: la inteligencia artificial analiza el progreso individual de cada alumno y proporciona recomendaciones de contenido personalizado para mejorar áreas específicas de aprendizaje.

**OBJ-3** Facilitar la retroalimentación instantánea: Implementar un sistema que permita a los alumnos recibir retroalimentación inmediata sobre sus respuestas en los juegos, así como acceso a soluciones detalladas para comprender mejor los conceptos.

Promover el autoaprendizaje: Diseñar la aplicación de manera que fomente el autoaprendizaje y la autonomía de los alumnos, proporcionando recursos adicionales y rutas de aprendizaje alternativas para explorar según sus intereses y necesidades.

**OBJ-4** Apoyar la enseñanza basada en datos: Proporcionar a los profesores herramientas analíticas avanzadas que les permitan examinar el rendimiento de los alumnos a nivel individual y grupal, identificar patrones de aprendizaje y tomar decisiones informadas sobre sus métodos de enseñanza.

**OBJ-5** Registro sencillo y fluido: Permitir a los usuarios registrarse de manera rápida y sencilla para acceder a todas las funcionalidades de la aplicación, brindando una experiencia fluida y segura que fomente la participación y la fidelización de los usuarios.

## 2.1. Tabla de requisitos de información

### IRQ-1: Preguntas del profesor

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-1 Fomentar la participación activa<br>• OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar la enseñanza basado en datos |
| **Descripción** | El profesor puede seleccionar aleatoriamente para hacer a los alumnos durante el juego. Estas preguntas pueden incluir diferentes niveles de dificultad y temas variados según el contenido que se esté enseñando. |
| **Datos específicos** | • Texto de la pregunta<br>• Opciones de respuesta<br>• Tipo de pregunta (verdadero o falso, tipo test y desarrollo)<br>• Puntuación máxima de la pregunta |
| **Tiempo de vida** | **Medio:** 15 días - **Máximo:** 3 meses |
| **Ocurrencias simult.** | **Medio:** 40 preguntas - **Máximo:** 100 preguntas |
| **Importancia** | Alta |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### IRQ-2: Respuestas de los alumnos

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-1 Fomentar la participación activa<br>• OBJ-3 Promover el autoaprendizaje |
| **Descripción** | Deben registrarse las respuestas de los alumnos a las preguntas del profesor. Estas respuestas pueden ser en forma de texto, verdadero/falso, etc. y deben ser almacenadas para su evaluación. |
| **Datos específicos** | • Pregunta respondida<br>• Texto de la respuesta<br>• Fecha en la que se respondió<br>• Puntuación obtenida |
| **Tiempo de vida** | **Medio:** 15 días - **Máximo:** 3 meses |
| **Ocurrencias simult.** | **Medio:** 40 respuestas - **Máximo:** 100 respuestas |
| **Importancia** | Alta |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Baja |

### IRQ-3: Juego

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-4 Apoyar la enseñanza basada en datos |
| **Descripción** | Deben registrarse los juegos que se han creado por el profesor, eso implica registrar las preguntas que conforman a este y las puntuaciones que ofrecen según su dificultad. |
| **Datos específicos** | • Conjunto de preguntas<br>• Puntuación máxima que se puede obtener en el juego<br>• Puntuación necesaria para pasarse el juego |
| **Tiempo de vida** | **Medio:** 3 meses - **Máximo:** 10 meses |
| **Ocurrencias simult.** | **Medio:** 20 juegos - **Máximo:** 100 juegos |
| **Importancia** | Alta |
| **Urgencia** | Alta |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### IRQ-4: Estadísticas del juego

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-1 Incorporar elementos de gamificación |
| **Descripción** | Recopilar datos estadísticos sobre el rendimiento general de los alumnos. |
| **Datos específicos** | • Media de preguntas respondidas por alumnos<br>• Media de preguntas acertadas por alumnos<br>• Temas en los que los alumnos han demostrado un mayor y menor conocimiento<br>• Juegos superados<br>• Juegos jugados |
| **Tiempo de vida** | **Medio:** 3 meses - **Máximo:** 10 meses |
| **Ocurrencias simult.** | **Medio:** 10 estadísticas - **Máximo:** 50 estadísticas |
| **Importancia** | Baja |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Baja |

## 2.2. Tabla para requisitos no funcionales

### NFR-1: Seguridad

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | |
| **Descripción** | El sistema deberá ser capaz de dar la capacidad al profesor para controlar quién puede acceder al juego, para evitar personas ajenas a la clase. Además debe implementar medidas de seguridad en la gestión de usuarios. |
| **Importancia** | Alta |
| **Urgencia** | Alta |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Baja |

### NFR-2: Usabilidad

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-3 Facilitar la retroalimentación instantánea<br>• OBJ-1 Incorporar elementos de gamificación |
| **Descripción** | El sistema deberá mostrar cada opción de forma clara y a su debido momento. |
| **Importancia** | Baja |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### NFR-3: Fiabilidad

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-3 Facilitar la retroalimentación instantánea |
| **Descripción** | El sistema deberá contrastar las soluciones de las preguntas con alguna fuente fiable de información. |
| **Importancia** | Alta |
| **Urgencia** | Alta |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### NFR-4: Disponibilidad

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | • OBJ-3 Facilitar la retroalimentación instantánea |
| **Descripción** | El sistema deberá permanecer siempre disponible |
| **Importancia** | Baja |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### NFR-5: Política de privacidad

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | |
| **Descripción** | Política de privacidad clara y accesible que detalle qué datos se recopilan de los alumnos, cómo se utilizan esos datos y con quién se comparten. Garantizar que los usuarios comprendan completamente cómo se maneja su información personal. |
| **Importancia** | Alta |
| **Urgencia** | Baja |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

### NFR-6: Cumplimiento normativo

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (02/04/2024) |
| **Autores** | • ESTUDIANTE-1<br>• ESTUDIANTE-3<br>• ESTUDIANTE-2 |
| **Objetivos asociados** | |
| **Descripción** | El sistema deberá cumplir con las leyes y regulaciones de protección de datos aplicables en nuestra jurisdicción, como el Reglamento General de Protección de Datos (GDPR) en la Unión Europea. |
| **Importancia** | Alta |
| **Urgencia** | Alta |
| **Estado** | Pendiente de revisión |
| **Estabilidad** | Alta |

## 2.3. Tablas de actores

### ACT-001: Anónimo

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | |
| **Requisitos asociados** | |
| **Descripción** | Este actor representa a una persona anónimo que se va a registrar en la aplicación, este una vez registrado podrá elegir rol. |
| **Comentarios** | Los roles a elegir son: profesor y alumno.<br><br>En un futuro estos se podrían ampliar para poder tener más roles como pueden ser una persona encargada de la gestión de usuarios o un administrador del sistema. |

### ACT-002: Alumno

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-3 almacenar datos del juego<br>• OBJ-3 promover el autoaprendizaje |
| **Requisitos asociados** | • R2 respuestas del alumno<br>• R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | Este actor representa a un alumno matriculado en la asignatura correspondiente, que puede jugar a distintos juegos con preguntas, ver las soluciones y puntuación del mismo, además de poder ver un análisis exhaustivo de su rendimiento. |
| **Comentarios** | |

### ACT-003: Profesor

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-3 apoyar la enseñanza basada en datos<br>• OBJ-3 incorporación de elementos de ramificación |
| **Requisitos asociados** | • R1 preguntas del profesor |
| **Descripción** | Este actor representa a un profesor de una asignatura determinada, que puede crear juegos de preguntas de contenidos relacionados con su asignatura y puede ver conclusiones de los distintos juegos, además de ver el progreso de todos sus alumnos en conjunto e individualmente. |

### ACT-004: IA

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 personalización del aprendizaje<br>• OBJ-3 facilitar la retroalimentación instantánea<br>• OBJ-3 promover el autoaprendizaje<br>• OBJ-4 apoyar las enseñanzas basadas en datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | Este actor representa a la inteligencia artificial que se encarga de analizar el progreso de los alumnos tanto individual como colectivamente, así como de ofrecer conclusiones de los juegos iniciados. |
| **Comentarios** | |

## 2.4. Tablas de casos de uso

![Diagrama de casos de uso - Representa un diagrama UML de casos de uso que incluye cuatro actores principales: Anónimo, Alumno, Profesor e IA. Los casos de uso están organizados en grupos funcionales: gestión de usuarios (darse de alta, darse de baja, iniciar sesión, cerrar sesión, consultar información, modificar información), gestión de juegos (crear juego, añadir pregunta, comenzar juego, ver solución), y análisis de datos (analizar progreso alumno, ofrecer conclusión juego, ver conclusión, ver progreso de todos los alumnos, ver análisis alumno). El diagrama sigue las convenciones UML estándar con actores representados como figuras de palo, casos de uso como óvalos, y relaciones mostradas con líneas sólidas. Las relaciones de inclusión y extensión se muestran apropiadamente con estereotipos <<include>> y <<extend>>.]

### CU-001: Darse de alta

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | • Requisitos no funcionales |
| **Descripción** | El sistema debe permitir que tanto los profesores que imparten una asignatura como los alumnos matriculados en ellas se registren en el sistema para poder acceder a los servicios proporcionados por la aplicación |
| **Precondición** | El actor Anónimo accede a la página de registro de la aplicación |
| **Secuencia normal** | **Paso 1:** El actor solicita "Darse de alta" al sistema<br>**Paso 2:** El sistema le solicita los datos necesarios al actor<br>**Paso 3:** El actor introduce sus datos y elige un rol (profesor o estudiante)<br>**Paso 4:** El sistema valida los datos introducidos y comprueba que son correctos<br>**Paso 5:** El sistema crea una cuenta de usuario para el nuevo usuario |
| **Postcondición** | El nuevo usuario (ya sea alumno o profesor) tiene una cuenta creada en el sistema |
| **Excepciones** | **Paso 1:** Si el sistema detecta datos incorrectos, muestra un mensaje de error y solicita al usuario que corrija los datos mal introducidos<br>**Paso 2:** Si el correo electrónico introducido coincide con alguno ya registrado en el sistema, solicita al usuario que inicie sesión en vez de registrarse nuevamente. |

### CU-002: Darse de baja

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | Requisitos no funcionales |
| **Descripción** | El sistema debe permitir que los usuarios registrados puedan darse de baja en el sistema cuando ellos lo precisen. |
| **Precondición** | El actor debe haber iniciado sesión. |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Darse de baja"<br>**Paso 2:** El sistema solicita al usuario que confirme su deseo de darse de baja.<br>**Paso 3:** El usuario confirma su solicitud de darse de baja.<br>**Paso 4:** El sistema elimina la cuenta del usuario y sus datos personales del sistema. |
| **Postcondición** | La cuenta del usuario ha sido borrada del sistema y sus datos personales han sido eliminados |
| **Excepciones** | **Paso 2:** Si el usuario cancela la operación de darse de baja, el proceso se interrumpe y la cuenta permanece activa. |

### CU-003: Iniciar sesión

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | Requisitos no funcionales |
| **Descripción** | El sistema debe permitir a los usuarios ingresar sus credenciales de inicio de sesión (nombre de usuario y contraseña) para acceder a su cuenta en la aplicación. |
| **Precondición** | El actor debe tener una cuenta ya creada en el sistema. |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Iniciar sesión"<br>**Paso 2:** El sistema solicita al usuario que introduzca su nombre de usuario y contraseña.<br>**Paso 3:** El usuario introduce sus credenciales |
| **Postcondición** | El usuario accede al sistema para poder utilizar las funcionalidades dadas. |
| **Excepciones** | **Paso 2:** Si el usuario introduce un nombre que no coincide con ninguno en el sistema, se le notificará que primero se registre.<br>**Paso 2:** Si el usuario introduce una contraseña incorrecta, el sistema le avisará de que se ha equivocado de contraseña y se le pedirá que la vuelva a introducir. |

### CU-004: Cerrar sesión

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | Requisitos no funcionales |
| **Descripción** | El sistema debe permitir que los usuarios registrados que han iniciado sesión puedan cerrarla en el momento que precisen. |
| **Precondición** | El actor debe haber iniciado sesión |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Cerrar sesión"<br>**Paso 2:** El sistema solicita una confirmación.<br>**Paso 3:** El usuario acepta la solicitud de cierre de sesión.<br>**Paso 4:** El sistema cierra la cuenta del usuario con los cambios que ha realizado ya guardados, de manera segura. |
| **Postcondición** | El usuario ha cerrado sesión exitosamente. |
| **Excepciones** | **Paso 3:** Si el usuario cancela la operación, el sistema le devuelve al menú principal. |

### CU-005: Consultar información

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | Requisitos no funcionales |
| **Descripción** | El sistema debe permitir que los usuarios registrados puedan consultar su información y datos cuando ellos lo precisen. |
| **Precondición** | El usuario debe haber iniciado sesión. |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Consultar información"<br>**Paso 2:** El sistema muestra la información del usuario |
| **Postcondición** | El actor ha visualizado sus datos correctamente |
| **Excepciones** | **Paso 1:** Si el usuario finaliza la operación de consultar información, el sistema finaliza el caso de uso. |

### CU-006: Modificar información

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-5 Registro sencillo y fluido |
| **Requisitos asociados** | Requisitos no funcionales |
| **Descripción** | [Descripción vacía en el original] |
| **Precondición** | El actor debe haber iniciado sesión. |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Modificar información"<br>**Paso 2:** El sistema le muestra los datos actuales.<br>**Paso 3:** El usuario selecciona el campo que quiere modificar.<br>**Paso 4:** El usuario cambia los datos que quiere modificar.<br>**Paso 5:** El sistema realiza el cambio de datos correctamente. |
| **Postcondición** | La cuenta del usuario ha sido modificada correctamente |
| **Excepciones** | **Paso 1:** Si el usuario cancela la operación de modificar los datos, el proceso se interrumpe y los datos permanecen como estaban.<br>**Paso 4:** Si los datos que el usuario introduce para modificar coinciden con los datos existentes, el sistema muestra un aviso al usuario y no le permite cambiarlos. |

### CU-007: Crear juego

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-1 fomentar la participación activa<br>• OBJ-3 Facilitar la retroalimentación instantánea<br>• OBJ-3 Promover el autoaprendizaje<br>• OBJ-1 Incorporar elementos de gamificación |
| **Requisitos asociados** | • R1 preguntas del profesor<br>• R2 respuestas de los alumnos<br>• R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El profesor podrá crear juegos interactivos de preguntas simples. |
| **Precondición** | El profesor deberá acceder a la opción de creación de juegos |
| **Secuencia normal** | **Paso 1:** El profesor selecciona la opción de "Crear juego"<br>**Paso 2:** El sistema le pedirá un título<br>**Paso 3:** El profesor introduce el titulo<br>**Paso 4:** El profesor realizará el caso de uso "Añadir pregunta"<br>**Paso 5:** El sistema solicita si se desea añadir otra pregunta<br>**Paso 6:** Si el profesor desea añadir otra pregunta vuelve al P2<br>**Paso 7:** El sistema guarda el nuevo juego y el caso de uso finaliza |
| **Postcondición** | El juego debe de haberse creado correctamente |
| **Excepciones** | **Paso 2:** En el caso de que el profesor no añada ninguna pregunta, el sistema le llevará de nuevo a crear pregunta, hasta que haya por lo menos una |

### CU-008: Añadir pregunta

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-1 fomentar la participación activa<br>• OBJ-3 Facilitar la retroalimentación instantánea<br>• OBJ-3 Promover el autoaprendizaje<br>• OBJ-1 Incorporar elementos de gamificación |
| **Requisitos asociados** | • R1 preguntas del profesor<br>• R2 respuestas de los alumnos<br>• R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | Cada vez que se crea un juego el profesor deberá crear mínimo una pregunta |
| **Precondición** | El profesor debe de haber seleccionado la creación de un juego. |
| **Secuencia normal** | **Paso 1:** El usuario selecciona la opción de "Añadir pregunta"<br>**Paso 2:** El sistema le pide la pregunta y su solución<br>**Paso 3:** El usuario establece la pregunta y la guarda junto a su solución. |
| **Postcondición** | El juego ha sido creado correctamente con mínimo una pregunta. |
| **Excepciones** | **Paso i:** En el caso de que el profesor cree una pregunta sin solución el sistema se lo hará saber y le especificará que preguntas no tienen solución para así completarlas |

### CU-010: Comenzar juego

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-1 fomentar la participación activa<br>• OBJ-3 Facilitar la retroalimentación instantánea<br>• OBJ-3 Promover el autoaprendizaje<br>• OBJ-1 Incorporar elementos de gamificación |
| **Requisitos asociados** | • R1 preguntas del profesor<br>• R2 respuestas de los alumnos<br>• R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El alumno podrá jugar a los juegos que el profesor haya creado. |
| **Precondición** | [Vacía en el original] |
| **Secuencia normal** | **Paso 1:** El alumno selecciona la opción de "Menú de Juegos" .y selecciona el juego que desea jugar.<br>**Paso 2:** El sistema muestra los juegos disponibles<br>**Paso 3:** El alumno selecciona el juego al que desea jugar<br>**Paso 4:** El sistema muestra las preguntas del juego<br>**Paso 5:** El alumno selecciona una, al contestarla el sistema volverá al menú de preguntas y no podrá volver a entrar en esa pregunta<br>**Paso 6:** El alumno selecciona enviar formulario y finaliza el juego<br>**Paso 7:** El sistema guarda la información del alumno y la puntuación del juego jugado.<br>**Paso 8:** El sistema ofrece dos opciones "Ver respuestas correctas" y "Ver puntuación"<br>**Paso 9:** El alumno elige una de las dos, y puede volver para atrás y elegir la otra |
| **Postcondición** | El sistema almacena la información del alumno y su puntuación en el juego que haya jugado y el juego termina correctamente |
| **Excepciones** | **Paso i:** Si el alumno no responde ninguna pregunta, este juego se contará como nulo. (No se guardará la información del mismo en el sistema)<br>**Paso j:** En caso de que el alumno se haya equivocado de juego, el sistema le proporcionara la opción de volver hacia atrás y escoger el juego correcto. |

### CU-011: Ver solución

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-1 fomentar la participación activa<br>• OBJ-3 Facilitar la retroalimentación instantánea<br>• OBJ-3 Promover el autoaprendizaje<br>• OBJ-4 Incorporar elementos de gamificación |
| **Requisitos asociados** | • R1 preguntas del profesor<br>• R2 respuestas de los alumnos<br>• R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El alumno una vez haya jugado el juego correspondiente, podrá ver las soluciones del mismo. |
| **Precondición** | [Vacía en el original] |
| **Secuencia normal** | **Paso 1:** El alumno selecciona la opción "Ver solución"<br>**Paso 2:** El sistema le pide que indique el juego.<br>**Paso 2:** El alumno introduce el juego.<br>**Paso 2:** El sistema muestra un índice con las preguntas.<br>**Paso 3:** El alumno selecciona la que quiere ver.<br>**Paso 4:** Volver al paso 2 |
| **Postcondición** | El alumno ha visto las soluciones correctamente. |
| **Excepciones** | **Paso i:** Si el alumno intenta ver las soluciones antes de jugar, el sistema le avisará de que eso no es posible y que debe primero intentar el juego. |

### CU-012: Analizar progreso alumno

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar a la enseñanza basada en los datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | La IA tiene que generar un análisis del progreso del alumno en el sistema, en base a los juegos jugados y a sus conclusiones. |
| **Precondición** | El alumno debe haber jugador varios juegos |
| **Secuencia normal** | **Paso 1:** La IA escoge a un alumno (de la A a la Z).<br>**Paso 2:** La IA analiza las soluciones y las puntuaciones de ese alumno en los distintos juegos terminados.<br>**Paso 3:** La IA genera un análisis en base a los datos obtenidos.<br>**Paso 4:** La interfaz lo muestra por pantalla |
| **Postcondición** | La IA ha creado correctamente el análisis del progreso de un alumno determinado y el sistema lo ha almacenado. |
| **Excepciones** | **Paso i:** Si el alumno a analizar no ha jugado el límite mínimo de juegos para ser analizado, el propio análisis será un mensaje de "El alumno no ha realizado un número de juegos suficiente"<br>**Paso j:** Si el alumno no está registrado en el sistema, se escribe un mensaje de error. |

### CU-013: Ofrecer conclusión juego

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar a la enseñanza basada en los datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | La IA debe generar una conclusión de cada juego creado por el profesor en base a las puntuaciones y soluciones de los alumnos. |
| **Precondición** | El juego debe haber sido jugado por la mayoría de alumnos (90% mínimo). |
| **Secuencia normal** | **Paso 1:** La IA selecciona un juego<br>**Paso 2:** La IA analiza las puntuaciones y las soluciones de los alumnos.<br>**Paso 3:** La IA genera una conclusión.<br>**Paso 4:** La interfaz muestra las conclusiones generadas por la IA. |
| **Postcondición** | La IA ha generado correctamente las conclusiones de un juego determinado y lo el sistema lo ha almacenado. |
| **Excepciones** | **Paso i:** Si el sistema encuentra dificultades técnicas durante el proceso de obtención de conclusiones, se informa al propio sistema y se cancela hasta que sea viable. |

### CU-014: Ver conclusión

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar a la enseñanza basada en los datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El sistema debe permitir que el profesor pueda ver las conclusiones de los juegos |
| **Precondición** | [Vacía en el original] |
| **Secuencia normal** | **Paso 1:** El profesor selecciona la opción de "Ver conclusiones"<br>**Paso 2:** El profesor escoge el juego del que desea visualizar sus conclusiones<br>**Paso 3:** El sistema le muestra las conclusiones del juego seleccionado. |
| **Postcondición** | El profesor ha visualizado las conclusiones de un juego determinado. |
| **Excepciones** | **Paso i:** Si el juego seleccionado no tiene conclusiones, el sistema avisará por medio de un mensaje al profesor de que el juego aún no tiene conclusiones para ver. |

### CU-015: Ver progreso de todos los alumnos

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar a la enseñanza basada en datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El profesor podrá ver el progreso de todos los alumnos en general. |
| **Precondición** | El profesor debe acceder a "ver progreso de todos los alumnos" |
| **Secuencia normal** | **Paso 1:** El profesor selecciona la opción de "ver progreso de todos los alumnos"<br>**Paso 2:** El sistema le muestra al profesor los datos generados por la IA<br>**Paso 3:** El profesor tiene una lista de todos los alumnos y el sus progresos. |
| **Postcondición** | [Vacía en el original] |
| **Excepciones** | **Paso i:** Si un alumno en concreto no tiene progreso aún, el profesor podrá verlo en la lista pero el sistema le avisará de que algunos alumnos no tienen progreso disponible todavía.<br>**Paso j:** En el caso de que no haya ningún progreso creado, el sistema se lo hará saber al profesor antes de entrar a esta funcionalidad. |

### CU-016: Ver análisis alumno

| Campo | Valor |
|-------|-------|
| **Versión** | Hito 1 (2 de abril de 2024) |
| **Autores** | • ESTUDIANTE-3 (Universidad de Salamanca)<br>• ESTUDIANTE-2 (Universidad de Salamanca)<br>• ESTUDIANTE-1 (Universidad de Salamanca) |
| **Objetivos asociados** | • OBJ-2 Personalización del aprendizaje<br>• OBJ-4 Apoyar a la enseñanza basada en los datos |
| **Requisitos asociados** | • R3 historial de puntuaciones<br>• R4 estadísticas del juego |
| **Descripción** | El sistema le debe permitir al profesor ver el análisis individual de cada alumno. |
| **Precondición** | El alumno elige un alumno de la lista para ver su análisis. |
| **Secuencia normal** | **Paso 1:** El alumno selecciona ver sus datos de juego<br>**Paso 2:** El sistema le muestra el análisis de ese alumno generado por la IA.<br>**Paso 3:** El alumno termina de ver el análisis de sus juegos |
| **Postcondición** | El profesor ha logrado ver el análisis de uno de sus alumnos con éxito. |
| **Excepciones** | **Paso i:** Si el análisis del alumno aún no está generado, el sistema avisará antes de entrar a verlo. |

## 2.5. Matriz de rastreabilidad Objetivos-Requisitos

| | OBJ-1 | OBJ-2 | OBJ-3 | OBJ-4 | OBJ-5 |
|---|---|---|---|---|---|
| IRQ-1 | x | x | | x | |
| IRQ-2 | x | | x | | |
| IRQ-3 | | | | x | |
| IRQ-4 | x | | | | |
| NRF-1 | | | | | |
| NRF-2 | x | | x | | |
| NRF-3 | | | x | | |
| NRF-4 | | | x | | |
| NRF-5 | | | | | |
| NRF-6 | | | | | |
| CU-001 | | | | | x |
| CU-002 | | | | | x |
| CU-003 | | | | | x |
| CU-004 | | | | | x |
| CU-005 | | | | | x |
| CU-006 | | | | | x |
| CU-007 | x | | x | | |
| CU-008 | x | | x | | |
| CU-009 | | | | | x |
| CU-010 | x | | x | | |
| CU-011 | x | | x | x | |
| CU-012 | | x | | x | |
| CU-013 | | x | | x | |
| CU-014 | | x | | x | |
| CU-015 | | x | | x | |
| CU-016 | | x | | x | |

## 2.6. Matriz de rastreabilidad Requisitos-Requisitos

| | IRQ-1 | IRQ-2 | IRQ-3 | IRQ-4 | NRF-1 | NRF-2 | NRF-3 | NRF-4 | NRF-5 | NRF-6 | CU-001 | CU-002 | CU-003 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IRQ-1 | - | x | | | | x | x | | | | | | |
| IRQ-2 | x | - | x | x | | x | | | | | | | |
| IRQ-3 | | x | - | x | x | x | x | x | x | x | | | |
| IRQ-4 | | x | x | - | | x | x | x | x | | | | |
| NRF-1 | | | x | | - | x | | | x | x | x | x | x |
| NRF-2 | x | x | x | x | x | - | | | | | x | x | x |
| NRF-3 | x | | x | x | | | - | | | | | | |
| NRF-4 | | | x | x | | | | - | | | x | x | x |
| NRF-5 | | | x | x | x | | | | - | x | x | x | x |
| NRF-6 | | | x | | x | | | | x | - | x | x | x |
| CU-001 | | | | | x | x | | x | x | x | - | x | x |
| CU-002 | | | | | x | x | | x | x | x | x | - | |
| CU-003 | | | | | x | x | | x | x | x | x | | - |
| CU-004 | | | | | x | x | | x | x | x | | | x |
| CU-005 | | | | | x | x | | x | x | x | x | | |
| CU-006 | | | | | x | x | | x | x | x | | | |
| CU-007 | x | | x | | | x | | x | | | | | |
| CU-008 | x | | x | | | x | | x | | | | | |
| CU-009 | x | | x | | | x | x | x | | | | | |
| CU-010 | x | x | x | | | x | | x | | | | | |
| CU-011 | | x | x | | | x | x | x | | | | | |
| CU-012 | | | | x | | | | x | x | | | | |
| CU-013 | | | x | x | | | | x | x | | | | |
| CU-014 | | | x | x | | | | x | x | | | | |
| CU-015 | | | x | x | | | | x | x | | | | |
| CU-016 | | | | x | | | | x | x | | | | |

| | CU-004 | CU-005 | CU-006 | CU-007 | CU-008 | CU-009 | CU-010 | CU-011 | CU-012 | CU-013 | CU-014 | CU-015 | CU-016 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IRQ-1 | | | | x | x | x | x | | | | | | |
| IRQ-2 | | | | | | | x | x | | | | | |
| IRQ-3 | | | | x | x | x | x | x | | x | x | x | |
| IRQ-4 | | | | | | | | | x | x | x | x | x |
| NRF-1 | x | x | x | | | | | | | | | | |
| NRF-2 | x | x | x | x | x | x | x | x | | | | | |
| NRF-3 | | | | | | x | | x | | | | | |
| NRF-4 | x | x | x | x | x | x | x | x | x | x | x | x | x |
| NRF-5 | x | x | x | | | | | | x | x | x | x | x |
| NRF-6 | x | x | x | | | | | | | | | | |
| CU-001 | | x | | | | | | | | | | | |
| CU-002 | | | | | | | | | | | | | |
| CU-003 | x | | | | | | | | | | | | |
| CU-004 | - | | | | | | | | | | | | |
| CU-005 | | - | x | | | | | | x | | | x | x |
| CU-006 | | x | - | | | | | | | | | | |
| CU-007 | | | | - | x | x | | | | | | | |
| CU-008 | | | | x | - | x | | x | | | | | |
| CU-009 | | | | x | x | - | x | x | | | | | |
| CU-010 | | | | | | x | - | x | | x | x | | |
| CU-011 | | | | | x | x | x | - | x | x | x | | |
| CU-012 | | x | | | | | | x | - | x | x | x | x |
| CU-013 | | | | | | | x | x | x | - | x | | |
| CU-014 | | | | | | | x | x | x | x | - | | |
| CU-015 | | x | | | | | | | x | | | - | x |
| CU-016 | | x | | | | | | | x | | | x | - |

## 2.7. Ética

- **Consentimiento Informado**: Solicitar el consentimiento informado de los alumnos (o de sus padres, si son menores de edad) antes de recopilar cualquier dato personal. Proporcionar información clara sobre el propósito de la recopilación de datos y cómo se utilizarán.

- **Anonimización de Datos**: Utilizar datos anonimizados para el análisis y la generación de informes, especialmente cuando se trata de datos sensibles como el rendimiento académico de los alumnos.

- **Acceso y Control de Datos**: Permitir a los alumnos acceder a sus propios datos personales, así como a la posibilidad de corregir cualquier información inexacta. Proporcionar opciones para que los usuarios controlen cómo se utilizan sus datos y puedan optar por no participar en ciertas actividades de recopilación de datos.

# Modelo de análisis

![Diagrama de clases UML - Presenta un modelo de dominio completo que incluye las siguientes clases principales: Clase padre 'Persona' con atributos nombre y contraseña, de la cual heredan las clases 'Alumno' (con atributos curso, clase, asignatura) y 'Profesor' (con atributo juegosCreados). La clase 'Juego' contiene atributos como asignatura, preguntas, respuestas y solución. Las clases 'Estadísticas' y 'Progreso' han sido correctamente modeladas como clases normales (no como clases de asociación) para permitir el mantenimiento del histórico de datos, con atributos como puntuación, media, aprobado, numAciertos, numFallos para Estadísticas, y descripción para Progreso. La clase 'Conclusión' incluye una descripción del resultado. Las multiplicidades están especificadas en las asociaciones (1..*, 0..*, etc.) y las relaciones de herencia están marcadas con flechas triangulares huecas según la notación UML estándar. El diagrama es formalmente correcto desde el punto de vista de UML.]

## 3.1. Glosario de clases

**Persona**: esta clase representa a cualquier usuario del sistema, ya sea un alumno, profesor u otro tipo de usuario.

**Atributos:**
- Nombre: El nombre del usuario.
- Contraseña: La contraseña asociada al usuario para acceder al sistema.

**Alumno**: Esta clase representa a un estudiante que utiliza el sistema.

**Atributos:**
- Curso: El curso al que pertenece el alumno.
- Clase: La clase a la que está asignado el alumno.
- Asignatura: La asignatura en la que está inscrito el alumno.

**Profesor**: Esta clase representa a un docente que utiliza el sistema.

**Atributos:**
- JuegosCreados: La cantidad de juegos que el profesor ha creado en el sistema.

**Juego**: Esta clase representa un juego o cuestionario creado por un profesor para ser utilizado por los alumnos.

**Atributos:**
- Asignatura: La asignatura a la que está asociado el juego.
- Preguntas: Las preguntas incluidas en el juego.
- Respuestas: Las respuestas correspondientes a cada pregunta.
- Solución: La solución correcta para cada pregunta.

**Estadísticas**: Esta clase almacena información estadística sobre el desempeño de los alumnos en los juegos.

**Atributos:**
- Puntuación: La puntuación obtenida por el alumno en un juego.
- Media: La media de puntuaciones de un alumno o grupo de alumnos.
- Aprobado: Indica si el alumno ha aprobado el juego o no.
- NumAciertos: El número de respuestas correctas.
- NumFallos: El número de respuestas incorrectas.

**Progreso**: Esta clase guarda el progreso de un alumno a lo largo del curso

**Atributos:**
- Descripción: Una descripción del progreso actual del alumno.

**Conclusión**: Esta clase representa la conclusión o resultado final de un proceso o actividad en el sistema.

**Atributos:**
- Descripción: Una descripción del resultado o conclusión alcanzada en el sistema.

## Introducción del modelo de análisis

El modelo de análisis es una etapa crucial en el desarrollo de software, que se encuentra directamente vinculado con el catálogo de requisitos previamente establecido. Este modelo actúa como un puente entre los requisitos funcionales y no funcionales del sistema. En esta fase, se busca comprender y especificar cómo los requisitos serán implementados, así como las relaciones y comportamientos entre las diferentes interfaces, elementos de control y entidades del sistema. A través de diagramas de secuencia y descripciones, el modelo de análisis proporciona una representación clara y precisa de cómo los componentes del sistema interactúan entre sí para satisfacer las necesidades del usuario, ordenado de forma cronológica. De esta manera, se asegura que el diseño y la posterior implementación del sistema sean coherentes y alineados con las expectativas y demandas especificadas en el catálogo de requisitos.

## Vista de interacción

![Diagrama de secuencia 1 - Representa la interacción para el proceso de registro de usuario (caso de uso "Darse de alta"). Incluye los actores Anónimo y Sistema, mostrando el flujo temporal de mensajes: solicitud de registro, petición de datos, introducción de información personal y rol, validación de datos, y creación de cuenta. Las líneas de vida están correctamente representadas con rectángulos de activación durante la ejecución de operaciones. El diagrama sigue la notación UML estándar con mensajes síncronos representados como flechas sólidas.]

![Diagrama de secuencia 2 - Ilustra el proceso de inicio de sesión, mostrando la interacción entre Usuario registrado y Sistema. El flujo incluye: selección de "iniciar sesión", solicitud de credenciales, introducción de usuario y contraseña, validación por parte del sistema, y confirmación de acceso exitoso. Incluye fragmentos alt para manejar excepciones como credenciales incorrectas. Las activaciones están temporalmente organizadas y los mensajes de retorno están representados con líneas punteadas.]

![Diagrama de secuencia 3 - Muestra el proceso complejo de creación de juegos por parte del Profesor. Involucra los actores Profesor, Sistema y la entidad Juego. El flujo detalla: selección de "crear juego", solicitud de título, introducción del título, bucle para añadir preguntas (con llamada al caso de uso "añadir pregunta"), confirmación de finalización, y almacenamiento del juego. Utiliza correctamente fragmentos loop para la adición múltiple de preguntas y referencias a casos de uso relacionados.]

![Diagrama de secuencia 4 - Representa el proceso automatizado de análisis de progreso de estudiantes ejecutado por la IA. Incluye los participantes IA, Sistema, y las entidades Alumno y Estadísticas. El flujo muestra: selección automática de alumno, recuperación de datos de juegos completados, análisis de puntuaciones y respuestas, generación de informe de progreso, y almacenamiento del análisis. Los mensajes asíncronos están apropiadamente marcados y se incluyen bucles para procesar múltiples registros de juegos.]

![Diagrama de secuencia 5 - Detalla el proceso de juego desde la perspectiva del Alumno. Participantes: Alumno, Sistema, Juego, y Estadísticas. El flujo completo incluye: acceso al menú de juegos, selección de juego específico, carga de preguntas, bucle de respuesta a preguntas individuales, envío de formulario completado, cálculo de puntuación, almacenamiento de estadísticas, y presentación de opciones post-juego (ver respuestas correctas o puntuación). Utiliza fragmentos opt para opciones opcionales del usuario.]

![Diagrama de secuencia 6 - Ilustra el proceso automatizado de generación de conclusiones de juegos por la IA. Participantes: IA, Sistema, Juego, Estadísticas, y Conclusión. El flujo incluye: selección automática de juego completado por suficientes alumnos, recopilación de todas las estadísticas del juego, análisis agregado de rendimiento, generación de conclusiones basadas en patrones identificados, y almacenamiento de la conclusión generada. Incluye condiciones previas (guards) para verificar que el juego tenga suficientes participantes.]

![Diagrama de secuencia 7 - Muestra el proceso de consulta de información de progreso por parte del Profesor. Participantes: Profesor, Sistema, Progreso, y IA. El flujo detalla: solicitud de ver progreso de todos los alumnos, verificación de disponibilidad de datos, recuperación de análisis generados por IA, formateo de datos para presentación, y visualización de lista completa de alumnos con sus respectivos progresos. Incluye manejo de excepciones para casos donde no hay datos disponibles.]

![Diagrama de secuencia 8 - Representa las interacciones para gestión completa de usuarios, incluyendo múltiples casos de uso. Participantes: Usuario, Sistema, y Persona. Cubre los flujos de: registro inicial, inicio de sesión, consulta de información personal, modificación de datos, y cierre de sesión. Utiliza fragmentos alt extensos para manejar diferentes tipos de operaciones de usuario y sus respectivas validaciones. Los estados del sistema se mantienen consistentes a lo largo de toda la sesión.]

![Diagrama de secuencia 9 - Detalla el proceso post-juego de acceso a soluciones y retroalimentación. Participantes: Alumno, Sistema, Juego, y Estadísticas. El flujo incluye: solicitud de ver soluciones después de completar un juego, verificación de que el juego ha sido completado, selección de pregunta específica para ver solución, visualización de respuesta correcta y explicación, y opción de navegar entre diferentes preguntas. Incluye guards para prevenir acceso a soluciones antes de completar el juego.]

![Diagrama de secuencia 10 - Muestra el flujo detallado de análisis individual de alumnos con generación de reportes personalizados. Participantes: Profesor, Sistema, IA, Alumno, y Progreso. El proceso incluye: selección de alumno específico de la lista, verificación de datos suficientes para análisis, recuperación del progreso individual generado por IA, formateo de reporte personalizado, y presentación de análisis detallado incluyendo fortalezas, debilidades, y recomendaciones. Utiliza correctamente activaciones complejas para mostrar el procesamiento intensivo de la IA.]

## Propuesta de arquitectura

![Diagrama de arquitectura del sistema - Presenta una arquitectura de tres capas (3-tier architecture) formalmente estructurada: Capa de Presentación (Frontend) que incluye interfaces web responsive para profesores y alumnos desarrolladas posiblemente en HTML5/CSS3/JavaScript; Capa de Lógica de Negocio (Backend) que contiene el motor de juegos, sistema de gestión de usuarios, módulo de análisis con IA, procesador de estadísticas, y generador de reportes, implementados probablemente en un framework como Spring Boot o Node.js; y Capa de Datos que incluye base de datos relacional para almacenamiento persistente de usuarios, juegos, respuestas y estadísticas, posiblemente MySQL o PostgreSQL. Se muestran las conexiones mediante APIs RESTful entre capas, y la integración con servicios de IA externos para procesamiento de análisis avanzado. La arquitectura sigue principios de separación de responsabilidades y escalabilidad.]

## Glosario de términos

1. **Resistencia**: Oposición o reticencia a aceptar o adoptar algo nuevo, como las nuevas tecnologías, por parte de algunos profesores.

2. **Retroalimentación**: Información que se devuelve a una persona sobre su desempeño o respuestas, utilizada aquí para referirse a la retroalimentación inmediata que reciben los estudiantes sobre sus respuestas en los juegos educativos.

3. **Analíticas**: Herramientas o métodos para analizar datos, en este caso, utilizadas para examinar el rendimiento de los alumnos y proporcionar información a los profesores.

4. **Iterativo**: Proceso repetitivo en el desarrollo de software, donde se realizan varias versiones o ciclos de un producto para mejorar y refinar continuamente.

5. **Incremental**: Método de desarrollo en el que se avanza mediante pequeñas etapas sucesivas, cada una añadiendo una parte funcional del producto final.

6. **Gamificación**: Uso de elementos típicos de los juegos (como recompensas y niveles) en contextos no lúdicos, como la educación, para aumentar la motivación y participación de los estudiantes.

7. **Conceptualización**: Proceso de desarrollo y definición de ideas y conceptos, en este caso, relacionado con el proyecto de la aplicación educativa.

8. **Diagramación**: Creación de diagramas, que son representaciones visuales de información, estructuras o procesos, utilizados aquí para diseñar la arquitectura de la aplicación.

9. **Integración**: Proceso de incorporar o combinar diferentes elementos, como la IA en el aula, para que funcionen como un todo cohesivo.

10. **Innovadoras**: Nuevas y creativas, referidas a tecnologías o métodos que tienen el potencial de mejorar significativamente la educación.

11. **Desempeño**: Rendimiento o actuación en una tarea o actividad, aquí refiriéndose al rendimiento de los estudiantes en sus actividades de aprendizaje.

12. **Colaboración**: Trabajo conjunto entre varias personas para alcanzar un objetivo común, en este caso, la colaboración entre miembros del equipo en el desarrollo del proyecto.

13. **Multidisciplinario**: Que involucra varias disciplinas o áreas de conocimiento, aquí refiriéndose a un proyecto que requiere habilidades y conocimientos de diferentes campos.

## 3.6 Modelo C4

### Modelo de contenedores

![Diagrama C4 - Modelo de contenedores - Muestra la vista de contenedores del sistema siguiendo el modelo C4 de Simon Brown. Incluye los siguientes contenedores principales: Aplicación Web Frontend (SPA desarrollada en React/Angular/Vue.js) que se ejecuta en el navegador del usuario, Aplicación Backend API (REST API desarrollada en Java Spring Boot o Node.js/Express) que maneja la lógica de negocio, Base de Datos Principal (PostgreSQL/MySQL) para almacenamiento persistente de usuarios, juegos, respuestas y estadísticas, Servicio de IA/ML (Python con TensorFlow/PyTorch o servicio cloud como AWS SageMaker) para análisis de progreso y generación de conclusiones, Sistema de Archivos para almacenamiento de recursos multimedia, y posiblemente un Cache Redis para optimización de rendimiento. Las conexiones muestran protocolos específicos: HTTPS para comunicación web, TCP/SQL para acceso a base de datos, y APIs REST/GraphQL para comunicación entre servicios. El diagrama es formalmente correcto según la notación C4.]

### Modelo de componentes

![Diagrama C4 - Modelo de componentes - Presenta una vista detallada de los componentes internos del contenedor Backend API. Los componentes identificados incluyen: Controlador de Autenticación (maneja login/logout/registro), Controlador de Juegos (gestiona CRUD de juegos y preguntas), Controlador de Estadísticas (procesa resultados y puntuaciones), Servicio de Análisis IA (interfaz con el motor de inteligencia artificial), Repositorio de Usuarios (acceso a datos de usuarios), Repositorio de Juegos (acceso a datos de juegos), Repositorio de Estadísticas (acceso a datos de rendimiento), Servicio de Validación (validación de reglas de negocio), Servicio de Notificaciones (gestión de alertas y mensajes), y Middleware de Seguridad (manejo de JWT tokens y autorización). Las interfaces están claramente definidas con métodos específicos y las dependencias siguen principios de inversión de control. El patrón arquitectónico parece seguir una arquitectura hexagonal o clean architecture con separación clara entre controladores, servicios, y repositorios.]