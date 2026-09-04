#!/usr/bin/env python3
"""PreToolUse hook: bloquea leer/editar .env reales y borrados peligrosos."""
import json
import re
import sys

datos = json.load(sys.stdin)
tool = datos.get("tool_name", "")
entrada = datos.get("tool_input", {})


def denegar(motivo):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": motivo,
        }
    }))
    sys.exit(0)


# 1) Proteger archivos .env reales (permitir .env.example)
ruta = entrada.get("file_path", "") or entrada.get("path", "")
if ruta:
    nombre = ruta.split("/")[-1]
    if nombre == ".env" or (nombre.startswith(".env") and not nombre.endswith(".example")):
        denegar("Bloqueado: no se tocan archivos .env reales. Usa .env.example.")

# 2) Bloquear borrados recursivos peligrosos en Bash
if tool == "Bash":
    cmd = entrada.get("command", "")
    patrones = [r"\brm\s+-rf\b", r"\brmdir\b", r"\bfind\b.*-delete\b", r"\bgit\s+clean\s+-[a-z]*d"]
    if any(re.search(p, cmd) for p in patrones):
        denegar("Bloqueado: comando de borrado recursivo peligroso.")

sys.exit(0)
