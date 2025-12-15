# DAN (Data Advanced Notation) Python Library

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Python implementation of the DAN (Data Advanced Notation) parser and encoder. DAN is a human-readable data format that combines the simplicity of key-value pairs with the power of nested structures and tables.

## Features

- **Decode**: Parse DAN text into Python dictionaries
- **Encode**: Convert Python dictionaries into DAN text
- Support for nested blocks, tables, arrays, and various data types
- Comment support (# and //)
- Type inference (strings, numbers, booleans, arrays)
- Comprehensive test suite with 40+ test cases
- Multiple real-world examples

See [FEATURES.md](FEATURES.md) for a complete feature list.

## Installation

```bash
pip install -e .
```

Or install from source:

```bash
git clone https://github.com/yourusername/dan-py.git
cd dan-py
pip install -e .
```

## Quick Start

### Decoding DAN

```python
from dan import decode

text = """
app {
  name: "MyApp"
  version: 1.0
  server {
    host: localhost
    port: 3000
  }
}
"""

data = decode(text)
print(data)
# {'app': {'name': 'MyApp', 'version': 1.0, 'server': {'host': 'localhost', 'port': 3000}}}
```

### Encoding to DAN

```python
from dan import encode

data = {
    "app": {
        "name": "MyApp",
        "version": 1.0,
        "server": {
            "host": "localhost",
            "port": 3000
        }
    }
}

text = encode(data)
print(text)
```

### Working with Tables

```python
text = """
users: table(id, username, email) [
  1, alice, "alice@example.com"
  2, bob, "bob@example.com"
]
"""

data = decode(text)
# {'users': [{'id': 1, 'username': 'alice', 'email': 'alice@example.com'}, ...]}
```

### Reading from Files

```python
from dan import decode

with open('config.dan', 'r') as f:
    config = decode(f.read())
```

## Examples

Check out the [examples/](examples/) directory for real-world usage scenarios:

- Application configuration (`config.dan`)
- Database schemas (`database_schema.dan`)
- API routes (`api_routes.dan`)
- Microservices configuration (`microservices.dan`)
- Docker Compose (`docker_compose.dan`)
- Kubernetes resources (`kubernetes.dan`)
- And many more!

## Running Tests

```bash
# Run all tests
python -m unittest discover tests -v

# Run specific test file
python -m unittest tests.test_dan -v

# Using pytest (if installed)
pytest tests/
```

## Documentation

- [FEATURES.md](FEATURES.md) - Complete feature documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guidelines for contributing
- [CHANGELOG.md](CHANGELOG.md) - Version history and changes
- [examples/README.md](examples/README.md) - Example files documentation

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security

Please report security vulnerabilities to the maintainers. See [SECURITY.md](SECURITY.md) for more information.

## Support

- 📖 [Documentation](https://github.com/yourusername/dan-py#readme)
- 🐛 [Issue Tracker](https://github.com/yourusername/dan-py/issues)
- 💬 [Discussions](https://github.com/yourusername/dan-py/discussions)

