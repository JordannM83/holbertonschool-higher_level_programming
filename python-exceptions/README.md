# Python - Exceptions

This project focuses on learning about Python exceptions, error handling, and how to use try/except blocks effectively.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- What's the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What's the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Files Description

### Mandatory Tasks

| File | Description |
|------|-------------|
| `0-safe_print_list.py` | Function that prints x elements of a list safely using try/except |
| `1-safe_print_integer.py` | Function that prints an integer with "{:d}".format() safely |
| `2-safe_print_list_integers.py` | Function that prints the first x elements of a list and only integers |
| `3-safe_print_division.py` | Function that divides 2 integers and prints the result |
| `4-list_division.py` | Function that divides element by element 2 lists |
| `5-raise_exception.py` | Function that raises a type exception |
| `6-raise_exception_msg.py` | Function that raises a name exception with a message |

### Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test file for task 0 |
| `1-main.py` | Test file for task 1 |
| `2-main.py` | Test file for task 2 |
| `3-main.py` | Test file for task 3 |
| `4-main.py` | Test file for task 4 |
| `5-main.py` | Test file for task 5 |
| `6-main.py` | Test file for task 6 |

## Usage Examples

### Task 0: Safe list printing
```python
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
```

### Task 1: Safe printing of integers list
```python
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
```

## Key Concepts

### Exception Handling
- **try/except blocks**: Used to catch and handle exceptions gracefully
- **IndexError**: Raised when trying to access an index that doesn't exist
- **ValueError**: Raised when a function receives an argument of correct type but inappropriate value
- **TypeError**: Raised when a function receives an argument of inappropriate type
- **ZeroDivisionError**: Raised when dividing by zero

### Best Practices
1. Always handle specific exceptions rather than using bare `except:`
2. Use `finally` blocks for cleanup actions
3. Don't suppress exceptions unless absolutely necessary
4. Provide meaningful error messages

## Author

This project is part of the Holberton School Higher Level Programming curriculum.