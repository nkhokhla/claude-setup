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

## 🎮 Try It Out: Build a Complete Feature

Follow this walkthrough to build a **customer segmentation** feature from planning to PR-ready. Each step builds on the previous one, demonstrating Claude Code's automation in a realistic development workflow.

**Time**: ~90 minutes | **Result**: Production-ready feature with tests, docs, and quality checks

---

### Step 1: Initial Planning (5 min)

**What you'll do**: Create a strategic plan for the feature

**Prompt to use** (copy-paste this):
```
I want to add customer segmentation analysis to this project. Create a comprehensive plan.

The feature should:
- Load customer data from CSV (customer_id, purchase_amount, purchase_date, category)
- Calculate RFM metrics (Recency, Frequency, Monetary value)
- Segment customers into groups (High Value, Regular, At Risk, Lost)
- Create visualizations showing segment distributions
- Export results to a notebook for exploration

Create the plan using the strategic-plan-architect pattern: analyze current code, design the solution, break into phases with acceptance criteria, identify risks.
```

**What happens**:
- Claude Code automatically activates the `project-guidelines` skill (you'll see a message)
- Creates `.claude/dev/active/customer-segmentation/` directory
- Generates three files:
  - `customer-segmentation-plan.md` - Full implementation plan with phases
  - `customer-segmentation-context.md` - Key decisions and integration points
  - `customer-segmentation-tasks.md` - Checklist to track progress

**Verify**: Check that `.claude/dev/active/customer-segmentation/` exists with 3 markdown files

---

### Step 2: Implement Core Module (25 min)

**What you'll do**: Create the segmentation logic in `src/analysis/segmentation.py`

**Prompt to use**:
```
Following the plan in .claude/dev/active/customer-segmentation/, implement the core segmentation module.

Create src/analysis/segmentation.py with:
- calculate_rfm() function: takes DataFrame with customer_id, purchase_amount, purchase_date, returns RFM scores
- segment_customers() function: takes RFM DataFrame, returns segments (High Value, Regular, At Risk, Lost)
- get_segment_summary() function: returns statistics per segment

Use type hints, Google-style docstrings, and handle edge cases (empty data, missing columns).
```

**What happens**:
- Skill activates with Python best practices
- Claude creates `src/analysis/segmentation.py` with proper type hints
- Post-tool-use hook tracks the edit and notes commands to run later

**Verify**: File exists at `src/analysis/segmentation.py` with type hints and docstrings

---

### Step 3: Add Visualization Support (15 min)

**What you'll do**: Extend viz.py with segmentation-specific plots

**Prompt to use**:
```
Add two visualization functions to src/analysis/viz.py for customer segmentation:

1. plot_segment_distribution(segments_df, title) - bar chart showing count per segment
2. plot_rfm_scatter(rfm_df, segments_df) - 3D scatter of RFM scores colored by segment

Follow the existing patterns in viz.py (return Figure, use seaborn/matplotlib, add docstrings).
```

**What happens**:
- Skill activates (editing existing Python file)
- Claude adds functions matching existing code style
- Hook tracks the edit

**Verify**: Two new functions in `src/analysis/viz.py`

---

### Step 4: Write Tests (20 min)

**What you'll do**: Create comprehensive pytest tests

**Prompt to use**:
```
Create tests/test_segmentation.py with pytest tests for the segmentation module.

Test cases:
- test_calculate_rfm_valid_data() - RFM calculation with sample data
- test_calculate_rfm_empty_data() - handle empty DataFrame
- test_segment_customers_distribution() - verify segments are assigned correctly
- test_segment_customers_edge_cases() - single customer, all same values
- test_get_segment_summary_structure() - verify summary has expected keys

Use fixtures for sample customer data. Aim for 80%+ coverage.
```

**What happens**:
- Skill activates with pytest guidance
- Claude creates `tests/test_segmentation.py` with fixtures
- Hook suggests running `uv run pytest`

**Verify**: Tests file exists and you can run `uv run pytest tests/test_segmentation.py`

---

### Step 5: Create Exploration Notebook (15 min)

**What you'll do**: Build a Jupyter notebook demonstrating the feature

**Prompt to use**:
```
Create notebooks/02_customer_segmentation.ipynb demonstrating the customer segmentation feature.

Structure:
1. Setup: import from analysis.segmentation and analysis.viz
2. Load sample data: generate synthetic customer transactions
3. Calculate RFM: use calculate_rfm()
4. Segment: use segment_customers()
5. Visualize: use plot_segment_distribution() and plot_rfm_scatter()
6. Summary: use get_segment_summary() and interpret results

Add markdown cells explaining each step. Clear outputs before saving.
```

**What happens**:
- Skill activates with Jupyter best practices
- Claude creates working notebook with markdown explanations
- Hook reminds you to clear outputs before committing

**Verify**: Notebook at `notebooks/02_customer_segmentation.ipynb`, run it with `uv run jupyter lab`

---

### Step 6: Quality Checks (10 min)

**What you'll do**: Run all quality tools and fix any issues

**Commands to run**:
```bash
# Type checking
uv run mypy src/analysis/segmentation.py

# Linting
uv run ruff check src/analysis/segmentation.py tests/test_segmentation.py

# Formatting
uv run ruff format src/ tests/

# Tests with coverage
uv run pytest tests/test_segmentation.py --cov=src/analysis/segmentation --cov-report=term-missing
```

**If there are issues**, ask Claude:
```
Fix the mypy errors in src/analysis/segmentation.py
```
or
```
Fix the ruff linting issues in tests/test_segmentation.py
```

**Verify**: All commands pass without errors, coverage >80%

---

### Step 7: Code Review (10 min)

**What you'll do**: Get automated code review and address feedback

**Prompt to use**:
```
Review the customer segmentation implementation for code quality.

Files to review:
- src/analysis/segmentation.py
- tests/test_segmentation.py
- src/analysis/viz.py (new functions only)

Check for:
- Type safety and error handling
- Code quality and Python best practices
- Test coverage and edge cases
- Documentation completeness

Provide categorized feedback (critical/important/minor) and suggest improvements.
```

**What happens**:
- Claude analyzes your code against project guidelines
- Provides specific, actionable feedback
- You address critical/important issues

**Example fixes to request**:
```
Address the critical issues from the code review
```

**Verify**: Review feedback makes sense, critical issues fixed

---

### Step 8: Documentation (10 min)

**What you'll do**: Create user-facing documentation

**Prompt to use**:
```
Create docs/customer-segmentation.md documenting the customer segmentation feature.

Include:
- Overview: what is customer segmentation, RFM methodology
- Installation: dependencies needed (already in pyproject.toml)
- Usage: code examples for calculate_rfm(), segment_customers()
- Visualization: examples of plot functions
- Interpretation: how to understand segment results
- API Reference: all functions with parameters and returns

Use the notebook as a source of working examples.
```

**What happens**:
- Creates `docs/customer-segmentation.md`
- Includes working code examples from your implementation

**Verify**: Doc file exists and is readable

---

### Step 9: Update Task Docs (5 min)

**What you'll do**: Update the dev-docs before committing

**Prompt to use**:
```
Update the customer-segmentation dev-docs to reflect completion.

In .claude/dev/active/customer-segmentation/:
- Update context.md with final implementation decisions
- Mark completed tasks in tasks.md
- Note: "Feature complete, ready for PR" in plan.md
```

**Verify**: Task files updated with current status

---

### Step 10: Final Integration Test (5 min)

**What you'll do**: Verify everything works together

**Commands to run**:
```bash
# Run all tests
uv run pytest

# Type check everything
uv run mypy src/

# Lint everything
uv run ruff check .

# Try the notebook
uv run jupyter lab notebooks/02_customer_segmentation.ipynb
# (Run all cells, verify no errors)
```

**Verify**: All checks pass, notebook runs end-to-end

---

### Step 11: Commit and Prepare PR

**What you'll do**: Create a clean commit ready for review

**Commands to run**:
```bash
# Clear notebook outputs
jupyter nbconvert --clear-output --inplace notebooks/02_customer_segmentation.ipynb

# Stage changes
git add src/analysis/segmentation.py
git add src/analysis/viz.py
git add tests/test_segmentation.py
git add notebooks/02_customer_segmentation.ipynb
git add docs/customer-segmentation.md
git add .claude/dev/active/customer-segmentation/

# Commit with conventional message
git commit -m "feat(segmentation): add customer segmentation with RFM analysis

- Add segmentation.py with RFM calculation and customer grouping
- Extend viz.py with segment distribution and RFM scatter plots
- Add comprehensive pytest tests with 85% coverage
- Create exploration notebook with examples
- Document feature in docs/customer-segmentation.md

Implements customer segmentation using RFM (Recency, Frequency, Monetary)
methodology to group customers into High Value, Regular, At Risk, and Lost
segments for targeted marketing strategies."

# Push to feature branch (optional)
git push origin feature/customer-segmentation
```

---

## ✅ What You Built

After completing all steps, you have:

- ✅ **Core module** (`segmentation.py`) with type-safe RFM analysis
- ✅ **Visualization functions** for exploring segments
- ✅ **Comprehensive tests** with 85%+ coverage
- ✅ **Working Jupyter notebook** demonstrating the feature
- ✅ **Complete documentation** for users
- ✅ **Quality-checked code** (mypy, ruff, pytest all passing)
- ✅ **PR-ready commit** with conventional commit message
- ✅ **Persistent task docs** surviving context resets

---

## 🎓 What You Learned

Throughout this workflow, you experienced:

1. **Skill Auto-Activation**: Skills activated automatically when you mentioned "segmentation", "pandas", "pytest"
2. **Hook Automation**: Post-tool-use hook tracked your edits and suggested quality checks
3. **Dev-Docs Pattern**: Created persistent documentation in `.claude/dev/active/`
4. **Progressive Disclosure**: Skills provided just enough guidance, linking to detailed resources
5. **Quality Integration**: mypy, ruff, pytest all integrated into development flow
6. **Code Review**: Got expert feedback without needing a human reviewer
7. **End-to-End Flow**: Went from idea to PR-ready feature in 90 minutes

---

## 🚀 Try Other Scenarios

Now that you understand the flow, try these variations:

### Quick Feature (30 min)
```
Add a simple outlier detection function to src/analysis/utils.py with tests
```

### Notebook-First Exploration (45 min)
```
Create a notebook exploring correlation between purchase categories, then extract reusable functions to src/
```

### Fix a Bug (15 min)
```
The clean_data function doesn't handle duplicate indices correctly. Fix it, add a test, and commit.
```

### Extend Existing Feature (60 min)
```
Add time-series support to the segmentation module: track how customers move between segments over time
```

Each follows the same pattern: plan → implement → test → quality check → document → commit

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
