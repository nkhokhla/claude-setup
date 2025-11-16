# Security Best Practices

## Overview

Security guidelines and best practices for **TODO: <project-name>**.

---

## Security Principles

### Core Tenets

1. **Defense in Depth**: Multiple layers of security
2. **Least Privilege**: Grant minimum necessary permissions
3. **Fail Securely**: Default to secure state on failure
4. **Never Trust Input**: Validate and sanitize all external input
5. **Keep Secrets Secret**: Never expose credentials or sensitive data

---

## Input Validation

### Validate All External Input

**Sources of External Input**:
- User input (forms, API requests)
- File uploads
- Query parameters
- HTTP headers
- Environment variables
- Third-party APIs

**Validation Rules**:
- **Type**: Ensure correct data type (string, number, boolean)
- **Format**: Validate format (email, URL, phone number)
- **Range**: Check min/max values, length limits
- **Whitelist**: Allow only known-good values
- **Sanitize**: Remove or escape dangerous characters

**Example** (TODO: adapt to your language):
```
TODO: <validation-example>

// Bad: No validation
function getUser(id) {
  return db.query(`SELECT * FROM users WHERE id = ${id}`);  // SQL injection!
}

// Good: Parameterized query
function getUser(id) {
  if (!Number.isInteger(id) || id <= 0) {
    throw new Error('Invalid user ID');
  }
  return db.query('SELECT * FROM users WHERE id = ?', [id]);
}
```

---

## Authentication and Authorization

### Authentication

**Best Practices**:
- Use established libraries (TODO: <auth-library>)
- Hash passwords with strong algorithms (bcrypt, Argon2)
- Implement rate limiting on login attempts
- Use multi-factor authentication (MFA) for sensitive operations
- Enforce strong password policies

**Example**:
```
TODO: <auth-example>
```

### Authorization

**Principles**:
- Verify permissions on every request
- Implement role-based access control (RBAC)
- Follow least privilege principle
- Never trust client-side authorization

**Example**:
```
TODO: <authz-example>
```

### Session Management

- Use secure, httpOnly cookies for session tokens
- Set appropriate session timeouts
- Regenerate session IDs after login
- Implement logout functionality
- Use CSRF tokens for state-changing operations

---

## Secrets Management

### Never Hardcode Secrets

**Secrets Include**:
- API keys
- Database passwords
- Encryption keys
- Private keys
- OAuth client secrets

### Use Environment Variables

```bash
# .env file (NEVER commit this!)
DATABASE_URL=postgres://user:pass@localhost/db
API_KEY=secret-key-here
JWT_SECRET=random-string-here
```

**Loading**:
```
TODO: <env-loading-example>
```

### Secure Storage

**Options**:
- **Development**: `.env` files (gitignored)
- **Production**: Secret managers (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault)
- **CI/CD**: GitHub Secrets, GitLab CI/CD variables

### Secret Rotation

- Rotate secrets periodically (e.g., every 90 days)
- Rotate immediately if compromised
- Use short-lived tokens when possible

---

## Data Protection

### Encryption

**Encrypt Data At Rest**:
- Sensitive user data (PII, financial info)
- Backups and archives
- Database fields with sensitive data

**Encrypt Data In Transit**:
- Use HTTPS/TLS for all connections
- Use TLS 1.2 or higher
- Verify SSL certificates

**Example**:
```
TODO: <encryption-example>
```

### Data Minimization

- Collect only necessary data
- Anonymize or pseudonymize when possible
- Delete data when no longer needed
- Implement data retention policies

---

## Common Vulnerabilities (OWASP Top 10)

### 1. Injection (SQL, NoSQL, Command)

**Prevention**:
- Use parameterized queries or ORMs
- Validate and sanitize input
- Avoid dynamic query construction

### 2. Broken Authentication

**Prevention**:
- Use strong password policies
- Implement MFA
- Rate limit login attempts
- Secure session management

### 3. Sensitive Data Exposure

