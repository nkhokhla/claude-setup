# TODO: <project-name>

> A Claude Code template with automated workflows, skills, and development guidelines

**Status**: 🚧 Template - Fill TODOs and customize for your project

---

## What Is This?

A **minimal, stack-agnostic project template** for [Claude Code](https://claude.ai/code) featuring:

- ✅ **Automated Skills**: Context-aware guidance based on your code and prompts
- ✅ **Development Hooks**: Auto-tracking of edited files and skill suggestions
- ✅ **Strategic Agents**: AI agents for planning, code review, and documentation
- ✅ **Dev-Docs Pattern**: Persistent task documentation that survives context resets
- ✅ **Session Management**: Handoff/pickup commands for continuing work across sessions
- ✅ **Best Practices**: Generic guidelines for structure, testing, deployment, and security

---

## 📚 See It In Action

**Want to see a complete example?** Check out `.claude-example/` for a fully customized version using **Python 3.12+**, **uv**, and **Jupyter notebooks** with all TODOs filled in.

[View the Python/Jupyter example →](.claude-example/README.md)

---

## Quick Start

### 1. Customize the Template

Replace these TODOs throughout the project:
- [ ] `TODO: <project-name>` - Your project name
- [ ] `TODO: <short-description>` - Brief description
- [ ] Tech stack placeholders in this README
- [ ] `.claude/skills/project-guidelines/SKILL.md` with your stack details
- [ ] `.claude/skills/skill-rules.json` with project-specific patterns

**Search for TODOs**:
```bash
grep -r "TODO:" .claude/ README.md
```

### 2. Install Hook Dependencies

```bash
cd .claude/hooks
npm install
cd ../..
```

### 3. Start Building

Use Claude Code commands:
- `/dev-docs <task-name>` - Create structured task documentation
- `/handoff <purpose>` - Save session context for later
- `/pickup <filename>` - Resume from a handoff
- `/make-release <version>` - Automate releases
- `/update-changelog` - Update CHANGELOG.md

---

## Available Commands

- **`/dev-docs <task>`** - Create comprehensive plan, context, and task files
- **`/dev-docs-update`** - Update task docs before context compaction
- **`/handoff <purpose>`** - Create detailed handoff plan for session continuation
- **`/pickup <filename>`** - Resume work from previous handoff
- **`/make-release <version>`** - Automate repository releases
- **`/update-changelog`** - Update CHANGELOG with recent commits

---

## Project Structure

```
├── src/                      # Source code (customize for your stack)
├── tests/                    # Tests
├── docs/                     # Documentation
├── .claude/
│   ├── hooks/               # Automation hooks
│   ├── skills/              # Development guidelines
│   │   ├── project-guidelines/
│   │   └── web-browser/     # Browser automation skill
│   ├── agents/              # Strategic AI agents
│   ├── commands/            # Slash commands
│   │   ├── dev-docs.md
│   │   ├── handoff.md
│   │   ├── pickup.md
│   │   ├── make-release.md
│   │   └── update-changelog.md
│   ├── handoffs/            # Session handoff files (gitignored)
│   └── dev/active/          # Active task documentation
└── README.md
```

---

## Development Workflow

### Plan a Feature
```bash
/dev-docs implement-authentication
```

Creates plan, context, and task files in `.claude/dev/active/`

### Work Across Sessions
```bash
# Before ending session
/handoff "Continue implementing authentication"

# In new session
/pickup 2025-11-16-implement-auth.md
```

### Make a Release
```bash
/update-changelog
/make-release 1.0.0
```

---

## Resources

- **Claude Code Docs**: [docs.claude.com/claude-code](https://docs.claude.com/claude-code)
- **Full Example**: [.claude-example/README.md](.claude-example/README.md)
- **Agent Commands**: Based on [mitsuhiko/agent-commands](https://github.com/mitsuhiko/agent-commands)

---

## License

TODO: <license> (e.g., MIT, Apache 2.0)

---

**Last Updated**: 2025-11-16 | **Template Version**: 1.0.0
