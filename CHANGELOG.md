# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive test suite with 40+ test cases
- Multiple example DAN files for various use cases
- GitHub community files (CODE_OF_CONDUCT.md, SECURITY.md, etc.)
- Project documentation (CONTRIBUTING.md, FEATURES.md, CHANGELOG.md)
- Issue templates for bug reports, feature requests, and questions

### Changed
- Improved table parsing to handle rows with varying column counts
- Enhanced README with better documentation and examples

## [0.1.0] - 2024-12-15

### Added
- Initial release of DAN Python Library
- `decode()` function to parse DAN text into Python dictionaries
- `encode()` function to convert Python dictionaries into DAN text
- Support for nested blocks with `{ }` syntax
- Support for tables with `table(columns) [rows]` syntax
- Support for arrays with `[values]` syntax
- Type inference for strings, numbers, booleans, and arrays
- Comment support for both `#` and `//` styles
- Support for quoted and unquoted string values
- Support for bytes input (from file reading)
- Comprehensive error handling
- Basic test suite

### Features
- **Decoding**: Parse DAN text (string or bytes) into Python dictionaries
- **Encoding**: Convert Python dictionaries into properly formatted DAN text
- **Nested Structures**: Support for deeply nested block structures
- **Tables**: Support for tabular data with column definitions
- **Arrays**: Support for array values with mixed types
- **Comments**: Support for both hash (#) and double-slash (//) comments
- **Type Inference**: Automatic detection of booleans, numbers, strings, and arrays

[Unreleased]: https://github.com/yourusername/dan-py/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/dan-py/releases/tag/v0.1.0

