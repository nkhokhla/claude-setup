# Implementation Plan: Project Setup

Last Updated: 2025-11-15

## Executive Summary

**What**: Transform Claude Code Infrastructure Showcase into a minimal, stack-agnostic project template

**Why**: Provide a reusable starting point for any project using Claude Code, without web/TypeScript assumptions

**How**: Extract essential infrastructure (hooks, skills, agents, commands), generalize to be stack-agnostic, add TODO placeholders

**Timeline**: Initial setup complete; ongoing customization as stack is chosen

---

## Current State Analysis

**Starting Point**: Empty repository (claude-setup)

**Showcase Source**: https://github.com/diet103/claude-code-infrastructure-showcase

**Infrastructure to Extract**:
- Hooks: skill-activation-prompt, post-tool-use-tracker
- Skills pattern: Progressive disclosure with SKILL.md + resources
- Commands: dev-docs, dev-docs-update
- Agents: strategic-plan-architect, code-architecture-reviewer, documentation-architect

**Not Extracted** (stack-specific):
- Stop hooks (tsc-check, trigger-build-resolver)
- Frontend/backend-specific skills
- Monorepo-specific patterns
- Web-specific agents

---

## Proposed Future State

**Target Architecture**:
- Minimal directory structure (src/, docs/, .claude/, tests/)
- Two essential hooks (UserPromptSubmit, PostToolUse)
- Generic project-guidelines skill with progressive disclosure
- Three stack-agnostic agents
- Dev-docs commands for task persistence
- Comprehensive README with usage instructions

**Success Criteria**:
- All infrastructure files created and functional
- All TODO placeholders clearly marked
- README provides complete usage guide
- Template can be customized for any tech stack
- No stack-specific assumptions in core files

---

## Implementation Phases

### Phase 1: Foundation ✅
- [x] Clone showcase repository to _showcase/
- [x] Create minimal directory structure
- [x] Create generic .gitignore

### Phase 2: Hooks and Settings ✅
- [x] Extract skill-activation-prompt hook (shell + TypeScript)
- [x] Simplify post-tool-use-tracker hook (remove monorepo logic)
- [x] Copy hook dependencies (package.json, tsconfig.json)
- [x] Create minimal settings.json (only two hooks, no Stop hooks)
- [x] Make hooks executable

### Phase 3: Skills and Rules ✅
- [x] Create project-guidelines skill (~500 lines)
- [x] Create 6 progressive disclosure resource files
  - structure.md
  - workflows.md
  - testing.md
  - docs.md
  - release.md
  - security.md
- [x] Create skill-rules.json with conservative activation triggers
- [x] Add TODO placeholders throughout skill files

### Phase 4: Commands and Agents ✅
- [x] Adapt dev-docs.md command (generic version)
- [x] Adapt dev-docs-update.md command
- [x] Create strategic-plan-architect agent
- [x] Create code-architecture-reviewer agent
- [x] Create documentation-architect agent
- [x] Remove stack-specific references from agents

### Phase 5: Documentation and Initial State ✅
- [x] Create comprehensive README with usage instructions
- [x] Add "How It Works" section explaining infrastructure
- [x] Add customization guide
- [x] Add troubleshooting section
- [x] Create project-setup dev-docs (this file)

### Phase 6: Cleanup and Finalize ⏳
- [ ] Remove _showcase/ directory
- [ ] Verify all hook dependencies installed
- [ ] Validate JSON files (.claude/settings.json, skill-rules.json)
- [ ] Test skill activation (verify rules work)
- [ ] Commit all changes to git

---

## Detailed Task Breakdown

### Cleanup (In Progress)

**Task 1: Remove Showcase Directory**
- Effort: S
- Dependencies: None (extraction complete)
- Acceptance Criteria: _showcase/ deleted, .gitignore includes it

**Task 2: Install Hook Dependencies**
- Effort: S
- Dependencies: None
- Command: `cd .claude/hooks && npm install`
- Acceptance Criteria: node_modules/ exists, hooks can run

**Task 3: Validate Configuration**
- Effort: S
- Dependencies: None
- Acceptance Criteria:
  - .claude/settings.json is valid JSON
  - .claude/skills/skill-rules.json is valid JSON
  - All hook scripts have execute permissions

**Task 4: Initial Git Commit**
- Effort: S
- Dependencies: Tasks 1-3
- Acceptance Criteria:
  - All template files committed
  - Commit message: "chore: initialize minimal template from showcase"
  - Pushed to remote branch

---

## Risk Assessment

### Technical Risks

**Risk 1: Hook Dependencies Unavailable**
- **Likelihood**: Low
- **Impact**: Medium (hooks won't run)
- **Mitigation**: Include package.json and clear install instructions

**Risk 2: Skills Don't Activate**
- **Likelihood**: Medium
- **Impact**: Low (users can invoke manually)
- **Mitigation**: Conservative activation rules, clear documentation

**Risk 3: TODOs Left Unfilled**
- **Likelihood**: High (intentional)
- **Impact**: Low (expected for template)
- **Mitigation**: Clear grep command in README to find all TODOs

---

## Success Metrics

- [x] All essential infrastructure files created
- [x] README provides complete usage guide
- [x] No stack-specific assumptions in core files
- [x] All TODO placeholders clearly marked
- [ ] Hooks functional (after npm install)
- [ ] Template ready for customization

---

## Required Resources

**Dependencies**:
- Node.js and npm (for hook TypeScript execution)
- jq (for JSON parsing in hooks)
- Git (for version control)

**External Services**: None

**Documentation References**:
- Claude Code docs: https://docs.claude.com/claude-code
- Showcase repo: https://github.com/diet103/claude-code-infrastructure-showcase

---

## Timeline Estimates

**Total Effort**: ~2 hours for initial template creation

**Breakdown**:
- Phase 1: 10 minutes ✅
- Phase 2: 15 minutes ✅
- Phase 3: 45 minutes ✅
- Phase 4: 30 minutes ✅
- Phase 5: 20 minutes ✅
- Phase 6: 10 minutes ⏳

**Ongoing**: Customization by user once stack is chosen

---

## Next Steps

1. Remove _showcase/ directory
2. Install hook dependencies
3. Validate all JSON configuration
4. Commit template to git
5. User: Fill TODOs and customize for their stack
