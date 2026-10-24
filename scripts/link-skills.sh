#!/usr/bin/env bash
set -euo pipefail

# Symlinks every skill in skills/<skill-name>/ into local agent skill directories:
#   - ~/.claude/skills (Claude Code)
#   - ~/.agents/skills (Codex and Agent Skills-compatible harnesses)

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

names=()
srcs=()
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  names+=("$(basename "$src")")
  srcs+=("$src")
done < <(find "$REPO/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -print0)

for DEST in "${DESTS[@]}"; do
  mkdir -p "$DEST"
  for i in "${!names[@]}"; do
    name="${names[$i]}"
    src="${srcs[$i]}"
    target="$DEST/$name"

    if [ -e "$target" ] && [ ! -L "$target" ]; then
      echo "skipped $name: $target exists and is not a symlink (move it aside to link this skill)" >&2
      continue
    fi

    ln -sfn "$src" "$target"
    echo "linked $name -> $src ($DEST)"
  done
done
