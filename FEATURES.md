# DAN Python Library - Features

This document provides a comprehensive overview of all features supported by the DAN Python Library.

## Core Features

### Decoding (Parsing)

The `decode()` function converts DAN text into Python dictionaries.

#### Supported Input Types
- **Strings**: Direct string input
- **Bytes**: Binary input (automatically decoded as UTF-8)

#### Data Structures

**Nested Blocks**
```dan
app {
  name: "MyApp"
  server {
    host: localhost
    port: 3000
  }
}
```

**Tables**
```dan
users: table(id, username, email) [
  1, alice, "alice@example.com"
  2, bob, "bob@example.com"
]
```

**Arrays**
```dan
roles: [admin, user, guest]
numbers: [1, 2, 3, 4, 5]
mixed: [1, "two", true, false, 3.14]
```

**Key-Value Pairs**
```dan
name: "John Doe"
age: 25
active: true
```

### Encoding (Serialization)

The `encode()` function converts Python dictionaries into properly formatted DAN text.

#### Supported Python Types
- **Dictionaries**: Converted to nested blocks
- **Lists of Dictionaries**: Converted to tables
- **Lists**: Converted to arrays
- **Strings**: Quoted in output
- **Numbers**: Integers and floats
- **Booleans**: Converted to `true`/`false`

## Data Type Support

### Strings

- **Quoted Strings**: `"Hello World"` → `"Hello World"`
- **Unquoted Strings**: `localhost` → `"localhost"`
- **Empty Strings**: `""` → `""`

### Numbers

- **Integers**: `42` → `42`
- **Floats**: `3.14` → `3.14`
- **Scientific Notation**: Not currently supported (parsed as strings)

### Booleans

- **True**: `true` → `True`
- **False**: `false` → `False`

### Arrays

- **String Arrays**: `[a, b, c]` → `["a", "b", "c"]`
- **Number Arrays**: `[1, 2, 3]` → `[1, 2, 3]`
- **Mixed Arrays**: `[1, "two", true]` → `[1, "two", True]`
- **Empty Arrays**: `[]` → `[]`
- **Nested Arrays**: Not currently supported

### Tables

Tables are arrays of dictionaries with consistent keys (columns).

**Input:**
```dan
users: table(id, username, email) [
  1, alice, "alice@example.com"
  2, bob, "bob@example.com"
]
```

**Output:**
```python
{
  "users": [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"}
  ]
}
```

## Comment Support

DAN supports two comment styles:

### Hash Comments (`#`)
```dan
# This is a comment
name: John  # Inline comment
```

### Double-Slash Comments (`//`)
```dan
// This is a comment
name: John  // Inline comment
```

### Comment Handling
- Comments are stripped during parsing
- Both styles can be used in the same file
- Inline comments are supported
- Comments don't affect parsing

## Advanced Features

### Deep Nesting

Blocks can be nested to any depth:

```dan
level1 {
  level2 {
    level3 {
      level4 {
        value: nested
      }
    }
  }
}
```

### Multiple Tables

A single DAN file can contain multiple tables:

```dan
users: table(id, name) [
  1, Alice
]

products: table(id, name, price) [
  1, Widget, 9.99
]
```

### Mixed Content

DAN files can contain a mix of blocks, tables, arrays, and key-value pairs:

```dan
app {
  name: "MyApp"
}

features: [auth, logging, monitoring]

users: table(id, name) [
  1, Alice
]

version: 1.0.0
```

## Error Handling

### Input Validation

- **Type Checking**: Raises `TypeError` for invalid input types
- **Empty Input**: Returns empty dictionary `{}`
- **Malformed Syntax**: May raise parsing errors (to be improved)

### Edge Cases

- **Empty Strings**: Handled gracefully
- **Whitespace-Only Input**: Returns empty dictionary
- **Missing Table Columns**: Filled with empty strings
- **Extra Table Values**: Ignored (only processes defined columns)

## Limitations

### Currently Not Supported

- **Null/None Values**: No explicit null support
- **Nested Arrays**: Arrays containing arrays
- **Table Row Validation**: No strict validation of table row structure
- **Custom Types**: No support for custom data types
- **Streaming**: No streaming parser for large files
- **Schema Validation**: No schema validation
- **Unicode Escaping**: Limited Unicode support

### Known Issues

- Large files may consume significant memory
- No size limits for input validation
- Type coercion may have edge cases

## Performance Considerations

- **Small Files**: Very fast parsing (< 1ms for typical configs)
- **Medium Files**: Good performance (< 10ms for files < 100KB)
- **Large Files**: May be slower; consider implementing size limits

## Future Enhancements

Potential features for future versions:

- [ ] Schema validation
- [ ] Streaming parser for large files
- [ ] Null/None value support
- [ ] Custom type handlers
- [ ] Better error messages with line numbers
- [ ] Performance optimizations
- [ ] YAML/JSON conversion utilities
- [ ] CLI tool for file conversion

## Examples

See the [examples/](examples/) directory for real-world usage scenarios:

- Application configuration
- Database schemas
- API route definitions
- Infrastructure as Code
- Game configurations
- IoT device management
- And many more!

## Getting Help

- 📖 Check the [README.md](README.md) for basic usage
- 💬 Ask questions in [Discussions](https://github.com/yourusername/dan-py/discussions)
- 🐛 Report bugs using the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)
- ✨ Request features using the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md)

