---
name: project-guidelines
description: Comprehensive Python project development guidelines using uv and Jupyter notebooks. Use when creating modules, notebooks, tests, or working with Python code, data analysis, visualization, or package management.
---

# Project Guidelines - Python/uv/Jupyter

## Purpose

Establish consistency and best practices for Python development using **uv** (fast package manager) and **Jupyter notebooks** for data analysis and experimentation.

## When to Use This Skill

Automatically activates when working on:
- Creating or modifying Python modules in `src/`
- Working with Jupyter notebooks in `notebooks/`
- Writing tests with pytest
- Managing dependencies with uv
- Data analysis and visualization tasks

---

## Quick Start

### New Feature Checklist

- [ ] **Plan**: Define requirements and approach
- [ ] **Module**: Create Python module in `src/` with type hints
- [ ] **Notebook**: Create exploratory notebook in `notebooks/` (if needed)
- [ ] **Tests**: Add pytest tests in `tests/`
- [ ] **Document**: Add docstrings and update README
- [ ] **Type Check**: Run `uv run mypy src/`
- [ ] **Lint**: Run `uv run ruff check .`
- [ ] **Format**: Run `uv run ruff format .`
- [ ] **Test**: Run `uv run pytest`
- [ ] **Commit**: Use conventional commit message

---

## Project Overview

**Project Name**: jupyter-analysis-template

**Description**: A Python project template for data analysis and exploration using Jupyter notebooks, managed with uv.

**Primary Language**: Python 3.12+

**Tech Stack**:
- **Runtime**: Python 3.12+ (managed via uv)
- **Package Manager**: uv (fast, modern Python package manager)
- **Notebooks**: Jupyter Lab
- **Testing**: pytest
- **Linting**: ruff
- **Type Checking**: mypy
- **Formatting**: ruff format

**Key Features**:
- Fast dependency management with uv
- Interactive data exploration with Jupyter
- Type-safe Python code with mypy
- Modern linting and formatting with ruff

---

## Architecture Overview

### Directory Structure

```
jupyter-analysis-template/
├── src/
│   └── analysis/          # Python modules for reusable code
│       ├── __init__.py
│       ├── data.py        # Data loading utilities
│       ├── viz.py         # Visualization helpers
│       └── utils.py       # General utilities
├── notebooks/             # Jupyter notebooks for exploration
│   ├── 01_data_exploration.ipynb
│   └── 02_analysis.ipynb
├── tests/                 # pytest tests
│   ├── __init__.py
│   ├── test_data.py
│   └── test_viz.py
├── .claude/               # Claude Code infrastructure
├── pyproject.toml         # Project metadata and dependencies (uv)
├── .python-version        # Python version for uv
├── uv.lock                # Lockfile (auto-generated)
├── .gitignore
└── README.md
```

**Key Principles**:
- **Separation**: Notebooks for exploration, `src/` for reusable code
- **Type Safety**: Use type hints everywhere
- **Testing**: Test reusable code in `src/`, not notebooks
- **Clean Notebooks**: Keep notebooks focused and well-documented

See [structure.md](resources/structure.md) for detailed organization.

---

## Coding Standards

### Python Style

**PEP 8 with ruff**:
- 4 spaces for indentation
- 88 character line length (Black-compatible)
- Use ruff for linting and formatting

### Naming Conventions

```python
# Modules and packages: lowercase with underscores
# data_loader.py, visualization_utils.py

# Classes: PascalCase
class DataProcessor:
    pass

class VisualizationHelper:
    pass

# Functions and variables: snake_case
def load_dataset(file_path: str) -> pd.DataFrame:
    pass

user_count = 42
is_valid = True

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Private: leading underscore
def _internal_helper():
    pass

_cache = {}
```

### Type Hints

**Always use type hints**:

```python
from typing import Optional, List, Dict, Any
import pandas as pd

def process_data(
    df: pd.DataFrame,
    columns: List[str],
    threshold: float = 0.5
) -> pd.DataFrame:
    """Process dataframe with specified columns."""
    ...

def fetch_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Fetch user by ID, returns None if not found."""
    ...
```

### Docstrings

**Use Google-style docstrings**:

```python
def calculate_statistics(data: List[float]) -> Dict[str, float]:
    """Calculate basic statistics for a dataset.

    Args:
        data: List of numeric values to analyze.

    Returns:
        Dictionary containing mean, median, and std deviation.

    Raises:
        ValueError: If data list is empty.

    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'std': 1.41}
    """
    if not data:
        raise ValueError("Data list cannot be empty")
    ...
```

