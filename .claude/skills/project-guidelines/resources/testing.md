# Testing Guide

## Overview

Comprehensive testing strategies and best practices for **TODO: <project-name>**.

---

## Testing Philosophy

**Goals**:
- Ensure correctness and prevent regressions
- Enable confident refactoring
- Document expected behavior
- Catch bugs early in development

**Principles**:
- Write tests first (TDD) or alongside code
- Keep tests fast, isolated, and repeatable
- Test behavior, not implementation
- Aim for TODO: <coverage-target>% code coverage

---

## Testing Pyramid

```
       /\
      /E2E\      ← Few (5-10%), slow, brittle
     /------\
    /Integr.\   ← Some (20-30%), moderate speed
   /----------\
  /Unit Tests \  ← Many (60-75%), fast, isolated
 /--------------\
```

**Balance**:
- **Unit Tests**: Majority of tests, fast feedback
- **Integration Tests**: Verify component interactions
- **E2E Tests**: Critical user journeys only

---

## Unit Testing

### What to Test

- Individual functions and methods
- Edge cases and boundary conditions
- Error handling and validation
- Business logic and calculations

### Writing Unit Tests

**Framework**: TODO: <testing-framework> (e.g., Jest, pytest, JUnit, cargo test)

**Structure**: Arrange-Act-Assert (AAA)
```
TODO: <language-specific-example>

// Example (JavaScript/Jest)
test('should calculate total price with tax', () => {
  // Arrange
  const price = 100;
  const taxRate = 0.1;

  // Act
  const total = calculateTotal(price, taxRate);

  // Assert
  expect(total).toBe(110);
});
```

**Best Practices**:
- One assertion per test (or closely related assertions)
- Descriptive test names: `test_<what>_<condition>_<expected>`
- Test both happy path and error cases
- Use test fixtures and factories for test data
- Avoid testing implementation details

### Mocking and Stubbing

**When to Mock**:
- External APIs and services
- Database connections
- File system operations
- Time-dependent code

**Example** (TODO: adapt to your framework):
```
TODO: <mocking-example>
```

---

## Integration Testing

### What to Test

- Database interactions
- API endpoints and routes
- Service-to-service communication
- Configuration and initialization

### Writing Integration Tests

**Example** (TODO: adapt to your stack):
```
TODO: <integration-test-example>
```

**Best Practices**:
- Use test databases or in-memory stores
- Clean up test data after each test
- Test realistic workflows and scenarios
- Verify side effects (database writes, API calls)

---

## End-to-End Testing

### What to Test

- Critical user journeys (signup, checkout, etc.)
- Cross-browser compatibility (if web app)
- Mobile responsiveness (if applicable)
- Production-like environment

### E2E Testing Tools

TODO: Choose and configure (Playwright, Cypress, Selenium, etc.)

**Example** (TODO: adapt to your tool):
```
TODO: <e2e-test-example>
```

**Best Practices**:
- Keep E2E tests minimal (slow and brittle)
- Run E2E tests in CI on every PR
- Use page object pattern for maintainability
- Test against staging environment

---

## Test Coverage

### Coverage Goals

- **Unit Tests**: TODO: <unit-coverage-target>% minimum
- **Integration Tests**: Cover all major workflows
- **E2E Tests**: Cover critical user paths

### Measuring Coverage

**Tool**: TODO: <coverage-tool> (e.g., Istanbul/nyc, coverage.py, JaCoCo)

**Command**:
```bash
TODO: <coverage-command>
```

**Interpreting Coverage**:
- 100% coverage doesn't guarantee bug-free code
- Focus on testing critical paths and edge cases
- Uncovered code may indicate dead code or missing tests

---

## Test Data Management

### Fixtures

Create reusable test data:
```
TODO: <fixture-example>
```

### Factories

Generate test data programmatically:
```
TODO: <factory-example>
```

### Database Seeding

For integration tests, seed database with known state:
```
TODO: <seeding-example>
```

---

## Performance Testing

### Load Testing

TODO: Configure load testing (k6, JMeter, Locust, etc.)

**Example**:
```
TODO: <load-test-example>
```

### Benchmarking

Measure performance of critical functions:
```
TODO: <benchmark-example>
```

---

## Continuous Testing

### Running Tests Locally

```bash
# Run all tests
TODO: <test-command>

# Run specific test file
TODO: <test-file-command>

# Run tests in watch mode
TODO: <test-watch-command>

# Run with coverage
TODO: <coverage-command>
```

### Running Tests in CI

See [workflows.md](workflows.md) for CI/CD configuration.

**Required Checks**:
- All unit tests pass
- Integration tests pass
- Coverage meets threshold
- No failing E2E tests

---

## Debugging Failing Tests

### Strategies

1. **Read the Error**: Understand what failed and why
2. **Isolate the Test**: Run the failing test in isolation
3. **Add Logging**: Print intermediate values
4. **Use Debugger**: Step through code with breakpoints
5. **Check Assumptions**: Verify test setup and expectations

### Common Issues

- **Flaky Tests**: Tests that pass/fail intermittently (usually timing or state issues)
- **Brittle Tests**: Tests that break on minor changes (testing implementation)
- **Slow Tests**: Tests that take too long (I/O, network, or inefficient code)

**Fixes**:
- Flaky: Add proper waits, fix race conditions, isolate state
- Brittle: Test behavior, not implementation details
- Slow: Mock expensive operations, optimize test setup

---

## Testing Checklist

Before merging code:
- [ ] All tests pass locally
- [ ] New features have unit tests
- [ ] Integration tests cover new workflows
- [ ] Coverage meets project threshold
- [ ] No skipped or disabled tests without justification
- [ ] Tests are fast (unit tests < TODO: <unit-test-time-limit>ms)

---

**Last Updated**: 2025-11-15
