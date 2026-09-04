#!/usr/bin/env bash
# init.sh — Verifica que el proyecto de documentos está sano antes de trabajar.
set -u
echo "▶ Verificando estructura..."
ARCHIVOS_CLAVE=("AGENTS.md" "feature_list.json" "progress/current.md" "docs/checklist.md")
for f in "${ARCHIVOS_CLAVE[@]}"; do
  if [ ! -f "$f" ]; then echo "✗ Falta el archivo necesario: $f"; exit 1; fi
done
echo "✓ Entorno listo. Puedes trabajar."
exit 0
