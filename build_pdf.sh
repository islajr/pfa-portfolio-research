#!/usr/bin/env bash
# build_pdf.sh — Compile dissertation markdown → PDF via pandoc/xelatex
# Uses traditional Computer Modern / Latin Modern academic typography.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DIST="$ROOT/outputs"
SRC="$ROOT/dissertation/dissertation.md"
TEMPLATE="$ROOT/dissertation/dissertation.latex"

mkdir -p "$DIST"

echo "=================================================================="
echo "  DISSERTATION PDF COMPILATION SYSTEM"
echo "  Author: AKINMOKUN ISAAC OLUWASEUN (ESM/2019/023)"
echo "  Typography: Latin Modern / Computer Modern"
echo "=================================================================="
echo "Source: $SRC"
echo "Source lines: $(wc -l < "$SRC")"
echo ""

echo "▶  Compiling canonical dissertation PDF..."
sed -e 's|https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/|outputs/charts/|g' \
    -e 's|https://github.com/islajr/pfa-portfolio-research/blob/master/outputs/charts/|outputs/charts/|g' \
    -e 's|https://github.com/islajr/pfa-portfolio-research/tree/master/outputs/charts/|outputs/charts/|g' \
    "$SRC" | pandoc \
  --template="$TEMPLATE" \
  --pdf-engine=xelatex \
  --from=markdown+tex_math_dollars+raw_tex+pipe_tables+implicit_figures \
  --resource-path="$ROOT:$ROOT/dissertation:$ROOT/outputs:$ROOT/outputs/charts" \
  --top-level-division=chapter \
  --variable=documentclass:report \
  --variable=classoption:a4paper \
  --variable=classoption:oneside \
  --variable=fontsize:12pt \
  --variable=geometry:top=30mm \
  --variable=geometry:bottom=25mm \
  --variable=geometry:left=38mm \
  --variable=geometry:right=25mm \
  --variable=geometry:headheight=15pt \
  --variable=linestretch:2 \
  --variable=numbersections:false \
  -o "$DIST/dissertation.pdf" \
  2>&1

echo "✅  Dissertation PDF written to:"
echo "    • $DIST/dissertation.pdf ($(ls -lh "$DIST/dissertation.pdf" | awk '{print $5}'))"
echo ""
echo "=================================================================="
echo "  Build completed successfully!"
echo "=================================================================="
