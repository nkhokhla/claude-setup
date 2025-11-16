# Project Structure

## Overview

This document provides detailed guidance on organizing code, modules, and files within **TODO: <project-name>**.

---

## Directory Organization

### Source Code (`src/`)

TODO: Customize based on your architecture (layered, feature-based, domain-driven, etc.)

**Recommended Structure**:
```
src/
├── core/           # Core domain logic and business rules
├── services/       # Application services and orchestration
├── repositories/   # Data access layer (if applicable)
├── utils/          # Shared utilities and helpers
├── types/          # Type definitions, interfaces, schemas
├── config/         # Configuration management
└── main.ext        # Application entry point
```

**Alternative Structures**:
- **Feature-based**: Organize by feature/module (e.g., `src/users/`, `src/orders/`)
- **Layer-based**: Organize by architectural layer (e.g., `src/api/`, `src/domain/`, `src/infra/`)
- **Domain-driven**: Organize by bounded contexts (e.g., `src/billing/`, `src/inventory/`)

**Choosing an Organization**:
- Use **feature-based** for applications with clear feature boundaries
- Use **layer-based** for small to medium projects with well-defined layers
- Use **domain-driven** for complex domains with multiple bounded contexts

---

## File Naming

TODO: Define file naming conventions based on language and framework

**General Principles**:
- Use consistent casing (kebab-case, PascalCase, snake_case)
- Match file name to primary export (e.g., `UserService.ts` exports `UserService`)
- Use descriptive names that reflect content
- Group related files with prefixes (e.g., `user-service.ts`, `user-repository.ts`, `user-types.ts`)

**Examples** (TODO: adapt to your language):
- `user-service.ts`, `order-processor.ts` (kebab-case)
- `UserService.java`, `OrderProcessor.java` (PascalCase)
- `user_service.py`, `order_processor.py` (snake_case)

---

## Module Boundaries

**Principles**:
- Each module should have a single, clear responsibility
- Minimize coupling between modules
- Use dependency injection to invert dependencies
- Avoid circular dependencies

**Module Structure**:
```
module/
├── index.ext        # Public API (what's exported)
├── types.ext        # Type definitions
├── service.ext      # Business logic
├── utils.ext        # Module-specific utilities
└── tests/           # Module tests
```

---

## Dependency Management

**Rules**:
- **Explicit Dependencies**: Import only what you need
- **No Circular Deps**: Refactor to eliminate cycles
- **Layer Ordering**: Higher layers depend on lower layers, not vice versa
- **External Deps**: Keep external dependencies minimal and well-justified

**Dependency Diagram** (TODO: customize):
```
      API Layer
         ↓
    Service Layer
         ↓
   Repository Layer
         ↓
      Database
```

---

## Configuration Files

**Location**: Store config in `src/config/` or root-level config files

**Best Practices**:
- Use environment variables for deployment-specific settings
- Provide sensible defaults
- Validate configuration on startup
- Never commit secrets (use `.env` files and `.gitignore`)

**Example**:
```
TODO: <config-example>
```

---

## Testing Structure

**Test Location**: Mirror source structure in `tests/` or colocate with source

**Recommended**:
```
tests/
├── unit/           # Fast, isolated unit tests
├── integration/    # Integration tests
├── e2e/            # End-to-end tests
└── fixtures/       # Test data and mocks
```

**Alternative**: Colocate tests next to source files
```
src/
├── user-service.ts
├── user-service.test.ts
```

---

## Documentation Structure

```
docs/
├── architecture/   # Architecture decisions and diagrams
├── guides/         # How-to guides and tutorials
├── api/            # API documentation
└── decisions/      # Architecture Decision Records (ADRs)
```

---

## Anti-Patterns to Avoid

- **God Modules**: Modules that do too many things
- **Circular Dependencies**: Modules that depend on each other
- **Deep Nesting**: More than 3-4 levels of directory nesting
- **Monolithic Files**: Files over TODO: <line-limit> lines
- **Unclear Naming**: Vague names like `utils.ts`, `helpers.ts`, `common.ts`

---

**Last Updated**: 2025-11-15