### Error Handling

```python
# Explicit error types
try:
    result = process_data(df)
except FileNotFoundError as e:
    logger.error(f"Data file not found: {e}")
    raise
except pd.errors.EmptyDataError:
    logger.warning("Empty dataset, using defaults")
    result = pd.DataFrame()

# Context in errors
if value < 0:
    raise ValueError(f"Expected positive value, got {value}")

# Use logging, not print
import logging
logger = logging.getLogger(__name__)
logger.info("Processing started")
```

---

## Jupyter Notebooks Best Practices

### Notebook Organization

```markdown
# Notebook Title

**Author**: Your Name
**Created**: 2025-11-15
**Purpose**: Brief description of analysis

## Setup

Import libraries and load data

## Data Exploration

Initial data inspection and visualization

## Analysis

Main analytical work

## Conclusions

Key findings and next steps
```

### Code in Notebooks

```python
# ✅ Good: Import reusable code from src/
from analysis.data import load_dataset
from analysis.viz import plot_distribution

df = load_dataset("data.csv")
plot_distribution(df['column'])

# ❌ Bad: Defining complex functions in notebooks
# (Move to src/ modules instead)
```

### Notebook Hygiene

- **Clear outputs before committing**: `jupyter nbconvert --clear-output --inplace notebook.ipynb`
- **Keep cells focused**: One task per cell
- **Add markdown**: Explain your thinking
- **Restart and run all**: Before finalizing, restart kernel and run all cells
- **Extract reusable code**: Move functions to `src/` when you reuse them

---

## Dependency Management with uv

### Why uv?

- **Fast**: 10-100x faster than pip
- **Reliable**: Deterministic resolution like Poetry
- **Simple**: Uses `pyproject.toml`, no new concepts
- **Compatible**: Works with existing Python ecosystem

### Common Commands

```bash
# Create new project
uv init

# Add dependency
uv add pandas jupyter

# Add dev dependency
uv add --dev pytest mypy ruff

# Install all dependencies
uv sync

# Run command in venv
uv run jupyter lab
uv run pytest
uv run mypy src/

# Update dependencies
uv lock --upgrade

# Remove dependency
uv remove pandas
```

### pyproject.toml Structure

```toml
[project]
name = "jupyter-analysis-template"
version = "0.1.0"
description = "Python data analysis template"
requires-python = ">=3.12"
dependencies = [
    "pandas>=2.0.0",
    "jupyter>=1.0.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "mypy>=1.0.0",
    "ruff>=0.1.0",
    "ipykernel>=6.25.0",
]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.mypy]
python_version = "3.12"
strict = true
```

---

## Testing Strategy

### Testing Pyramid for Data Projects

```
       /\
      /E2E\      ← Few: Full pipeline tests
     /------\
    /Integr.\   ← Some: Module interaction tests
   /----------\
  /Unit Tests \  ← Many: Function-level tests
 /--------------\
```

### Test Coverage Goals

- **Unit Tests**: 80%+ coverage for `src/` modules
- **Integration Tests**: Cover data pipelines
- **Notebook Tests**: Not typically tested (exploratory)

### Writing Tests with pytest

```python
# tests/test_data.py
import pytest
import pandas as pd
from analysis.data import load_dataset, clean_data

def test_load_dataset_success():
    """Test successful dataset loading."""
    df = load_dataset("test_data.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_dataset_file_not_found():
    """Test handling of missing file."""
    with pytest.raises(FileNotFoundError):
        load_dataset("nonexistent.csv")

def test_clean_data_removes_nulls():
    """Test that clean_data removes null values."""
    df = pd.DataFrame({'a': [1, None, 3], 'b': [4, 5, None]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0

@pytest.fixture
def sample_dataframe():
    """Fixture providing sample data for tests."""
    return pd.DataFrame({
        'value': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'B', 'A']
    })

def test_analysis_with_fixture(sample_dataframe):
    """Test analysis using fixture data."""
    result = analyze(sample_dataframe)
    assert result['mean'] == 3.0
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test file
uv run pytest tests/test_data.py

# Run specific test
uv run pytest tests/test_data.py::test_load_dataset_success

# Run in verbose mode
uv run pytest -v
```

See [testing.md](resources/testing.md) for comprehensive guide.

---

## Code Quality Tools

### Linting with ruff

```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Check specific file
uv run ruff check src/analysis/data.py
```

