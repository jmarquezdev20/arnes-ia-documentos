# Verificación

Este proyecto no tiene tests automáticos. La verificación es manual y la
realiza el agente revisor usando la checklist de `docs/checklist.md`.

Una tarea está terminada solo cuando:

1. El agente implementador ha dejado su informe en `progress/impl_<id>.md`
   con los archivos que creó o modificó.
2. El agente revisor ha comprobado, uno a uno, todos los puntos de
   `docs/checklist.md` para esa tarea.
3. El revisor ha dejado su veredicto en `progress/review_<id>.md` con el
   resultado APRUEBA o RECHAZA y los motivos.
4. Solo si el veredicto es APRUEBA, el líder pasa la tarea a `"done"` en
   `feature_list.json`.

Si el revisor rechaza, el líder vuelve a lanzar al implementador con el
feedback concreto. No se cierra la tarea hasta que el revisor apruebe.
