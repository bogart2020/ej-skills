#!/usr/bin/env bash
set -euo pipefail

# Packages each skill under skills/<skill-name>/ into <skill-name>.zip at the
# repository root for direct upload into Claude Desktop:
#   Claude Desktop -> Settings -> Capabilities -> Skills -> Upload skill
#
# Excludes harness-specific metadata (such as agents/openai.yaml and .DS_Store)
# so the archive contains only <skill-name>/SKILL.md and its references/scripts/assets.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO/skills"

for skill_dir in */; do
  skill_name="${skill_dir%/}"
  if [ ! -f "$skill_name/SKILL.md" ]; then
    continue
  fi

  out_zip="$REPO/${skill_name}.zip"
  rm -f "$out_zip"

  zip -r -q "$out_zip" "$skill_name" \
    -x "*/.DS_Store" \
    -x "${skill_name}/agents/*" \
    -x "${skill_name}/agents"

  echo "Packaged ${skill_name}.zip -> $out_zip"
done
