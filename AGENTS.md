# Arnés IA para documentos — Punto de entrada

Este archivo es lo primero que lees antes de hacer nada. Es un estándar abierto
(`AGENTS.md`): funciona igual en Claude Code, Codex o Gemini CLI.

Este arnés está pensado para un proyecto de **documentos** (artículos, tablas,
notas), NO de código. Por eso aquí no hay tests automáticos: la verificación es
una **checklist** que revisa el agente revisor.

## Protocolo (síguelo siempre, en este orden)

1. Ejecuta `./init.sh`. Si NO termina en verde, **para** y avisa.
2. Lee `progress/current.md` para saber si hay trabajo a medias.
3. Abre `feature_list.json` y coge la primera tarea con `"estado": "pending"`.
4. Actúa como el agente **líder** (`.claude/agents/lider.md`): orquesta a los demás.
5. Cuando una tarea esté validada por el revisor contra la checklist, pásala a
   `"done"`, anótala en `progress/history.md` y deja `progress/current.md` limpio.

## Reglas

- Una tarea solo es `done` si el revisor ha comprobado, con `docs/checklist.md`,
  que cumple TODOS sus criterios.
- **No inventes información**: todo lo que escribas en índices, tablas o resúmenes
  tiene que salir de los documentos reales del proyecto.
- Cada subagente escribe su resultado en un archivo de `progress/`, nunca solo en
  el chat.
- Nunca leas ni edites archivos `.env` reales. Un hook lo bloquea.

## Verificación  ← ESTE BLOQUE SE ADAPTA POR PROYECTO

Este proyecto NO tiene tests automáticos. Se valida con la **checklist** de
`docs/checklist.md`: el revisor comprueba cada punto a mano antes de dar una
tarea por terminada.

## Mapa del repo

- `docs/` — convenciones, verificación y la `checklist.md`.
- `.claude/agents/` — líder, implementador y revisor.
- `.claude/hooks/` — guardian_secretos (protege tu `.env` y borrados peligrosos).
- `progress/` — memoria: `current.md` (sesión actual) e `history.md` (histórico).
- `feature_list.json` — las tareas y su estado.
- `documentos/` — aquí pones tus documentos (PDF, texto, Markdown…). Vienen 2 de ejemplo que puedes borrar.
