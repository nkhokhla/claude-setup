---
name: project-guidelines
description: Comprehensive project development guidelines for TODO: <project-name>. Use when creating features, refactoring code, implementing tests, setting up CI/CD, writing documentation, or working with TODO: <primary-language>. Covers project structure, coding standards, testing patterns, deployment workflows, and best practices. Automatically activates when working on core project files or when planning, architecting, testing, or documenting features.
---

# Project Guidelines

## Purpose

Establish consistency, quality, and best practices across all development work for **TODO: <project-name>**.

## When to Use This Skill

Automatically activates when working on:
- Creating or modifying source code in `src/`
- Planning features or architecture
- Implementing tests and quality checks
- Writing or updating documentation
- Setting up CI/CD and automation
- Refactoring or optimizing code

---

## Quick Start

### New Feature Checklist

- [ ] **Plan**: Review requirements and acceptance criteria
- [ ] **Design**: Consider architecture and integration points
- [ ] **Implement**: Write clean, maintainable code following project standards
- [ ] **Test**: Add unit/integration tests with good coverage
- [ ] **Document**: Update README, code comments, and dev-docs
- [ ] **Review**: Run quality checks (TODO: <linting-command>, TODO: <type-check-command>)
- [ ] **Commit**: Use conventional commit messages
- [ ] **Deploy**: Follow deployment workflow (see [release.md](resources/release.md))

### New Project Setup Checklist

- [ ] Clone this template repository
- [ ] Replace all TODO placeholders with project-specific values
- [ ] Choose your tech stack and update dependencies (TODO: <package-manager>)
- [ ] Configure testing framework (TODO: <testing-framework>)
- [ ] Set up CI/CD pipeline (see [workflows.md](resources/workflows.md))
- [ ] Refine `.claude/skills/skill-rules.json` with project-specific patterns
- [ ] Run `/dev-docs project-setup` to create initial task documentation
- [ ] Remove example code from `src/` and add your first module
- [ ] Update README.md with project description and setup instructions

---

## Project Overview

**Project Name**: TODO: <project-name>

**Description**: TODO: <short-description>

**Primary Language**: TODO: <primary-language>

**Tech Stack**:
- TODO: <framework-or-runtime>
- TODO: <database-or-storage>
- TODO: <testing-framework>
- TODO: <build-tool>
- TODO: <deployment-target>

**Key Features**:
- TODO: <feature-1>
- TODO: <feature-2>
- TODO: <feature-3>

---

## Architecture Overview

### Directory Structure

```
TODO: <project-name>/
├── src/                 # Source code (TODO: customize structure)
│   ├── core/           # Core business logic
│   ├── services/       # Service layer
│   ├── utils/          # Utilities and helpers
│   ├── types/          # Type definitions (if applicable)
│   └── config/         # Configuration management
├── tests/              # Test files (unit, integration, e2e)
├── docs/               # Project documentation
├── .claude/            # Claude Code infrastructure
│   ├── hooks/         # Automation hooks
│   ├── skills/        # Development guidelines and skills
│   ├── agents/        # Specialized AI agents
│   ├── commands/      # Slash commands for workflows
│   └── dev/active/    # Active task documentation
├── scripts/            # Build and deployment scripts
├── TODO: <config-files># Configuration (package.json, Cargo.toml, etc.)
└── README.md           # Project overview

```

**Key Principles**:
- **Separation of Concerns**: Each module has a single, well-defined responsibility
- **Modularity**: Code is organized into reusable, testable units
- **Clarity**: Names and structure reflect intent and domain concepts
- **Maintainability**: Optimize for readability and long-term maintenance

See [structure.md](resources/structure.md) for complete architectural details.

---

## Coding Standards

### General Principles

1. **Readability First**: Code is read far more often than written
2. **Explicit Over Implicit**: Favor clarity over cleverness
3. **Fail Fast**: Validate inputs and assumptions early
4. **No Magic**: Avoid obscure patterns or hidden behaviors
5. **DRY**: Don't Repeat Yourself, but avoid premature abstraction

### Naming Conventions

TODO: Customize based on language conventions

**General Guidelines**:
- Use descriptive names that reveal intent
- Avoid abbreviations unless universally recognized
- Be consistent with casing (camelCase, PascalCase, snake_case, UPPER_SNAKE_CASE)
- Name functions as actions (verbs): `getUserById`, `calculate_total`, `parse_input`
- Name classes/types as nouns: `UserService`, `OrderProcessor`, `ConfigManager`
- Name constants with semantic meaning: `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`

