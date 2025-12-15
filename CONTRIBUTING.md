# Contributing to DAN Python Library

Thank you for your interest in contributing to DAN Python Library! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find that the issue has already been reported. When creating a bug report, include:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Code examples that demonstrate the issue
- Your environment (Python version, OS, etc.)

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) when creating an issue.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- A clear, descriptive title
- A detailed description of the proposed enhancement
- Use cases and examples
- Any alternative solutions you've considered

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md) when creating an issue.

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Add tests** for any new functionality
4. **Update documentation** as needed
5. **Ensure all tests pass** before submitting
6. **Submit a pull request** with a clear description of changes

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/dan-py.git
   cd dan-py
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

3. Run tests:
   ```bash
   python -m unittest discover tests -v
   ```

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use 2 spaces for indentation (as configured in `.editorconfig`)
- Maximum line length: 100 characters
- Use descriptive variable and function names
- Add docstrings to all public functions and classes

### Code Formatting

The project uses `.editorconfig` for consistent formatting. Please ensure your editor is configured to use it.

### Type Hints

Type hints are encouraged for better code documentation and IDE support:

```python
from typing import Any, Dict, Union

def decode(text: Union[str, bytes]) -> Dict[str, Any]:
    """Decode DAN text into a Python dictionary."""
    ...
```

### Testing

- Write tests for all new features
- Ensure all existing tests pass
- Aim for high test coverage
- Test edge cases and error conditions

### Documentation

- Update docstrings for any new or modified functions
- Update README.md if adding new features
- Add examples to the `examples/` directory for new use cases
- Update CHANGELOG.md with your changes

## Commit Messages

Follow these guidelines for commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally
- Consider starting the commit message with an applicable emoji:
  - 🐛 `:bug:` for bug fixes
  - ✨ `:sparkles:` for new features
  - 📝 `:memo:` for documentation
  - ♻️ `:recycle:` for refactoring
  - ✅ `:white_check_mark:` for tests
  - 🎨 `:art:` for code style/formatting

Example:
```
✨ Add support for nested table structures

- Implement parsing of nested tables within blocks
- Add tests for nested table scenarios
- Update documentation with examples

Fixes #123
```

## Pull Request Process

1. Update the CHANGELOG.md with your changes under the [Unreleased] section
2. Ensure your code follows the project's style guidelines
3. Make sure all tests pass
4. Update documentation as needed
5. Request review from maintainers

## Project Structure

```
dan-py/
├── dan.py              # Main library code
├── tests/              # Test suite
│   ├── __init__.py
│   └── test_dan.py
├── examples/           # Example DAN files
│   ├── README.md
│   └── *.dan
├── .github/            # GitHub templates and workflows
│   └── ISSUE_TEMPLATE/
├── README.md           # Main documentation
├── CONTRIBUTING.md     # This file
├── CHANGELOG.md        # Version history
├── FEATURES.md         # Feature documentation
├── LICENSE             # License file
└── pyproject.toml      # Package configuration
```

## Questions?

If you have questions about contributing, feel free to:

- Open a [Question issue](.github/ISSUE_TEMPLATE/question.md)
- Start a [Discussion](https://github.com/yourusername/dan-py/discussions)
- Contact the maintainers

Thank you for contributing to DAN Python Library! 🎉

