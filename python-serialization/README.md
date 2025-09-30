# Python - Serialization

## Description

This project explores different serialization and deserialization techniques in Python. Serialization is the process of converting a Python object into a format that can be stored or transmitted and then reconstructed later. This project covers JSON serialization, pickle serialization, CSV to JSON conversion, and XML serialization.

## Learning Objectives

By the end of this project, you should be able to:

- Understand what serialization and deserialization mean
- Serialize and deserialize Python objects using JSON
- Use the `pickle` module to serialize custom Python objects
- Handle CSV data and convert it to JSON format
- Work with XML serialization as an alternative to JSON
- Understand the different use cases for each serialization method

## Files Description

### Task 0: Basic Serialization
- **File**: `task_00_basic_serialization.py`
- **Description**: Implements basic serialization and deserialization using JSON format
- **Functions**:
  - `serialize_and_save_to_file(data, filename)`: Serializes a Python dictionary to a JSON file
  - `load_and_deserialize(filename)`: Loads and deserializes data from a JSON file
- **Test**: `main_00_basic_serialization.py`

### Task 1: Pickling Custom Classes
- **File**: `task_01_pickle.py`
- **Description**: Demonstrates serialization and deserialization of custom Python objects using pickle
- **Class**: `CustomObject`
  - Attributes: `name`, `age`, `is_student`
  - Methods: `display()`, `serialize()`, `deserialize()`
- **Test**: `main_01_pickle.py`

### Task 2: Converting CSV to JSON
- **File**: `task_02_csv.py`
- **Description**: Reads data from CSV format and converts it to JSON format
- **Functions**:
  - `convert_csv_to_json(csv_filename)`: Converts CSV data to JSON format
- **Data**: `data.csv` - Sample CSV file with user data
- **Test**: `main_02_csv.py`

### Task 3: Serializing and Deserializing with XML
- **File**: `task_03_xml.py`
- **Description**: Explores XML as an alternative serialization format
- **Functions**:
  - `serialize_to_xml(dictionary, filename)`: Serializes a Python dictionary to XML
  - `deserialize_from_xml(filename)`: Deserializes XML data back to a Python dictionary
- **Test**: `main_03_xml.py`

## Usage Examples

### JSON Serialization
```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Serialize data
data = {"name": "John", "age": 30, "city": "New York"}
serialize_and_save_to_file(data, 'data.json')

# Deserialize data
loaded_data = load_and_deserialize('data.json')
print(loaded_data)
```

### Pickle Serialization
```python
from task_01_pickle import CustomObject

# Create and serialize object
obj = CustomObject("John", 25, True)
obj.serialize("object.pkl")

# Deserialize object
new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()
```

### CSV to JSON Conversion
```python
from task_02_csv import convert_csv_to_json

# Convert CSV to JSON
convert_csv_to_json("data.csv")
```

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the PEP 8 style (pycodestyle version 2.8.*)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation

## Serialization Methods Comparison

| Method | Use Case | Pros | Cons |
|--------|----------|------|------|
| **JSON** | Web APIs, configuration files | Human-readable, language-independent | Limited data types |
| **Pickle** | Python-specific object storage | Supports complex Python objects | Python-only, security concerns |
| **CSV** | Tabular data exchange | Simple, widely supported | Only for tabular data |
| **XML** | Document structure, configuration | Self-describing, hierarchical | Verbose, complex parsing |

## Author

This project is part of the Holberton School Higher Level Programming curriculum.