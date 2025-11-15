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

## 🎮 Try It Out: Interactive Examples

Want to experience Claude Code's automation in action? Here are specific prompts and scenarios to try in this example project.

### 1. **Skill Auto-Activation**

The `project-guidelines` skill activates automatically when you work on Python code. Try these prompts:

**Example Prompts**:
```
"Add a new function to calculate the median of a pandas Series"
→ Skill activates with Python/pandas best practices

"How should I structure tests for the visualization module?"
→ Skill activates with pytest guidance

"I want to create a notebook for customer segmentation analysis"
→ Skill activates with Jupyter best practices

"What's the best way to handle missing data in pandas?"
→ Skill activates with data cleaning patterns
```

**How to verify**: Look for the skill activation message before Claude responds.

---

### 2. **Use the Strategic Plan Architect**

Create comprehensive implementation plans for new features.

**Example Scenario**: Plan a new time-series analysis feature

**Prompt**:
```
Use the Task tool to launch the strategic-plan-architect agent.

Create a plan for adding time-series analysis capabilities to this project:
- Load time-series data from CSV
- Resample and aggregate time series
- Detect trends and seasonality
- Create time-series visualizations
- Export results to notebooks

The plan should include implementation phases, acceptance criteria, and risks.
```

**What happens**:
1. Agent analyzes current codebase
2. Creates `.claude/dev/active/time-series-analysis/` directory
3. Generates three files:
   - `time-series-analysis-plan.md`: Comprehensive implementation plan
   - `time-series-analysis-context.md`: Key decisions and files
   - `time-series-analysis-tasks.md`: Checklist to track progress

**Try it**: Follow the checklist to implement the feature step by step!

---

### 3. **Code Architecture Review**

Get expert feedback on your code quality and design.

**Example Scenario**: Review the data module

**Prompt**:
```
Use the Task tool to launch the code-architecture-reviewer agent.

Review the data.py module for:
- Code quality and type safety
- Error handling completeness
- Docstring quality
- Test coverage adequacy
- Adherence to Python best practices

Save the review to the project-setup task directory.
```

**What happens**:
1. Agent examines `src/analysis/data.py` and tests
2. Checks type hints, error handling, docstrings
3. Reviews against project guidelines
4. Saves review to `.claude/dev/active/project-setup/project-setup-code-review.md`
5. Provides categorized feedback (critical, important, minor)

**Try it**: Review the suggestions and implement improvements!

---

### 4. **Documentation Generation**

Automatically create comprehensive documentation.

**Example Scenario**: Document the visualization module

**Prompt**:
```
Use the Task tool to launch the documentation-architect agent.

Create comprehensive documentation for the visualization module (src/analysis/viz.py):
- API documentation with examples
- Usage guide for common plots
- Customization options
- Gallery of example outputs

Save the documentation to docs/visualization.md
```

**What happens**:
1. Agent analyzes `viz.py` functions and signatures
2. Gathers context from existing code
3. Creates `docs/visualization.md` with:
   - API reference for each function
   - Code examples
   - Parameter documentation
   - Visual examples (if applicable)

**Try it**: Use the generated docs as a template for other modules!

---

### 5. **Dev-Docs for Task Persistence**

Create persistent task documentation that survives context resets.

**Example Scenario**: Start a customer churn prediction feature

**Prompt**:
```
I want to implement customer churn prediction. Use /dev-docs to create task documentation.

The feature should:
- Load customer data with transaction history
- Engineer features (recency, frequency, monetary value)
- Train a logistic regression model
- Evaluate model performance
- Create visualization of feature importance
```

**What happens**:
1. Creates `.claude/dev/active/customer-churn-prediction/`
2. Generates:
   - `customer-churn-prediction-plan.md`: Full implementation plan
   - `customer-churn-prediction-context.md`: Key decisions
   - `customer-churn-prediction-tasks.md`: Checklist

**Try it**: Start implementing, then run `/dev-docs-update` before context limits!

---

### 6. **Experience Hook Automation**

See how hooks track your work and suggest quality checks.

**Example Scenario**: Add a new utility function

