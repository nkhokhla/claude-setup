# Tasks: Project Setup

Last Updated: 2025-11-15

---

## Phase 1: Foundation ✅

- [x] Clone showcase repository to _showcase/ (Effort: S, Dependencies: none)
- [x] Create minimal directory structure (Effort: S, Dependencies: none)
- [x] Create generic .gitignore (Effort: S, Dependencies: none)

## Phase 2: Hooks and Settings ✅

- [x] Extract skill-activation-prompt hook (Effort: S, Dependencies: Phase 1)
- [x] Simplify post-tool-use-tracker hook (Effort: M, Dependencies: Phase 1)
- [x] Copy hook dependencies (package.json, tsconfig.json) (Effort: S, Dependencies: Phase 2)
- [x] Create minimal settings.json (Effort: S, Dependencies: Phase 2)
- [x] Make hooks executable (Effort: S, Dependencies: Phase 2)

## Phase 3: Skills and Rules ✅

- [x] Create project-guidelines/SKILL.md (~500 lines) (Effort: L, Dependencies: Phase 2)
- [x] Create structure.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create workflows.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create testing.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create docs.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create release.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create security.md resource (Effort: M, Dependencies: Phase 3)
- [x] Create skill-rules.json (Effort: S, Dependencies: Phase 3)

## Phase 4: Commands and Agents ✅

- [x] Adapt dev-docs.md command (Effort: S, Dependencies: Phase 3)
- [x] Adapt dev-docs-update.md command (Effort: S, Dependencies: Phase 3)
- [x] Create strategic-plan-architect agent (Effort: M, Dependencies: Phase 3)
- [x] Create code-architecture-reviewer agent (Effort: M, Dependencies: Phase 3)
- [x] Create documentation-architect agent (Effort: M, Dependencies: Phase 3)

## Phase 5: Documentation and Initial State ✅

- [x] Create comprehensive README (Effort: L, Dependencies: Phase 4)
- [x] Create project-setup-plan.md (Effort: M, Dependencies: Phase 4)
- [x] Create project-setup-context.md (Effort: M, Dependencies: Phase 4)
- [x] Create project-setup-tasks.md (this file) (Effort: S, Dependencies: Phase 4)

## Phase 6: Cleanup and Finalize ⏳

- [ ] Remove _showcase/ directory (Effort: S, Dependencies: Phase 5)
- [ ] Install hook dependencies (Effort: S, Dependencies: Phase 5)
- [ ] Validate JSON configuration (Effort: S, Dependencies: Phase 5)
- [ ] Commit all changes to git (Effort: S, Dependencies: Phase 6 tasks)

---

## User Customization Checklist (Post-Setup)

Once the template is initialized, users should:

- [ ] Replace all `TODO: <project-name>` with actual project name
- [ ] Fill in tech stack placeholders in README.md
- [ ] Update .claude/skills/project-guidelines/SKILL.md with stack details
- [ ] Refine .claude/skills/skill-rules.json with project-specific patterns
- [ ] Configure .claude/hooks/post-tool-use-tracker.sh for build system
- [ ] Add first module to src/
- [ ] Run `/dev-docs <first-feature>` for first real task
- [ ] Update LICENSE (if needed)
- [ ] Update repository URL and issue tracker

---

## Verification Checklist

Before considering template complete:

- [x] All essential files created
- [x] README comprehensive and clear
- [x] All TODO placeholders marked
- [x] No stack-specific assumptions
- [ ] Hooks executable (`chmod +x .claude/hooks/*.sh`)
- [ ] JSON files valid (run `jq . <file>.json`)
- [ ] Hook dependencies installed (`npm install` in .claude/hooks/)
- [ ] Git committed and pushed

---

## Next Immediate Action

Remove _showcase/ directory and finalize template.
