#!/bin/bash

uv pip compile pyproject.toml --quiet --output-file requirements.txt
# Check for uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
  echo "Error: There are uncommitted changes. Please commit or stash them before running this script."
  exit 1
fi
