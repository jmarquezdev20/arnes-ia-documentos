# Arquitectura del proyecto de documentos

Este arnés está pensado para trabajar con una carpeta de **documentos** en lugar
de código. El esquema habitual es:

- **Documentos** — PDFs o documentos de texto (informes, estudios, artículos
  académicos) que son la materia prima. Viven en `documentos/`. No se modifican nunca.
- **Tablas** — archivos Excel o CSV donde se recogen datos extraídos de los
  documentos (hallazgos, fechas, autores, valoraciones…).
- **Notas** — apuntes sueltos en Markdown o texto plano con ideas, referencias
  cruzadas o preguntas pendientes.

El arnés añade sobre esa carpeta tres capas de valor:

1. **Índices** — un `INDICE.md` que lista todos los documentos con sus metadatos
   básicos (autor, año, resumen en una línea).
2. **Extracción estructurada** — rellenar una tabla con datos que vienen
   directamente de los documentos (nunca inventados).
3. **Síntesis** — un `resumen-global.md` que reúne conclusiones comunes y
   señala puntos de acuerdo o discrepancia entre los documentos.

La verificación no es automática: la hace el agente revisor usando la checklist
de `docs/checklist.md`.

## Cómo organizar tu proyecto

- Pon tus documentos dentro de `documentos/` (vienen dos de ejemplo que puedes
  borrar).
- Los entregables que produce el arnés (`INDICE.md`, `resumen-tabla.md`,
  `resumen-global.md`) van en la raíz del proyecto.
- Las tareas concretas se describen en `feature_list.json`. Cámbialas por las
  tuyas: qué quieres que haga la IA con tus documentos.
