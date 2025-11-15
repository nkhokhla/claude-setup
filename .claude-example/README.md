# Jupyter Analysis Template (Python + uv)

> Example showcase: Claude Code template customized for Python data analysis with uv and Jupyter notebooks

**This is a working example** showing how to customize the generic Claude Code template for a specific tech stack.

---

## What This Demonstrates

This example shows the template customized for:

- ✅ **Python 3.12+** as the primary language
- ✅ **uv** for fast package management
- ✅ **Jupyter** notebooks for interactive analysis
- ✅ **pandas, matplotlib, seaborn** for data work
- ✅ **pytest** for testing
- ✅ **mypy** for type checking
- ✅ **ruff** for linting and formatting

All TODOs from the generic template have been filled in with Python-specific values.

---

## Quick Start

### 1. Install uv

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Setup Project

```bash
cd .claude-example

# Sync dependencies (creates .venv automatically)
uv sync

# Or sync with dev dependencies
uv sync --all-extras
```

### 3. Start Jupyter

```bash
# Launch Jupyter Lab
uv run jupyter lab

# Open notebooks/01_example_analysis.ipynb
```

### 4. Run Quality Checks

```bash
# Format code
uv run ruff format .

# Lint
uv run ruff check .

# Type check
uv run mypy src/

# Test
uv run pytest

# Test with coverage
uv run pytest --cov=src --cov-report=html
```

---

## Project Structure

```
.claude-example/
├── src/analysis/              # Reusable Python modules
│   ├── __init__.py
│   ├── data.py               # Data loading utilities
│   └── viz.py                # Visualization helpers
├── notebooks/                # Jupyter notebooks
│   └── 01_example_analysis.ipynb
├── tests/                    # pytest tests
│   ├── __init__.py
│   └── test_data.py
├── .claude/                  # Claude Code infrastructure (customized)
│   ├── hooks/               # Python-specific hooks
│   ├── skills/              # Python/uv/Jupyter guidelines
│   └── ...
├── pyproject.toml           # Project config (uv-compatible)
├── .python-version          # Python version for uv
├── .gitignore               # Python-specific ignores
└── README.md                # This file
```

---

## What Was Customized

### 1. **Skill Guidelines** (`.claude/skills/project-guidelines/SKILL.md`)

All TODOs replaced with Python specifics:
- Language: Python 3.12+
- Package manager: uv
- Testing: pytest
- Linting: ruff
- Type checking: mypy
- Notebooks: Jupyter
- Code examples in Python
- PEP 8 style guide

### 2. **Skill Activation Rules** (`.claude/skills/skill-rules.json`)

Triggers customized for Python:
- **File patterns**: `src/**/*.py`, `tests/**/*.py`, `**/*.ipynb`, `pyproject.toml`
- **Keywords**: python, jupyter, pandas, dataframe, pytest, mypy, ruff
- **Content patterns**: `import pandas`, `def .*->`, `@pytest.`, `pd.DataFrame`

### 3. **Post-Tool-Use Hook** (`.claude/hooks/post-tool-use-tracker.sh`)

Python project detection:
- Detects `pyproject.toml`
- Tracks quality check commands (mypy, ruff, pytest)
- Reminds about clearing notebook outputs

### 4. **Project Files**

Example Python code:
- `src/analysis/data.py`: Data loading with type hints
- `src/analysis/viz.py`: Visualization utilities
- `tests/test_data.py`: pytest test examples
- `notebooks/01_example_analysis.ipynb`: Sample analysis notebook
- `pyproject.toml`: uv-compatible configuration
- `.python-version`: Python 3.12

---

## How To Use This as a Template

### Option 1: Copy This Example

```bash
# Copy the .claude-example to your new project
cp -r .claude-example my-new-project
cd my-new-project

# Update project name in pyproject.toml
# Start coding!
```

### Option 2: Learn and Adapt

Use this as a reference to customize the main template for your stack:

1. **Review the changes**:
   - Compare `.claude-example/.claude/skills/project-guidelines/SKILL.md` with the template version
   - See how TODOs were filled in

2. **Copy the patterns**:
   - Skill activation rules for your language
   - Hook customizations for your build system
   - Project file examples

3. **Apply to your project**:
   - Fill TODOs in the main template
   - Use this example as a guide

---

## Development Workflow

### Daily Workflow

```bash
# 1. Start Jupyter for exploration
uv run jupyter lab

# 2. Work in notebooks, extract reusable code to src/

# 3. Run quality checks
uv run ruff format .
uv run mypy src/
uv run pytest

# 4. Commit changes
git add .
git commit -m "feat(analysis): add customer segmentation"
```

### Claude Code Integration

**Skills auto-activate** when you:
- Edit Python files in `src/` or `tests/`
- Work on Jupyter notebooks
- Use keywords like "pandas", "analysis", "test"

**Hooks track** your edits and remind you to run:
- `uv run mypy src/` (type checking)
- `uv run ruff check .` (linting)
- `uv run pytest` (tests)

