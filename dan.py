"""
DAN (Data Advanced Notation) Parser and Encoder for Python
"""

import re
from typing import Any, Dict, List, Union


def decode(text: Union[str, bytes]) -> Dict[str, Any]:
    """
    Decode DAN text into a Python dictionary.
    
    Args:
        text: DAN text as string or bytes
        
    Returns:
        Dictionary representation of the DAN data
        
    Raises:
        TypeError: If input is not string or bytes
    """
    # Handle bytes inputs
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # Ensure text is a string
    if not isinstance(text, str):
        raise TypeError(f"Expected string or bytes, got {type(text).__name__}")
    
    # Handle empty input - return empty object
    if not text or not text.strip():
        return {}
    
    lines = text.splitlines()
    stack = [{"obj": {}, "type": "root"}]
    current_table = None
    
    table_re = re.compile(r'^(\w+):\s*table\(([^)]+)\)\s*\[$')
    kv_re = re.compile(r'^(\w+):\s*(.+)$')
    
    for i, line in enumerate(lines):
        # Remove comments and trim
        comment_index1 = line.find("#")
        comment_index2 = line.find("//")
        cut_index = -1
        if comment_index1 >= 0 and comment_index2 >= 0:
            cut_index = min(comment_index1, comment_index2)
        else:
            cut_index = max(comment_index1, comment_index2)
        
        if cut_index >= 0:
            line = line[:cut_index]
        line = line.strip()
        if not line:
            continue
        
        top = stack[-1]
        
        # Block start
        if line.endswith("{"):
            key = line[:-1].strip()
            new_obj = {}
            top["obj"][key] = new_obj
            stack.append({"obj": new_obj, "type": "block"})
            continue
        
        # Block end
        if line == "}":
            stack.pop()
            continue
        
        # Table start
        table_match = table_re.match(line)
        if table_match:
            key = table_match.group(1)
            columns = [c.strip() for c in table_match.group(2).split(",")]
            table = []
            top["obj"][key] = table
            current_table = {"obj": table, "columns": columns}
            continue
        
        # Table end
        if line == "]":
            current_table = None
            continue
        
        # Table row
        if current_table:
            row = {}
            # Split by comma and trim each value
            values = [v.strip() for v in line.split(",")]
            # Only process up to the number of columns defined
            for col_idx, val in enumerate(values):
                if col_idx < len(current_table["columns"]):
                    row[current_table["columns"][col_idx]] = parse_value(val)
            # Ensure all columns are present (fill missing with empty string)
            for col_idx, col_name in enumerate(current_table["columns"]):
                if col_name not in row:
                    row[col_name] = ""
            current_table["obj"].append(row)
            continue
        
        # Key-value
        kv_match = kv_re.match(line)
        if kv_match:
            key = kv_match.group(1)
            val = kv_match.group(2)
            top["obj"][key] = parse_value(val)
    
    return stack[0]["obj"]


def encode(obj: Dict[str, Any], indent: int = 0) -> str:
    """
    Encode a Python dictionary into DAN text.
    
    Args:
        obj: Dictionary to encode
        indent: Current indentation level (for recursion)
        
    Returns:
        DAN text representation
    """
    lines = []
    pad = "  " * indent
    
    for key, val in obj.items():
        if isinstance(val, list):
            if len(val) > 0 and isinstance(val[0], dict) and not isinstance(val[0], list):
                # Table
                columns = list(val[0].keys())
                lines.append(f"{pad}{key}: table({', '.join(columns)}) [")
                for row in val:
                    row_values = [serialize_value(row.get(c)) for c in columns]
                    lines.append(f"{pad}  {', '.join(row_values)}")
                lines.append(f"{pad}]")
            else:
                lines.append(f"{pad}{key}: {serialize_value(val)}")
        elif isinstance(val, dict):
            lines.append(f"{pad}{key} {{")
            nested_lines = encode(val, indent + 1)
            if nested_lines:
                # Split nested lines and add them individually for proper formatting
                nested_lines_array = nested_lines.split("\n")
                lines.extend(nested_lines_array)
            lines.append(f"{pad}}}")
        else:
            lines.append(f"{pad}{key}: {serialize_value(val)}")
    
    return "\n".join(lines)


# --- Internal helpers ---

def parse_value(val: str) -> Any:
    """
    Parse a string value into appropriate Python type.
    
    Args:
        val: String value to parse
        
    Returns:
        Parsed value (bool, int, float, str, list, or original string)
    """
    if not isinstance(val, str):
        return val
    
    val = val.strip()
    
    if val == "true":
        return True
    if val == "false":
        return False
    
    # String (quoted)
    if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
        return val[1:-1]
    
    # Number
    if val and not val.startswith("["):
        try:
            # Try integer first
            if '.' not in val:
                return int(val)
            else:
                return float(val)
        except ValueError:
            pass
    
    # Array
    if len(val) >= 2 and val[0] == "[" and val[-1] == "]":
        content = val[1:-1].strip()
        if content == "":
            return []
        # Split by comma, but preserve empty strings for explicit empty values
        parts = [v.strip() for v in content.split(",")]
        return [parse_value(v) for v in parts]
    
    return val


def serialize_value(val: Any) -> str:
    """
    Serialize a Python value to DAN string representation.
    
    Args:
        val: Value to serialize
        
    Returns:
        String representation
    """
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, str):
        return f'"{val}"'
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, list):
        return f"[{', '.join(serialize_value(v) for v in val)}]"
    return str(val)

