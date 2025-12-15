# Security Policy

## Supported Versions

We actively support and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

We take the security of DAN Python Library seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send an email to [security@example.com] with details about the vulnerability
2. **GitHub Security Advisory**: Use GitHub's [private vulnerability reporting](https://github.com/yourusername/dan-py/security/advisories/new) feature

### What to Include

When reporting a vulnerability, please include:

- A description of the vulnerability
- Steps to reproduce the issue
- Potential impact of the vulnerability
- Any suggested fixes or mitigations (if you have them)
- Your contact information (optional, but helpful for follow-up questions)

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Initial Assessment**: We will provide an initial assessment within 7 days
- **Updates**: We will keep you informed of our progress
- **Resolution**: We will work to resolve the issue as quickly as possible

### Disclosure Policy

- We will work with you to understand and resolve the issue quickly
- We will credit you for the discovery (unless you prefer to remain anonymous)
- We will not disclose the vulnerability publicly until a fix is available
- We will coordinate with you on the timing of any public disclosure

### Security Best Practices

When using DAN Python Library:

1. **Keep dependencies updated**: Regularly update to the latest version
2. **Validate input**: Always validate and sanitize input data before processing
3. **Use in trusted environments**: Be cautious when parsing untrusted DAN files
4. **Review examples**: Check the examples directory for best practices

### Known Security Considerations

- **Input Validation**: The library parses text input. Always validate input from untrusted sources
- **Resource Limits**: Large DAN files may consume significant memory. Consider implementing size limits for untrusted input
- **Type Coercion**: The parser performs automatic type conversion. Be aware of potential type confusion issues

### Security Updates

Security updates will be released as patch versions (e.g., 0.1.1, 0.1.2) and will be documented in the [CHANGELOG.md](CHANGELOG.md).

## Thank You

Thank you for helping keep DAN Python Library and its users safe!

