# arnes-ia-documentos

Un **arnés de IA** sencillo y en español para organizar y trabajar con una
carpeta de documentos (artículos PDF, tablas Excel, notas). Lee
`COMO-ADAPTARLO.md` para enchufarlo al tuyo en unos minutos.

## Las piezas

| Pieza | Para qué sirve | Pilar |
|-------|----------------|-------|
| `AGENTS.md` | Punto de entrada: reglas y protocolo que lee la IA | 1 · vive en tu proyecto |
| `CLAUDE.md` | Puntero a AGENTS.md (portabilidad) | 1 |
| `docs/` | Arquitectura, convenciones, verificación y checklist | 1 / 3 |
| `feature_list.json` | Las tareas y su estado (pending/in_progress/done) | 2 · memoria |
| `progress/` | Lo que va haciendo cada agente (memoria fuera del modelo) | 2 |
| `.claude/agents/` | Líder, implementador y revisor | 2 · un equipo |
| `init.sh` | Verifica que el proyecto está sano antes de empezar | 3 · verificación |
| `docs/checklist.md` | Lista de comprobación que usa el revisor antes de aprobar | 3 |
| `.claude/hooks/guardian_secretos.py` | Bloquea leer tu `.env` y borrados peligrosos | 3 |

## Diferencia con el arnés de código

En un proyecto de documentos **no hay tests automáticos**. La verificación es
una **checklist** que el agente revisor comprueba a mano antes de dar cualquier
tarea por terminada. Todo lo demás funciona igual.

## Cómo usarlo

Lee `COMO-ADAPTARLO.md`: copias los archivos del arnés junto a tus documentos,
ajustas la checklist y el feature_list, y abres Claude Code.
