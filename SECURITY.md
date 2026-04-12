# Security policy — DAN Python library

## Supported versions

Security fixes are applied to the supported release line. Prefer the **latest** patch release.

| Version   | Supported          |
| --------- | ------------------ |
| 0.1.x     | :white_check_mark: |
| Before 0.1 | :x:              |

## Reporting a vulnerability

**Do not** report undisclosed security vulnerabilities through **public GitHub issues**.

Please report via **[GitHub private vulnerability reporting](https://github.com/marcuwynu23/dan-py/security/advisories/new)** (repository **Security** tab → **Report a vulnerability**).

Include:

- Description of the vulnerability and potential impact
- Steps to reproduce
- Affected versions or commits
- Optional: suggested fix or mitigation
- Optional: contact for follow-up questions

## What to expect

- **Acknowledgment:** within **48 hours** when possible  
- **Initial assessment:** within about **7 days**  
- **Updates** while we investigate and ship a fix  
- **Public disclosure** coordinated after a fix is available; credit unless you prefer to stay anonymous  

## Scope

This policy covers the **dan-py** package (Python parser/encoder and published artifacts in this repository).

## Safe harbor

Good-faith security research that follows this policy (no unnecessary access, no harm to users, prompt reporting) is considered authorized.

## Recommendations for users

- Treat parsed DAN as **untrusted** until validated for your domain.
- Apply **size limits** and resource bounds for network-supplied documents.
- **Upgrade** when security releases are published; see [CHANGELOG.md](CHANGELOG.md).

Thank you for helping keep users safe.
