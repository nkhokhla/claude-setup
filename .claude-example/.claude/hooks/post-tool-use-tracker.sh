#!/bin/bash
set -e

# Post-tool-use hook for Python/uv projects
# Tracks edited Python files and suggests quality checks

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

# Skip markdown and documentation files
if [[ "$file_path" =~ \.(md|markdown|txt|rst)$ ]]; then
    exit 0
fi

# Create cache directory in project
cache_dir="$CLAUDE_PROJECT_DIR/.claude/cache/${session_id:-default}"
mkdir -p "$cache_dir"

# Log edited file with timestamp
echo "$(date +%s):$file_path" >> "$cache_dir/edited-files.log"

# Detect Python project and track quality check commands
if [[ -f "$CLAUDE_PROJECT_DIR/pyproject.toml" ]]; then
    # Python project detected

    # Check if file is Python source or test
    if [[ "$file_path" =~ \.py$ ]]; then
        # Track quality check commands
        commands_file="$cache_dir/commands.txt"

        # Add type checking
        if ! grep -q "^mypy:" "$commands_file" 2>/dev/null; then
            echo "mypy:uv run mypy src/" >> "$commands_file"
        fi

        # Add linting
        if ! grep -q "^ruff-check:" "$commands_file" 2>/dev/null; then
            echo "ruff-check:uv run ruff check ." >> "$commands_file"
        fi

        # Add formatting check
        if ! grep -q "^ruff-format:" "$commands_file" 2>/dev/null; then
            echo "ruff-format:uv run ruff format --check ." >> "$commands_file"
        fi

        # Add tests if test file or source file
        if [[ "$file_path" =~ ^tests/ ]] || [[ "$file_path" =~ ^src/ ]]; then
            if ! grep -q "^pytest:" "$commands_file" 2>/dev/null; then
                echo "pytest:uv run pytest" >> "$commands_file"
            fi
        fi
    fi

    # Track Jupyter notebook edits
    if [[ "$file_path" =~ \.ipynb$ ]]; then
        if ! grep -q "^notebook-edited:" "$cache_dir/notebook-log.txt" 2>/dev/null; then
            echo "$(date +%s):$file_path" >> "$cache_dir/notebook-log.txt"
            # Suggest clearing outputs before commit
            echo "Note: Remember to clear notebook outputs before committing" >> "$cache_dir/reminders.txt"
        fi
    fi
fi

# Exit cleanly
exit 0