**Examples** (TODO: adapt to your language):
```
TODO: <language-specific-examples>
// Functions: camelCase (JavaScript/TypeScript)
function processPayment() { }
async function fetchUserData() { }

// Classes: PascalCase
class UserRepository { }
class PaymentProcessor { }

// Constants: UPPER_SNAKE_CASE
const MAX_CONNECTIONS = 10;
const API_BASE_URL = "https://api.example.com";

// Variables: camelCase
const userId = 123;
let isAuthenticated = false;
```

### Code Organization

- **File Length**: Keep files focused and under TODO: <line-limit> lines
- **Function Length**: Aim for TODO: <function-line-limit> lines per function; extract helpers for complex logic
- **Indentation**: TODO: <indentation-style> (e.g., 2 spaces, 4 spaces, tabs)
- **Line Length**: TODO: <line-length-limit> characters maximum
- **Imports**: Group and sort imports logically (stdlib → external → internal)

### Error Handling

- **Explicit Errors**: Return errors explicitly or throw typed exceptions
- **Context**: Include context in error messages (what failed, why, where)
- **Recovery**: Handle expected errors gracefully; fail fast on unexpected errors
- **Logging**: Log errors with appropriate severity levels

TODO: Add language-specific error handling patterns

### Type Safety (if applicable)

- **Strict Mode**: Enable strict type checking (TODO: <type-system>)
- **No `any`**: Avoid escape hatches; use proper types or generics
- **Null Safety**: Handle null/undefined explicitly
- **Type Inference**: Let the compiler infer when obvious, annotate when helpful

### Comments and Documentation

- **Why, Not What**: Explain the reasoning behind non-obvious decisions
- **Public APIs**: Document all public interfaces, parameters, and return values
- **TODOs**: Mark temporary code with `TODO:` and context
- **Examples**: Include usage examples for complex APIs

---

## Testing Strategy

### Testing Pyramid

```
       /\
      /E2E\      ← Few, critical user flows (TODO: <e2e-tool>)
     /------\
    /Integr.\   ← Moderate, test component interactions
   /----------\
  /Unit Tests \  ← Many, fast, isolated tests
 /--------------\
```

### Test Coverage Goals

- **Unit Tests**: TODO: <coverage-target>% minimum coverage
- **Integration Tests**: Cover all major workflows
- **E2E Tests**: Cover critical user journeys

### Writing Good Tests

- **Arrange-Act-Assert**: Structure tests clearly
- **One Assertion**: Focus each test on a single behavior
- **Descriptive Names**: Test names describe the scenario and expected outcome
- **Fast**: Unit tests should run in milliseconds
- **Isolated**: Tests should not depend on each other or external state
- **Repeatable**: Same inputs always produce same outputs

**Test Naming Pattern**: `test_<what>_<condition>_<expected>` or `should_<expected>_when_<condition>`

TODO: Add language-specific testing examples

See [testing.md](resources/testing.md) for detailed testing guide.

---

## Git Workflow

### Branching Strategy

- **Main Branch**: `main` or `master` (production-ready code)
- **Feature Branches**: `feature/<description>` or `<username>/<description>`
- **Bugfix Branches**: `fix/<issue-number>-<description>`
- **Release Branches**: `release/<version>` (if applicable)

### Commit Messages

Follow **Conventional Commits** format:

