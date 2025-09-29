# Python - Input/Output

This repository contains Python programs that demonstrate various input/output operations, including file handling, JSON serialization/deserialization, and object-oriented programming concepts.

## 📁 Project Structure

```
python-input_output/
├── 0-read_file.py          # Read and print file contents
├── 1-write_file.py         # Write string to file
├── 2-append_write.py       # Append string to file
├── 3-to_json_string.py     # Convert object to JSON string
├── 4-from_json_string.py   # Convert JSON string to object
├── 5-save_to_json_file.py  # Save object to JSON file
├── 6-load_from_json_file.py # Load object from JSON file
├── 7-add_item.py           # Script to add arguments to list
├── 8-class_to_json.py      # Convert class instance to dictionary
├── 9-student.py            # Student class with JSON serialization
├── 10-student.py           # Student class with attribute filtering
├── 11-student.py           # Student class with deserialization
├── 12-pascal_triangle.py   # Generate Pascal's triangle
├── 8-my_class.py           # Test class for task 8
├── 8-my_class_2.py         # Second test class for task 8
└── *-main.py               # Test files for each task
```

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- How to open a file in Python
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON and how to serialize/deserialize data
- What are `*args` and how to use them
- What are `**kwargs` and how to use them
- How to handle named arguments in a function

## 📋 Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code follows pycodestyle (version 2.8.*)
- All files are executable
- All modules, classes and functions have documentation

## 📖 Tasks Description

### Task 0: Read file
**File:** `0-read_file.py`

Write a function that reads a text file (UTF8) and prints it to stdout:
- Prototype: `def read_file(filename=""):`
- Must use the `with` statement
- No need to manage file permission or file doesn't exist exceptions
- Not allowed to import any module

### Task 1: Write to a file
**File:** `1-write_file.py`

Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
- Prototype: `def write_file(filename="", text=""):`
- Must use the `with` statement
- Function should create the file if it doesn't exist
- Function should overwrite the content if file already exists
- Not allowed to import any module

### Task 2: Append to a file
**File:** `2-append_write.py`

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
- Prototype: `def append_write(filename="", text=""):`
- If the file doesn't exist, it should be created
- Must use the `with` statement
- Not allowed to import any module

### Task 3: To JSON string
**File:** `3-to_json_string.py`

Write a function that returns the JSON representation of an object (string):
- Prototype: `def to_json_string(my_obj):`
- No need to manage exceptions if the object can't be serialized

### Task 4: From JSON string to Object
**File:** `4-from_json_string.py`

Write a function that returns an object (Python data structure) represented by a JSON string:
- Prototype: `def from_json_string(my_str):`
- No need to manage exceptions if the JSON string doesn't represent an object

### Task 5: Save Object to a file
**File:** `5-save_to_json_file.py`

Write a function that writes an Object to a text file, using a JSON representation:
- Prototype: `def save_to_json_file(my_obj, filename):`
- Must use the `with` statement
- No need to manage exceptions if the object can't be serialized

### Task 6: Create object from a JSON file
**File:** `6-load_from_json_file.py`

Write a function that creates an Object from a "JSON file":
- Prototype: `def load_from_json_file(filename):`
- Must use the `with` statement
- No need to manage exceptions if the JSON string doesn't represent an object

### Task 7: Load, add, save
**File:** `7-add_item.py`

Write a script that adds all arguments to a Python list, and then save them to a file:
- Must use functions `save_to_json_file` and `load_from_json_file`
- List must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn't exist, it should be created

### Task 8: Class to JSON
**File:** `8-class_to_json.py`

Write a function that returns the dictionary description with simple data structure for JSON serialization of an object:
- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
- Not allowed to import any module

### Task 9: Student to JSON
**File:** `9-student.py`

Write a class Student that defines a student by:
- Public instance attributes: `first_name`, `last_name`, `age`
- Instantiation with `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance

### Task 10: Student to JSON with filter
**File:** `10-student.py`

Based on `9-student.py`, add filtering capability:
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation
- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved
- Otherwise, all attributes must be retrieved

### Task 11: Student to disk and reload
**File:** `11-student.py`

Based on `10-student.py`, add deserialization capability:
- Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance
- You can assume `json` will always be a dictionary
- A dictionary key will be the public attribute name
- A dictionary value will be the value of the public attribute

### Task 12: Pascal's Triangle
**File:** `12-pascal_triangle.py`

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal's triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer
- Not allowed to import any module

## 🚀 Usage Examples

### Reading a file:
```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file
read_file("my_file_0.txt")
```

### Writing to a file:
```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
```

### JSON serialization:
```python
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string
my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)  # [1, 2, 3]
print(type(s_my_list))  # <class 'str'>
```

### Student class usage:
```python
#!/usr/bin/python3
Student = __import__('9-student').Student
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]
for student in students:
    j_student = student.to_json()
    print(j_student['first_name'])
    print(j_student['age'])
```

## 🧪 Testing

Each task comes with a corresponding main file for testing:

```bash
# Test file reading
./0-main.py

# Test file writing
./1-main.py

# Test JSON operations
./3-main.py
./4-main.py
./5-main.py
./6-main.py

# Test Student class
./9-main.py
./10-main.py
./11-main.py student.json

# Test Pascal's triangle
./12-main.py
```

## ✅ Code Quality

All code in this project follows:
- **PEP 8** style guide (checked with `pycodestyle`)
- **Documentation** for all modules, classes, and functions
- **Error handling** where appropriate
- **Best practices** for file operations and JSON handling

## 📝 Author

This project is part of the Holberton School Higher Level Programming curriculum.

## 📄 License

This project is for educational purposes as part of Holberton School's curriculum.