**Prevention**:
- Encrypt sensitive data
- Use HTTPS everywhere
- Don't log secrets or PII
- Implement proper access controls

### 4. XML External Entities (XXE)

**Prevention**:
- Disable XML external entity processing
- Use less complex data formats (JSON)
- Validate and sanitize XML input

### 5. Broken Access Control

**Prevention**:
- Verify authorization on every request
- Implement RBAC or ABAC
- Default deny access
- Test authorization logic thoroughly

### 6. Security Misconfiguration

**Prevention**:
- Use secure defaults
- Disable unnecessary features
- Keep dependencies updated
- Review security settings regularly

### 7. Cross-Site Scripting (XSS)

**Prevention**:
- Escape output (HTML, JavaScript, CSS)
- Use Content Security Policy (CSP)
- Sanitize user input
- Use frameworks with auto-escaping

**Example**:
```
TODO: <xss-prevention-example>
```

### 8. Insecure Deserialization

**Prevention**:
- Validate deserialized data
- Use simple data formats (JSON)
- Implement integrity checks
- Avoid deserializing untrusted data

### 9. Using Components with Known Vulnerabilities

**Prevention**:
- Keep dependencies updated
- Use dependency scanning tools (Dependabot, Snyk)
- Monitor security advisories
- Remove unused dependencies

**Tools**:
```bash
TODO: <dependency-scan-command>
```

### 10. Insufficient Logging and Monitoring

**Prevention**:
- Log security events (login, logout, failures)
- Monitor for suspicious activity
- Set up alerts for critical events
- Never log secrets or PII

---

## API Security

### Rate Limiting

```
TODO: <rate-limiting-example>
```

### Input Validation

- Validate request body, query params, headers
- Enforce size limits on payloads
- Reject unexpected fields

### CORS

Configure CORS properly:
```
TODO: <cors-example>
```

### API Keys

- Don't expose API keys in client-side code
- Use different keys for different environments
- Implement key rotation

---

## Dependency Security

### Scanning

**Tools**: TODO: <security-scan-tools>

**Commands**:
```bash
# npm audit
npm audit

# Python safety
safety check

# Cargo audit
cargo audit
```

### Updates

- Review and update dependencies regularly
- Test thoroughly after updates
- Subscribe to security advisories
- Use automated tools (Dependabot, Renovate)

---

## Security Checklist

### Development

- [ ] Input validation on all external input
- [ ] Parameterized queries (no SQL injection)
- [ ] Output escaping (no XSS)
- [ ] Authentication and authorization implemented
- [ ] Secrets stored securely (no hardcoded secrets)
- [ ] HTTPS/TLS for all connections
- [ ] CSRF protection for state-changing operations
- [ ] Rate limiting on sensitive endpoints

### Deployment

- [ ] Environment variables configured
- [ ] Secret rotation implemented
- [ ] Monitoring and alerting set up
- [ ] Security headers configured (CSP, HSTS, X-Frame-Options)
- [ ] Dependencies scanned for vulnerabilities
- [ ] Firewall and network policies configured
- [ ] Backups encrypted
- [ ] Access logs enabled

### Ongoing

- [ ] Regular dependency updates
- [ ] Periodic security audits
- [ ] Penetration testing (if applicable)
- [ ] Security training for team
- [ ] Incident response plan
- [ ] Regular secret rotation

---

## Incident Response

### Detection

- Monitor logs and alerts
- Watch for unusual activity
- Review security reports

### Response

1. **Contain**: Isolate affected systems
2. **Investigate**: Determine scope and impact
3. **Eradicate**: Remove threat and vulnerabilities
4. **Recover**: Restore systems to normal operation
5. **Post-Mortem**: Document lessons learned

### Communication

- Notify stakeholders
- Comply with disclosure requirements (GDPR, etc.)
- Update users if data was compromised

---

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- TODO: <project-specific-security-resources>

---

**Last Updated**: 2025-11-15