**Agents available**:
- `/dev-docs <task>`: Create task documentation
- `strategic-plan-architect`: Plan new features
- `code-architecture-reviewer`: Review code quality

---

## Example: Adding a New Analysis

### 1. Create Notebook

```bash
# Create new notebook
touch notebooks/02_my_analysis.ipynb

# Start Jupyter
uv run jupyter lab
```

### 2. Explore Interactively

Work in the notebook, import from `analysis` package:

```python
from analysis.data import load_dataset, clean_data
from analysis.viz import plot_distribution

df = load_dataset("data.csv")
df_clean = clean_data(df)
plot_distribution(df_clean['age'])
```

### 3. Extract Reusable Code

When you write a function you'll reuse, move it to `src/analysis/`:

```python
# src/analysis/stats.py
def calculate_summary(df: pd.DataFrame) -> dict[str, float]:
    """Calculate summary statistics."""
    return {
        'mean': df.mean(),
        'median': df.median(),
        'std': df.std()
    }
```

### 4. Add Tests

```python
# tests/test_stats.py
from analysis.stats import calculate_summary

def test_calculate_summary():
    df = pd.DataFrame({'a': [1, 2, 3]})
    result = calculate_summary(df)
    assert result['mean'] == 2.0
```

### 5. Run Quality Checks

```bash
uv run mypy src/        # Type check
uv run ruff check .     # Lint
uv run pytest           # Test
```

### 6. Commit

```bash
git add .
git commit -m "feat(analysis): add summary statistics calculation"
```

---

## Dependencies

### Core

- **pandas**: Data manipulation
- **jupyter**: Interactive notebooks
- **matplotlib**: Plotting
- **seaborn**: Statistical visualization
- **numpy**: Numerical computing

### Dev

- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **mypy**: Static type checking
- **ruff**: Linting and formatting
- **ipykernel**: Jupyter kernel
- **pandas-stubs**: Type stubs for pandas

All managed by **uv** via `pyproject.toml`.

---

## Testing

### Run Tests

```bash
# All tests
uv run pytest

# With coverage
uv run pytest --cov=src --cov-report=term-missing

# Specific test file
uv run pytest tests/test_data.py

# Specific test
uv run pytest tests/test_data.py::test_clean_data_removes_nulls
```

### Test Structure

```
tests/
├── __init__.py
├── test_data.py          # Tests for data module
└── test_viz.py           # Tests for viz module (add as needed)
```

---

## Type Checking

```bash
# Check all source code
uv run mypy src/

# Strict mode (recommended)
uv run mypy --strict src/
```

Configuration in `pyproject.toml`:
```toml
[tool.mypy]
python_version = "3.12"
strict = true
```

---

## Linting and Formatting

```bash
# Format code (auto-fix)
uv run ruff format .

# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .
```

Configuration in `pyproject.toml`:
```toml
[tool.ruff]
line-length = 88
target-version = "py312"
```

---

## Jupyter Best Practices

### Before Committing Notebooks

```bash
# Clear outputs
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb

# Or configure git to do it automatically
# (see Jupyter docs for git filters)
```

### Notebook Hygiene

- ✅ Add markdown cells to explain your analysis
- ✅ Keep cells focused (one task per cell)
- ✅ Import reusable code from `src/`
- ✅ Restart kernel and run all before finalizing
- ✅ Clear outputs before committing (or commit them for docs)
- ❌ Don't define complex functions in notebooks
- ❌ Don't hard-code file paths

---

## Comparison: Template vs. Example

| Aspect | Generic Template | This Example |
|--------|-----------------|--------------|
| Language | `TODO: <primary-language>` | Python 3.12+ |
| Package Manager | `TODO: <package-manager>` | uv |
| Testing | `TODO: <testing-framework>` | pytest |
| Linting | `TODO: <lint-command>` | ruff |
| Type Checking | `TODO: <type-system>` | mypy |
| Notebooks | Not included | Jupyter Lab |
| Skill Rules | Generic patterns | Python-specific triggers |
| Post-Tool-Use Hook | Minimal tracking | Python build detection |
| Example Code | None | data.py, viz.py, tests |

---

## Resources

- **uv Documentation**: https://docs.astral.sh/uv/
- **Jupyter**: https://jupyter.org/
- **pandas**: https://pandas.pydata.org/
- **pytest**: https://docs.pytest.org/
- **mypy**: https://mypy.readthedocs.io/
- **ruff**: https://docs.astral.sh/ruff/

---

## Next Steps

1. **Explore the notebook**: Open `notebooks/01_example_analysis.ipynb`
2. **Review the code**: Check `src/analysis/` modules
3. **Run the tests**: `uv run pytest`
4. **Try the tools**: Run mypy, ruff, and pytest
5. **Use as reference**: Apply these patterns to your own projects

---

**This example demonstrates how to transform the generic Claude Code template into a production-ready Python data analysis project.** 🚀

For the generic template, see the parent directory: `../README.md`
