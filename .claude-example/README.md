# Jupyter Analysis Template (Python + uv)

> Example: Claude Code template customized for Python data analysis with uv and Jupyter notebooks

**This is a working example** showing how to customize the generic template for a specific tech stack.

---

## Quick Start

### Install uv and Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

cd .claude-example

# Sync dependencies (creates .venv automatically)
uv sync --all-extras

# Launch Jupyter Lab
uv run jupyter lab
```

### Run Quality Checks

```bash
uv run ruff format .      # Format code
uv run ruff check .       # Lint
uv run mypy src/          # Type check
uv run pytest             # Test
```

---

## Available Commands

- **`/dev-docs <task>`** - Create comprehensive plan, context, and task files
- **`/dev-docs-update`** - Update task docs before context compaction
- **`/handoff <purpose>`** - Create detailed handoff plan for session continuation
- **`/pickup <filename>`** - Resume work from previous handoff
- **`/make-release <version>`** - Automate repository releases
- **`/update-changelog`** - Update CHANGELOG with recent commits

---

## 🎮 Try It Out: Build a Complete Feature End-to-End

Follow this walkthrough to build a **customer segmentation** feature from planning to PR-ready. Each step demonstrates Claude Code's automation in a realistic workflow.

**Time**: ~90 minutes | **Result**: Production-ready feature with tests, docs, and quality checks

---

### Step 1: Initial Planning (5 min)

**What you'll do**: Create a strategic plan for the feature

**Prompt**:
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
- `project-guidelines` skill auto-activates
- Creates `.claude/dev/active/customer-segmentation/` with plan, context, and task files

**Verify**: Check that `.claude/dev/active/customer-segmentation/` exists with 3 markdown files

---

### Step 2: Implement Core Module (25 min)

**Prompt**:
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
- Post-tool-use hook tracks the edit

**Verify**: File exists at `src/analysis/segmentation.py` with type hints and docstrings

---

### Step 3: Add Visualization Support (15 min)

**Prompt**:
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

**Prompt**:
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

**Prompt**:
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

**Commands**:
```bash
uv run mypy src/analysis/segmentation.py
uv run ruff check src/analysis/segmentation.py tests/test_segmentation.py
uv run ruff format src/ tests/
uv run pytest tests/test_segmentation.py --cov=src/analysis/segmentation --cov-report=term-missing
```

**If issues**, ask Claude:
```
Fix the mypy errors in src/analysis/segmentation.py
```

**Verify**: All commands pass without errors, coverage >80%

---

### Step 7: Code Review (10 min)

**Prompt**:
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

**Verify**: Review feedback makes sense, critical issues fixed

---

### Step 8: Documentation (10 min)

**Prompt**:
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

### Step 9: Create Session Handoff (5 min)

**What you'll do**: Save your progress for later continuation

**Prompt**:
```
/handoff Continue testing customer segmentation feature and prepare for release
```

**What happens**:
- Claude creates detailed handoff plan in `.claude/handoffs/2025-11-16-customer-segmentation.md`
- Captures all context: files changed, decisions made, next steps
- Provides pickup instructions

**Verify**: Handoff file created in `.claude/handoffs/`

**To resume later**:
```
/pickup 2025-11-16-customer-segmentation.md
```

---

### Step 10: Update Task Docs (5 min)

**Prompt**:
```
/dev-docs-update
```

**What happens**:
- Updates `.claude/dev/active/customer-segmentation/` files
- Marks completed tasks
- Notes final status

**Verify**: Task files updated with current status

---

### Step 11: Final Integration Test (5 min)

**Commands**:
```bash
uv run pytest                    # Run all tests
uv run mypy src/                 # Type check everything
uv run ruff check .              # Lint everything
uv run jupyter lab notebooks/02_customer_segmentation.ipynb  # Try the notebook
```

**Verify**: All checks pass, notebook runs end-to-end

---

### Step 12: Prepare Release (Optional)

**If you want to version this release**:

```
/update-changelog
```

Claude will:
- Scan git commits since last release
- Add notable changes to `CHANGELOG.md` in "Unreleased" section
- Format according to conventional changelog style

Then create a release:

```
/make-release 0.2.0
```

Claude will:
- Update CHANGELOG.md to version the release
- Run release scripts (if configured)
- Create git tag
- Show push instructions

**Verify**: CHANGELOG.md updated, git tag created

---

### Step 13: Commit and Prepare PR

**Commands**:
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

# Commit
git commit -m "feat(segmentation): add customer segmentation with RFM analysis

- Add segmentation.py with RFM calculation and customer grouping
- Extend viz.py with segment distribution and RFM scatter plots
- Add comprehensive pytest tests with 85% coverage
- Create exploration notebook with examples
- Document feature in docs/customer-segmentation.md

Implements customer segmentation using RFM (Recency, Frequency, Monetary)
methodology to group customers into High Value, Regular, At Risk, and Lost
segments for targeted marketing strategies."

# Push to feature branch
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
- ✅ **Session handoff** for continuing work later
- ✅ **Release automation** with changelog and versioning
- ✅ **PR-ready commit** with conventional commit message

---

## 🎓 What You Learned

Throughout this workflow, you experienced:

1. **Skill Auto-Activation**: Skills activated when you mentioned "segmentation", "pandas", "pytest"
2. **Hook Automation**: Post-tool-use hook tracked edits and suggested quality checks
3. **Dev-Docs Pattern**: Created persistent documentation in `.claude/dev/active/`
4. **Session Management**: `/handoff` and `/pickup` for work continuity across sessions
5. **Release Automation**: `/update-changelog` and `/make-release` for versioning
6. **Quality Integration**: mypy, ruff, pytest integrated into development flow
7. **Code Review**: Expert feedback without human reviewer
8. **End-to-End Flow**: Idea to PR-ready feature in 90 minutes

---

## Resources

- **uv Documentation**: https://docs.astral.sh/uv/
- **Jupyter**: https://jupyter.org/
- **pandas**: https://pandas.pydata.org/
- **pytest**: https://docs.pytest.org/
- **mypy**: https://mypy.readthedocs.io/
- **ruff**: https://docs.astral.sh/ruff/
- **Agent Commands**: https://github.com/mitsuhiko/agent-commands

---

**This example demonstrates the Claude Code template in action with Python data analysis.** 🚀

For the generic template, see: `../README.md`