**Steps**:
1. Create a new file `src/analysis/stats.py`:
   ```python
   """Statistical analysis utilities."""

   import pandas as pd
   from typing import Dict

   def calculate_summary(df: pd.DataFrame) -> Dict[str, float]:
       """Calculate summary statistics for numeric columns.

       Args:
           df: DataFrame to analyze

       Returns:
           Dictionary with mean, median, std for each column
       """
       return {
           'mean': df.mean().to_dict(),
           'median': df.median().to_dict(),
           'std': df.std().to_dict()
       }
   ```

2. The `post-tool-use-tracker` hook runs automatically and logs:
   - File edited: `src/analysis/stats.py`
   - Suggests running: `uv run mypy src/`
   - Suggests running: `uv run ruff check .`
   - Suggests running: `uv run pytest`

**Try it**: Check `.claude/cache/<session-id>/commands.txt` to see tracked commands!

---

### 7. **Build a Complete Feature End-to-End**

Put it all together: plan → implement → test → review → document.

**Example Scenario**: Add data validation functionality

**Step 1: Plan** (5 minutes)
```
Use the strategic-plan-architect agent to create a plan for adding data validation:
- Validate CSV schemas (column names, types)
- Check for required columns
- Validate value ranges
- Handle validation errors gracefully
```

**Step 2: Implement** (30 minutes)
```
Create src/analysis/validation.py with:
- validate_schema() function
- check_required_columns() function
- validate_ranges() function
Add type hints and docstrings
```

**Step 3: Test** (15 minutes)
```
Create tests/test_validation.py with:
- Test valid data passes
- Test missing columns are caught
- Test invalid types are caught
- Test range violations are caught
```

**Step 4: Review** (10 minutes)
```
Use the code-architecture-reviewer agent to review validation.py.
Address any critical or important feedback.
```

**Step 5: Document** (10 minutes)
```
Use the documentation-architect agent to create docs/validation.md
```

**Step 6: Quality Check** (5 minutes)
```bash
uv run mypy src/
uv run ruff check .
uv run pytest --cov=src
```

**Step 7: Commit**
```bash
git add .
git commit -m "feat(validation): add CSV schema validation"
```

**Total time**: ~75 minutes for a production-ready feature with tests and docs!

---

### 8. **Trigger Skill Activation with Keywords**

Test skill activation rules by using Python-specific keywords.

**Try these prompts**:

**Data-related**:
```
"How do I load a parquet file with pandas?"
"What's the best way to handle duplicate rows in a DataFrame?"
"Show me how to merge two datasets on a common key"
```

**Testing**:
```
"Write pytest tests for a function that processes time series data"
"How do I mock pandas read_csv in my tests?"
"What fixtures should I create for testing visualization functions?"
```

**Type hints**:
```
"Add proper type hints to a function that returns a tuple of DataFrames"
"How do I annotate a function that takes variable keyword arguments?"
```

**Jupyter**:
```
"What's the recommended way to organize a data exploration notebook?"
"Should I commit notebook outputs to git?"
"How do I convert a notebook to a Python script?"
```

Each prompt should trigger the `project-guidelines` skill with relevant guidance!

---

### 9. **Test File Pattern Triggers**

Skills activate based on file patterns too. Try editing these files:

**Edit a Python module**:
```
Edit src/analysis/data.py
→ Skill activates with Python best practices
```

**Edit a test file**:
```
Edit tests/test_data.py
→ Skill activates with pytest guidance
```

**Edit a Jupyter notebook**:
```
Edit notebooks/01_example_analysis.ipynb
→ Skill activates with notebook hygiene tips
```

**Edit pyproject.toml**:
```
Edit pyproject.toml
→ Skill activates with dependency management guidance
```

---

### 10. **Progressive Disclosure: Dive Deeper**

The skill uses progressive disclosure - main guidance is ~500 lines, with detailed resources.

**Try exploring resources**:

**In your prompts, reference**:
```
"Check the testing.md resource for pytest patterns"
"What does structure.md say about organizing Python modules?"
"Show me the security.md guidelines for handling API keys in Python"
```

The skill will use those resource files to provide deeper guidance!

---

## 🎯 Success Indicators

You'll know the setup is working when:

- ✅ Skills activate automatically with relevant keywords
- ✅ Hooks suggest quality checks after editing Python files
- ✅ Agents create structured plans and reviews
- ✅ `/dev-docs` creates persistent task documentation
- ✅ Code follows Python best practices (type hints, docstrings)
- ✅ Tests pass with good coverage
- ✅ Quality checks (mypy, ruff, pytest) pass

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
