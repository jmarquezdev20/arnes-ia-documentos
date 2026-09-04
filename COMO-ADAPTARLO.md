# Cómo adaptar este arnés a tu proyecto de documentos

Este arnés sirve para cualquier proyecto basado en documentos (artículos,
informes, tablas, notas). Para enchufarlo al tuyo:

1. **Copia estos archivos** dentro de la carpeta de tu proyecto (junto a tus
   documentos).
2. **Ajusta `docs/checklist.md`** con lo que para ti significa "bien hecho".
3. **Escribe tus tareas** en `feature_list.json` (qué quieres que haga con tus
   documentos: un índice, rellenar una tabla, resúmenes…). Truco: abre Claude
   Code y pídele "hazme preguntas para rellenar el feature_list de este proyecto".
4. Ejecuta `./init.sh`. Si está en verde, pídele "implementa la siguiente tarea
   pendiente" o háblale de forma natural ("hazme un índice de los artículos").

Lo único que cambia respecto a un proyecto de código: aquí **no hay tests**; la
verificación es la **checklist** (`docs/checklist.md`) que revisa el agente revisor.