### Type Checking with mypy

```bash
# Check all source code
uv run mypy src/

# Check specific file
uv run mypy src/analysis/data.py

# Strict mode (recommended)
uv run mypy --strict src/
```

### Pre-commit Workflow

```bash
# Before committing
uv run ruff format .       # Format code
uv run ruff check --fix .  # Fix linting issues
uv run mypy src/           # Type check
uv run pytest              # Run tests
```

---

## Git Workflow

### Branching

- **Main Branch**: `main` (stable code)
- **Feature Branches**: `feature/data-pipeline`, `feature/visualization`

### Commit Messages

**Conventional Commits**:

```
feat(data): add CSV loading with validation
fix(viz): correct color scale in heatmap
docs(readme): update installation instructions
test(data): add tests for data cleaning
refactor(utils): simplify date parsing logic
```

### .gitignore for Python

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
.Python
*.so

# Virtual environments
.venv/
venv/
env/

# Jupyter
.ipynb_checkpoints/
*.ipynb (optionally clear outputs instead)

# uv
uv.lock (commit this!)

# IDEs
.vscode/
.idea/

# Data (usually)
data/*.csv
data/*.parquet
!data/sample.csv  # Keep small examples

# Outputs
outputs/
figures/
*.png (or commit them)

# OS
.DS_Store
```

---

## Development Workflows

### Local Development

```bash
# 1. Setup (first time)
uv sync                    # Install dependencies
uv run pre-commit install  # Setup git hooks (optional)

# 2. Daily workflow
uv run jupyter lab         # Start Jupyter
# Work in notebooks...

# Extract reusable code to src/
# Write tests for new functions

uv run pytest              # Run tests
uv run mypy src/           # Type check
uv run ruff check .        # Lint

# 3. Commit
git add .
git commit -m "feat(analysis): add customer segmentation"
```

### Adding New Analysis

1. Create notebook: `notebooks/03_new_analysis.ipynb`
2. Explore data interactively
3. Extract reusable functions to `src/analysis/`
4. Add type hints and docstrings
5. Write tests in `tests/`
6. Run quality checks
7. Commit notebook + code + tests

---

## Progressive Disclosure Resources

For detailed guidance on specific topics, see:

- [structure.md](resources/structure.md): Python project organization patterns
- [workflows.md](resources/workflows.md): CI/CD for Python projects
- [testing.md](resources/testing.md): pytest strategies and patterns
- [docs.md](resources/docs.md): Python documentation with Sphinx
- [release.md](resources/release.md): Versioning and PyPI publishing
- [security.md](resources/security.md): Python-specific security practices

---

## Common Patterns

### Data Loading Pattern

```python
# src/analysis/data.py
from pathlib import Path
import pandas as pd
from typing import Optional

def load_dataset(
    file_path: str | Path,
    *,
    nrows: Optional[int] = None
) -> pd.DataFrame:
    """Load dataset from CSV with validation.

    Args:
        file_path: Path to CSV file
        nrows: Optional limit on rows to load

    Returns:
        Loaded and validated DataFrame

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If data validation fails
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path, nrows=nrows)

    # Validate
    if df.empty:
        raise ValueError("Dataset is empty")

    return df
```

### Visualization Helper Pattern

```python
# src/analysis/viz.py
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

def plot_distribution(
    data: pd.Series,
    title: Optional[str] = None,
    **kwargs
) -> plt.Figure:
    """Plot distribution with KDE overlay.

    Args:
        data: Series to plot
        title: Optional plot title
        **kwargs: Additional arguments for seaborn

    Returns:
        Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data, kde=True, ax=ax, **kwargs)

    if title:
        ax.set_title(title)

    return fig
```

---

## Troubleshooting

### Common Issues

**Issue**: `uv: command not found`
- Solution: Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

**Issue**: Jupyter kernel not found
- Solution: `uv run python -m ipykernel install --user --name=venv`

**Issue**: Import errors in notebooks
- Solution: Ensure project is in path or use: `uv run jupyter lab`

**Issue**: Type errors in tests
- Solution: Install dev dependencies: `uv sync --all-extras`

---

## References

- **uv Documentation**: https://docs.astral.sh/uv/
- **Jupyter**: https://jupyter.org/
- **ruff**: https://docs.astral.sh/ruff/
- **mypy**: https://mypy.readthedocs.io/
- **pytest**: https://docs.pytest.org/

---

**Last Updated**: 2025-11-15

**Version**: 1.0.0
