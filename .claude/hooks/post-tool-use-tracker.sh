#!/bin/bash
set -e

# Post-tool-use hook that tracks edited files
# This runs after Edit, MultiEdit, or Write tools complete successfully
# Minimal, stack-agnostic version for template projects

# Read tool information from stdin
tool_info=$(cat)

# Extract relevant data
tool_name=$(echo "$tool_info" | jq -r '.tool_name // empty')
file_path=$(echo "$tool_info" | jq -r '.tool_input.file_path // empty')
session_id=$(echo "$tool_info" | jq -r '.session_id // empty')

# Skip if not an edit tool or no file path
if [[ ! "$tool_name" =~ ^(Edit|MultiEdit|Write)$ ]] || [[ -z "$file_path" ]]; then
    exit 0
fi

# Skip markdown and documentation files (they don't need build tracking)
if [[ "$file_path" =~ \.(md|markdown|txt|rst)$ ]]; then
    exit 0
fi

# Create cache directory in project
cache_dir="$CLAUDE_PROJECT_DIR/.claude/cache/${session_id:-default}"
mkdir -p "$cache_dir"

# Log edited file with timestamp
echo "$(date +%s):$file_path" >> "$cache_dir/edited-files.log"

# TODO: Add project-specific build/test tracking here
# Once you know your stack, you can detect build commands and track affected modules
# Example patterns to implement:
#   - Detect package.json and track npm/yarn/pnpm builds
#   - Detect requirements.txt and track Python test commands
#   - Detect Cargo.toml and track Rust builds
#   - Detect go.mod and track Go test commands

# Exit cleanly
exit 0
