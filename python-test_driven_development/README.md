# Python - Test-driven development

This project is part of the Holberton School Higher Level Programming curriculum. It focuses on the concept of Test-Driven Development (TDD) in Python, teaching how to write comprehensive tests before implementing code.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

## Project Structure

```
python-test_driven_development/
├── README.md
├── 0-add_integer.py
├── 0-main.py
├── 2-matrix_divided.py
├── 2-main.py
├── 3-say_my_name.py
├── 3-main.py
├── 4-print_square.py
├── 4-main.py
├── 5-text_indentation.py
├── 5-main.py
├── 6-max_integer.py
└── tests/
    ├── 0-add_integer.txt
    ├── 2-matrix_divided.txt
    ├── 3-say_my_name.txt
    ├── 4-print_square.txt
    ├── 5-text_indentation.txt
    └── 6-max_integer_test.py
```

## Tasks

### 0. Integers addition
**Files:** `0-add_integer.py`, `tests/0-add_integer.txt`
- Write a function that adds 2 integers.
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### 1. Divide a matrix
**Files:** `2-matrix_divided.py`, `tests/2-matrix_divided.txt`
- Write a function that divides all elements of a matrix.
- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats
- Each row of the `matrix` must be of the same size
- `div` must be a number (integer or float)
- `div` can't be equal to 0
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

### 2. Say my name
**Files:** `3-say_my_name.py`, `tests/3-say_my_name.txt`
- Write a function that prints `My name is <first name> <last name>`
- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception
- You are not allowed to import any module

### 3. Print square
**Files:** `4-print_square.py`, `tests/4-print_square.txt`
- Write a function that prints a square with the character `#`.
- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a `TypeError` exception
- if `size` is less than 0, raise a `ValueError` exception
- if `size` is a float and is less than 0, raise a `TypeError` exception first
- You are not allowed to import any module

### 4. Text indentation
**Files:** `5-text_indentation.py`, `tests/5-text_indentation.txt`
- Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module

### 5. Max integer - Unittest
**Files:** `6-max_integer.py`, `tests/6-max_integer_test.py`
- Since the beginning you have been creating "Interactive tests". For this exercise, you will add Unittests.
- In this task, you will write unittests for the function `def max_integer(list=[]):`
- Your test file should be inside a folder `tests`
- You have to use the unittest module
- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

## Running Tests

### Doctest
Run all doctests:
```bash
python3 -m doctest ./tests/*
```

Run a specific doctest:
```bash
python3 -m doctest ./tests/0-add_integer.txt
```

### Unittest
Run unittest:
```bash
python3 -m unittest tests.6-max_integer_test
```

Run unittest with verbose output:
```bash
python3 -m unittest tests.6-max_integer_test -v
```

### Interactive Testing
Run the main files to test functions interactively:
```bash
./0-main.py
./2-main.py
./3-main.py
./4-main.py
./5-main.py
```

## Test-Driven Development (TDD)

TDD is a software development process that relies on the repetition of a very short development cycle:

1. **Red**: Write a failing test
2. **Green**: Write the minimum amount of code to make the test pass
3. **Refactor**: Clean up the code while keeping the tests green

### Benefits of TDD:
- **Better code coverage**: Tests are written first, ensuring all code is tested
- **Improved design**: Writing tests first forces you to think about the interface
- **Regression protection**: Tests catch bugs when code changes
- **Documentation**: Tests serve as living documentation
- **Confidence**: You can refactor safely knowing tests will catch issues

### Types of Tests:
- **Unit tests**: Test individual functions or methods
- **Integration tests**: Test how different parts work together
- **Edge cases**: Test boundary conditions and error cases
- **Doctests**: Tests embedded in documentation strings

## Key Concepts

### Doctest
- Tests written in docstrings using interactive Python session format
- Executed with `python3 -m doctest`
- Example:
```python
def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b
```

### Unittest
- More structured testing framework
- Organized in test classes inheriting from `unittest.TestCase`
- Uses assertion methods like `assertEqual()`, `assertRaises()`
- Example:
```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

### Edge Cases to Consider
- **Empty inputs**: empty lists, empty strings, None values
- **Boundary values**: zero, negative numbers, very large numbers
- **Type errors**: wrong data types
- **Invalid inputs**: division by zero, negative sizes for squares

## Best Practices

1. **Write tests first**: Follow TDD principles
2. **Test edge cases**: Don't just test happy path
3. **Clear test names**: Use descriptive test method names
4. **One assertion per test**: Keep tests focused
5. **Use docstrings**: Document what each test does
6. **Test error conditions**: Use `assertRaises()` for expected exceptions

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-test_driven_development`

## Author

**Holberton School Student**
