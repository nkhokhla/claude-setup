# TODO: <project-name>

> A Claude-managed project template with automated workflows, skills, and development guidelines

**Status**: 🚧 Template - Fill TODOs and customize for your project

---

## What Is This?

This is a **minimal, stack-agnostic project template** designed for use with [Claude Code](https://claude.ai/code). It includes:

- ✅ **Automated Skills**: Context-aware guidance that activates based on your code and prompts
- ✅ **Development Hooks**: Auto-tracking of edited files and intelligent skill suggestions
- ✅ **Strategic Agents**: AI agents for planning, code review, and documentation
- ✅ **Dev-Docs Pattern**: Persistent task documentation that survives context resets
- ✅ **Best Practices**: Generic guidelines for structure, testing, deployment, and security

This template is **intentionally generic** with `TODO:` placeholders throughout. You'll customize it once you choose your tech stack.

---

## Tech Stack

**Language**: TODO: <primary-language> (e.g., TypeScript, Python, Rust, Go)

**Framework**: TODO: <framework-or-runtime> (e.g., Node.js, FastAPI, Actix, Gin)

**Database**: TODO: <database-or-storage> (e.g., PostgreSQL, MongoDB, Redis)

**Testing**: TODO: <testing-framework> (e.g., Jest, pytest, cargo test)

**Build Tool**: TODO: <build-tool> (e.g., npm, cargo, poetry)

**Deployment**: TODO: <deployment-target> (e.g., Docker, AWS, Vercel, Kubernetes)

---

## Quick Start

### 1. Clone and Setup

```bash
# This repository is already cloned
cd /home/user/claude-setup

# Install dependencies (once you have a stack)
TODO: <install-command>
```

### 2. Customize the Template

**Critical TODOs to fill**:
- [ ] Replace `TODO: <project-name>` everywhere with your project name
- [ ] Replace `TODO: <short-description>` with a 1-2 sentence description
- [ ] Fill in tech stack placeholders in this README
- [ ] Update `.claude/skills/project-guidelines/SKILL.md` with your stack details
- [ ] Refine `.claude/skills/skill-rules.json` with project-specific patterns
- [ ] Configure `.claude/hooks/post-tool-use-tracker.sh` for your build system (optional)
- [ ] Update `src/` with your first module (remove any placeholder files)

**Search for TODOs**:
```bash
# Find all TODOs in the project
grep -r "TODO:" .claude/ README.md src/ docs/
```

### 3. Install Hook Dependencies

The hooks use TypeScript. Install dependencies:

```bash
cd .claude/hooks
npm install
cd ../..
```

### 4. Run Your First Dev-Docs

Create task documentation for your first feature:

```bash
# In Claude Code, run:
/dev-docs my-first-feature
```

This creates:
- `.claude/dev/active/my-first-feature/my-first-feature-plan.md`
- `.claude/dev/active/my-first-feature/my-first-feature-context.md`
- `.claude/dev/active/my-first-feature/my-first-feature-tasks.md`

---

## How It Works

### Claude Code Infrastructure

This template uses Claude Code's automation features:

#### 1. **Hooks** (`.claude/hooks/`)

**`skill-activation-prompt.sh`** (UserPromptSubmit):
- Runs every time you send a prompt
- Matches your message against skill rules
- Suggests relevant skills automatically

**`post-tool-use-tracker.sh`** (PostToolUse):
- Runs after Edit, Write, or MultiEdit tools
- Tracks which files you've edited
- Can trigger builds/tests (TODO: configure for your stack)

#### 2. **Skills** (`.claude/skills/`)

**`project-guidelines`**:
- Comprehensive development guidelines (~500 lines)
- Progressive disclosure with resource files
- Auto-activates when editing code or planning features
- Customize with your stack, conventions, and patterns

**How Skills Work**:
- Defined in `.claude/skills/project-guidelines/SKILL.md`
- Activation rules in `.claude/skills/skill-rules.json`
- Triggered by file paths, keywords, or intent patterns

#### 3. **Agents** (`.claude/agents/`)

Specialized AI agents for complex tasks:

**`strategic-plan-architect`**:
- Creates comprehensive implementation plans
- Breaks work into phases with acceptance criteria
- Outputs plan, context, and task files

**`code-architecture-reviewer`**:
- Reviews code for quality and best practices
- Questions design decisions
- Saves detailed review to task directory

**`documentation-architect`**:
- Creates and updates documentation
- Gathers context from code and existing docs
- Produces developer-focused guides

#### 4. **Commands** (`.claude/commands/`)

Slash commands for workflows:

**`/dev-docs <task-name>`**:
- Creates structured task documentation
- Generates plan, context, and checklist files
- Persists across context resets

**`/dev-docs-update`**:
- Updates task docs before compaction
- Captures session progress and decisions

---

## Project Structure

```
TODO: <project-name>/
├── src/                      # Source code (TODO: customize structure)
├── tests/                    # Tests (unit, integration, e2e)
├── docs/                     # Project documentation
├── .claude/                  # Claude Code infrastructure
│   ├── hooks/               # Automation hooks
│   │   ├── skill-activation-prompt.sh
│   │   ├── skill-activation-prompt.ts
│   │   ├── post-tool-use-tracker.sh
│   │   ├── package.json
│   │   └── tsconfig.json
│   ├── skills/              # Development guidelines
│   │   ├── project-guidelines/
│   │   │   ├── SKILL.md    # Main skill file (~500 lines)
│   │   │   └── resources/  # Progressive disclosure files
│   │   │       ├── structure.md
│   │   │       ├── workflows.md
│   │   │       ├── testing.md
│   │   │       ├── docs.md
│   │   │       ├── release.md
│   │   │       └── security.md
│   │   └── skill-rules.json
│   ├── agents/              # Strategic AI agents
│   │   ├── strategic-plan-architect.md
│   │   ├── code-architecture-reviewer.md
│   │   └── documentation-architect.md
│   ├── commands/            # Slash commands
│   │   ├── dev-docs.md
│   │   └── dev-docs-update.md
│   ├── dev/active/          # Active task documentation
│   └── settings.json        # Hook configuration
├── .gitignore
└── README.md                # This file
```

---

## Development Workflow

### 1. Plan a Feature

```bash
# Use the strategic-plan-architect agent
/dev-docs implement-authentication
```

Claude creates:
- `implement-authentication-plan.md`: Detailed implementation plan
- `implement-authentication-context.md`: Key decisions and files
- `implement-authentication-tasks.md`: Checklist for tracking progress

### 2. Implement the Feature

As you edit files:
- Hooks track your changes
- Skills auto-activate with guidance
- Follow checklist in `<task>-tasks.md`

### 3. Review the Code

Launch the code review agent:
```
Use the Task tool to launch code-architecture-reviewer
```

Agent produces: `implement-authentication-code-review.md` with findings.

### 4. Update Documentation

Launch the documentation agent:
```
Use the Task tool to launch documentation-architect
```

Agent creates/updates relevant documentation.

### 5. Before Context Compaction

```bash
/dev-docs-update
```

Updates task docs with progress, decisions, and next steps.

---

## Customization Guide

### 1. Refine Skill Rules

Edit `.claude/skills/skill-rules.json`:

```json
{
  "skills": {
    "project-guidelines": {
      "fileTriggers": {
        "pathPatterns": [
          "src/**/*.TODO:<ext>",  // Add your file extensions
          "TODO:<your-dir>/**/*"   // Add your directories
        ],
        "contentPatterns": [
          "TODO:<import-pattern>",  // e.g., "from myframework"
          "TODO:<class-pattern>"     // e.g., "class.*Service"
        ]
      },
      "promptTriggers": {
        "keywords": [
          "TODO:<domain-keyword>",   // e.g., "authentication"
          "TODO:<tech-keyword>"       // e.g., "database"
        ]
      }
    }
  }
}
```

### 2. Configure Build Tracking

Edit `.claude/hooks/post-tool-use-tracker.sh`:

Add detection for your stack:
```bash
# Example: Detect package.json and track npm builds
if [[ -f "package.json" ]]; then
  echo "npm run build" >> "$cache_dir/commands.txt"
fi
```

### 3. Update Project Guidelines

Edit `.claude/skills/project-guidelines/SKILL.md`:
- Replace all `TODO:` placeholders with actual values
- Add language-specific examples
- Document your conventions and patterns
- Add common pitfalls to avoid

### 4. Add More Skills (Optional)

Create new skills in `.claude/skills/<skill-name>/`:
- `SKILL.md`: Main guidance (~500 lines)
- `resources/`: Progressive disclosure files
- Update `skill-rules.json` to activate the skill

---

## Best Practices

### Keep Skills Concise

- Main `SKILL.md`: ~400-500 lines
- Resource files: ~100-300 lines each
- Use progressive disclosure (link to resources)

### Maintain Dev-Docs

- Run `/dev-docs <task>` for every non-trivial feature
- Run `/dev-docs-update` before context compaction
- Keep task docs up to date as you work

### Leverage Agents

- Use `strategic-plan-architect` for planning
- Use `code-architecture-reviewer` after implementation
- Use `documentation-architect` for docs

### Don't Edit Outside Claude

To preserve hook tracking and docs alignment:
- Make all code changes through Claude Code
- If you edit manually, update task docs accordingly

---

## Maintenance

### Before Context Compaction

```bash
/dev-docs-update
```

### Quarterly Review

- [ ] Review and update project guidelines
- [ ] Update dependency versions
- [ ] Refine skill rules based on actual usage
- [ ] Clean up completed tasks from `.claude/dev/active/`

### On Major Changes

- [ ] Update architecture docs
- [ ] Revise testing strategy if needed
- [ ] Update deployment workflows
- [ ] Run code review agent on refactors

---

## Troubleshooting

### Hooks Not Working

1. Check hook files are executable:
   ```bash
   ls -la .claude/hooks/
   chmod +x .claude/hooks/*.sh
   ```

2. Verify `.claude/settings.json` is valid JSON

3. Check hook dependencies installed:
   ```bash
   cd .claude/hooks && npm install
   ```

### Skills Not Activating

1. Check `.claude/skills/skill-rules.json` syntax
2. Verify file paths match your project structure
3. Test keyword triggers with your prompts

### Dev-Docs Not Created

1. Ensure `.claude/dev/active/` directory exists
2. Check command exists in `.claude/commands/dev-docs.md`
3. Verify you're using correct syntax: `/dev-docs <task-name>`

---

## Resources

- **Claude Code Docs**: [docs.claude.com/claude-code](https://docs.claude.com/claude-code)
- **Infrastructure Showcase**: [github.com/diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase)
- **Repository**: TODO: <repo-url>
- **Issue Tracker**: TODO: <issue-tracker-url>
- **Documentation**: TODO: <docs-url> (if applicable)

---

## Contributing

TODO: Add contributing guidelines if this is a team project

---

## License

TODO: <license> (e.g., MIT, Apache 2.0, Proprietary)

---

## Credits

This template was created by transforming the [Claude Code Infrastructure Showcase](https://github.com/diet103/claude-code-infrastructure-showcase) into a minimal, stack-agnostic starting point for any project using Claude Code.

**Key Changes from Showcase**:
- Removed all web/TypeScript-specific code
- Generalized skills to be language-agnostic
- Simplified hooks to two essential ones (no Stop hooks)
- Added TODO placeholders throughout for customization
- Created generic project-guidelines skill pattern
- Adapted agents to work across all stacks

---

**Last Updated**: 2025-11-15

**Template Version**: 1.0.0

**Next Steps**: Fill TODOs, choose your stack, and start building! 🚀
