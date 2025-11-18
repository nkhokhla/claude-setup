# Context: Project Setup

Last Updated: 2025-11-15

---

## Overview

Initial setup of a minimal, stack-agnostic Claude Code project template by extracting and adapting the Claude Code Infrastructure Showcase.

---

## Key Files Modified/Created

### Infrastructure

**`.claude/settings.json`**:
- Purpose: Hook configuration
- Content: Two hooks (UserPromptSubmit, PostToolUse)
- No Stop hooks (stack-agnostic)

**`.claude/hooks/`**:
- `skill-activation-prompt.sh` + `.ts`: Auto-suggests skills based on prompt
- `post-tool-use-tracker.sh`: Tracks edited files (simplified from showcase)
- `package.json`, `tsconfig.json`: Dependencies for TypeScript hooks

**`.claude/skills/project-guidelines/`**:
- `SKILL.md`: Main skill file (~500 lines) with TODOs
- `resources/`: 6 progressive disclosure files
  - structure.md: Architecture and file organization
  - workflows.md: CI/CD and development processes
  - testing.md: Testing strategies
  - docs.md: Documentation standards
  - release.md: Release management
  - security.md: Security best practices

**`.claude/skills/skill-rules.json`**:
- Purpose: Skill activation triggers
- Content: Conservative rules for project-guidelines
- Customizable per project

### Agents

**`.claude/agents/strategic-plan-architect.md`**:
- Purpose: Create comprehensive implementation plans
- Output: plan.md, context.md, tasks.md in .claude/dev/active/

**`.claude/agents/code-architecture-reviewer.md`**:
- Purpose: Review code for quality and best practices
- Output: code-review.md in task directory

**`.claude/agents/documentation-architect.md`**:
- Purpose: Create and update documentation
- Output: docs in appropriate locations

### Commands

**`.claude/commands/dev-docs.md`**:
- Purpose: Create structured task documentation
- Usage: `/dev-docs <task-name>`
- Output: Creates .claude/dev/active/<task>/

**`.claude/commands/dev-docs-update.md`**:
- Purpose: Update task docs before compaction
- Usage: `/dev-docs-update`

### Documentation

**`README.md`**:
- Comprehensive template guide
- Usage instructions
- Customization checklist
- Troubleshooting

**`.gitignore`**:
- Generic patterns for build artifacts, deps, logs, secrets
- Includes _showcase/

### Task Documentation

**`.claude/dev/active/project-setup/`** (this directory):
- `project-setup-plan.md`: Implementation plan
- `project-setup-context.md`: This file
- `project-setup-tasks.md`: Checklist

---

## Architectural Decisions

### 1. Stack-Agnostic Approach

**Decision**: Use TODO placeholders instead of choosing a stack

**Rationale**:
- Template should work for any language/framework
- Users fill TODOs once they choose their stack
- Avoids assumptions and bias

**Impact**:
- All skills have TODO: <placeholder> throughout
- Examples are generic or commented as needing adaptation
- Hook logic is minimal (no build detection yet)

### 2. Two Hooks Only

**Decision**: Include only UserPromptSubmit and PostToolUse hooks

**Rationale**:
- Showcase's Stop hooks (tsc-check, trigger-build-resolver) are TypeScript-specific
- Minimal hooks reduce complexity and are safe for all stacks
- Users can add Stop hooks once they know their build system

**Impact**:
- No automatic build/test triggering on Stop (yet)
- Simpler initial setup
- User must configure build tracking manually

### 3. Progressive Disclosure for Skills

**Decision**: Keep SKILL.md ~500 lines, use resource files for details

**Rationale**:
- Follows showcase pattern
- Balances completeness with readability
- Resource files allow deep dives without overwhelming main skill

**Impact**:
- Main skill is quick to read
- Resources provide comprehensive guidance when needed
- Easy to maintain and update

### 4. Generic Agents

**Decision**: Remove all stack-specific references from agents

**Rationale**:
- Agents should work across all tech stacks
- Infer stack from file types and content
- Apply universal principles (SOLID, DRY, separation of concerns)

**Impact**:
- Agents are less prescriptive initially
- Users refine agent prompts once stack is known
- Focus on architecture over language-specific details

---

## Dependencies

### Runtime

**Node.js and npm**:
- Required for: TypeScript hooks (skill-activation-prompt.ts)
- Installation: `cd .claude/hooks && npm install`
- Packages: tsx, @types/node (see .claude/hooks/package.json)

**jq**:
- Required for: JSON parsing in shell hooks
- Usually pre-installed on Linux/macOS
- Fallback: Users can simplify hooks if jq unavailable

### Development

**Git**:
- Required for: Version control
- Already available in environment

---

## Integration Points

### Hook → Skill Flow

1. User sends a prompt
2. `skill-activation-prompt.sh` runs
3. Script loads `skill-rules.json`
4. Matches prompt against keywords/patterns
5. Suggests relevant skills
6. User invokes skill (or auto-activates if configured)

### Edit → Tracking Flow

1. User edits a file with Edit/Write/MultiEdit
2. `post-tool-use-tracker.sh` runs
3. Script logs file path and timestamp
4. (Future) Script could trigger build/test commands

### Command → Agent Flow

1. User runs `/dev-docs <task>`
2. Command expands prompt for strategic-plan-architect
3. Agent creates plan, context, tasks files
4. User follows plan, updates tasks as they work
5. User runs `/dev-docs-update` before compaction

---

## Testing Strategy

**Manual Testing** (user must perform):
- [ ] Install hook dependencies: `cd .claude/hooks && npm install`
- [ ] Verify skill activates when editing `src/` files
- [ ] Test `/dev-docs` command creates task files
- [ ] Validate JSON files with `jq . .claude/settings.json`

**No Automated Tests** (template, not application):
- Template is documentation and infrastructure
- Users will add tests for their own code

---

## Performance Considerations

**Hook Performance**:
- `skill-activation-prompt.ts` runs on every prompt (fast, <100ms)
- `post-tool-use-tracker.sh` runs on every edit (fast, <50ms)
- Minimal file I/O, simple JSON parsing

**Skill Activation**:
- Conservative rules prevent over-triggering
- User can refine rules to reduce noise

---

## Security Considerations

**No Secrets in Template**:
- All TODOs clearly marked
- .gitignore includes .env and credentials
- Security.md provides best practices

**Hook Safety**:
- Hooks only read/write to .claude/ directory
- No external network calls
- No secret exposure risk

---

## Unfinished Work

None. Initial template setup is complete.

**Next steps for user**:
1. Install hook dependencies
2. Fill TODO placeholders
3. Customize for their stack
4. Add first feature with `/dev-docs`

---

## References

- **Showcase**: https://github.com/diet103/claude-code-infrastructure-showcase
- **Claude Code Docs**: https://docs.claude.com/claude-code
- **This Template**: /home/user/claude-setup