```
<type>(<scope>): <short description>

<optional body>

<optional footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring (no behavior change)
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (deps, config, etc.)
- `perf`: Performance improvements
- `style`: Code style changes (formatting, whitespace)

**Examples**:
```
feat(auth): add JWT token validation
fix(api): handle timeout errors gracefully
docs(readme): update installation instructions
refactor(core): simplify error handling logic
```

### Pull Request Guidelines

- **Title**: Use conventional commit format
- **Description**: Explain what changed and why
- **Tests**: Include tests for new functionality
- **Documentation**: Update docs if APIs or behavior changed
- **Review**: Request review from at least TODO: <required-reviewers> team member(s)
- **CI**: Ensure all CI checks pass before merging

---

## Development Workflows

### Local Development

1. **Setup**: `TODO: <install-command>` (e.g., `npm install`, `pip install -r requirements.txt`)
2. **Run**: `TODO: <run-command>` (e.g., `npm start`, `python main.py`)
3. **Test**: `TODO: <test-command>` (e.g., `npm test`, `pytest`)
4. **Lint**: `TODO: <lint-command>` (e.g., `npm run lint`, `ruff check`)
5. **Build**: `TODO: <build-command>` (e.g., `npm run build`, `cargo build`)

### CI/CD Pipeline

TODO: Configure CI/CD (GitHub Actions, GitLab CI, CircleCI, etc.)

**Pipeline Stages**:
1. **Lint**: Check code style and formatting
2. **Test**: Run unit and integration tests
3. **Build**: Compile/bundle the application
4. **Deploy**: Deploy to TODO: <deployment-target> (staging/production)

See [workflows.md](resources/workflows.md) for detailed CI/CD configuration.

---

## Deployment

**Deployment Target**: TODO: <deployment-target>

**Deployment Process**:
1. Merge feature branch to `main` via pull request
2. CI runs tests and builds artifacts
3. TODO: <deployment-steps>
4. Monitor for errors and rollback if needed

**Environment Variables**: Store in `.env` files (never commit secrets!)

See [release.md](resources/release.md) for release management details.

---

## Security Best Practices

- **Input Validation**: Validate and sanitize all external inputs
- **Secrets Management**: Use environment variables or secret managers (never hardcode)
- **Dependencies**: Keep dependencies updated; scan for vulnerabilities
- **Least Privilege**: Grant minimum necessary permissions
- **Logging**: Log security events; never log secrets or PII

See [security.md](resources/security.md) for complete security guidelines.

---

## Documentation Standards

### Code Documentation

- **Public APIs**: Document all public functions/classes
- **Parameters**: Describe each parameter's type, purpose, and constraints
- **Return Values**: Document what the function returns
- **Exceptions**: List exceptions that can be thrown
- **Examples**: Include usage examples for complex APIs

### Project Documentation

- **README.md**: Project overview, setup, and quick start
- **docs/**: Detailed guides, architecture, and design decisions
- **.claude/dev/active/**: Active task plans, context, and progress tracking
- **CHANGELOG.md**: Track changes between versions (TODO: if applicable)

### Dev-Docs Pattern

Use `/dev-docs <task-name>` to create persistent task documentation:
- `<task-name>-plan.md`: Comprehensive implementation plan
- `<task-name>-context.md`: Key decisions, files, and dependencies
- `<task-name>-tasks.md`: Checklist for tracking progress

Update docs with `/dev-docs-update` before context compaction.

See [docs.md](resources/docs.md) for documentation guidelines.

---

## Claude Code Integration

This project uses Claude Code infrastructure for automated development assistance.

### Hooks

- **UserPromptSubmit**: Suggests relevant skills based on your prompt
- **PostToolUse**: Tracks edited files for build/test automation (TODO: configure)

### Skills

Skills provide context-aware guidance. This `project-guidelines` skill activates automatically when:
- Editing files in `src/`, `docs/`, `.claude/commands/`
- Using keywords: plan, architecture, guidelines, release, testing, docs
- TODO: Add project-specific keywords to `.claude/skills/skill-rules.json`

### Agents

- **strategic-plan-architect**: Creates comprehensive plans for features/refactors
- **code-architecture-reviewer**: Reviews code for quality and adherence to guidelines
- **documentation-architect**: Creates and updates project documentation

### Commands

- `/dev-docs <task>`: Create structured task documentation (plan, context, tasks)
- `/dev-docs-update`: Update task docs before context compaction

---

## Progressive Disclosure Resources

For detailed guidance on specific topics, see:

- [structure.md](resources/structure.md): Detailed architecture and file organization
- [workflows.md](resources/workflows.md): CI/CD, automation, and development workflows
- [testing.md](resources/testing.md): Comprehensive testing strategies and examples
- [docs.md](resources/docs.md): Documentation standards and templates
- [release.md](resources/release.md): Release management and versioning
- [security.md](resources/security.md): Security best practices and checklists

---

## Common Patterns

TODO: Add project-specific patterns as they emerge

**Pattern Template**:
```
### Pattern Name

**Use Case**: When to use this pattern

**Example**:
<code example>

**Rationale**: Why this approach is preferred

**Gotchas**: Common mistakes to avoid
```

---

## Troubleshooting

TODO: Add common issues and solutions as they're discovered

**Common Issues**:
- Issue 1: TODO: <description> → Solution: TODO: <fix>
- Issue 2: TODO: <description> → Solution: TODO: <fix>

---

## References

- Project Repository: TODO: <repo-url>
- Issue Tracker: TODO: <issue-tracker-url>
- Documentation Site: TODO: <docs-url> (if applicable)
- Team Communication: TODO: <slack-discord-etc>

---

**Last Updated**: 2025-11-15

**Version**: 1.0.0

**Next Review**: TODO: <review-date>
