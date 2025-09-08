# Python - Import & Modules

This project is part of the Holberton School Higher Level Programming curriculum. It focuses on understanding Python modules, imports, and how to structure Python programs using modules and packages.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

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

## Files Description

### Module Files
- **`add_0.py`** - Contains the `add` function that adds two integers
- **`calculator_1.py`** - Contains basic calculator functions (add, sub, mul, div)
- **`variable_load_5.py`** - Contains a variable that will be imported

### Task Files

#### 0. Import a simple function from a simple file
**File:** `0-import_add.py`
- Import the function `add(a, b)` from the file `add_0.py`
- Print the result of the addition `1 + 2 = 3`
- Use print function with string format to display integers
- Assign the value `1` to variable `a`, `2` to variable `b`, and use those variables only

#### 1. My first toolbox!
**File:** `1-calculation.py`
- Import functions from the file `calculator_1.py`
- Do some Maths operations and print the results
- Use only the functions imported from `calculator_1.py`
- Use print function with string format to display integers
- Variables `a` and `b` are used for the operations

#### 2. How to make a script dynamic!
**File:** `2-args.py`
- Print the number of and the list of its arguments
- The output should be:
  - Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
  - `:` (or `.` if no argument was passed) followed by
  - A new line, followed by (if at least one argument), one line per argument:
    - The position of the argument (starting at 1) followed by `: `, followed by the argument value and a new line

#### 3. Infinite addition
**File:** `3-infinite_add.py`
- Print the result of the addition of all arguments
- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers using `int()`
- Your code should not be executed when imported

#### 4. Who are you?
**File:** `4-hidden_discovery.py`
- Print all the names defined by the compiled module `hidden_4.pyc`
- Print one name per line, in alpha order
- Print only names that do **not** start with `__`
- Your code should not be executed when imported

#### 5. Everything can be imported
**File:** `5-variable_load.py`
- Import the variable `a` from the file `variable_load_5.py`
- Print the value of the variable `a`
- Your code should not be executed when imported

## Usage Examples

### Running the scripts

```bash
# Task 0
./0-import_add.py
# Output: 1 + 2 = 3

# Task 1
./1-calculation.py
# Output: 
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2

# Task 2
./2-args.py
# Output: 0 arguments.

./2-args.py Hello
# Output: 
# 1 argument:
# 1: Hello

./2-args.py Hello World School 98 Battery
# Output:
# 5 arguments:
# 1: Hello
# 2: World
# 3: School
# 4: 98
# 5: Battery

# Task 3
./3-infinite_add.py
# Output: 0

./3-infinite_add.py 79 10
# Output: 89

./3-infinite_add.py 79 10 -40 -300 89
# Output: -162

# Task 5
./5-variable_load.py
# Output: 98
```

### Making files executable

```bash
chmod +x *.py
```

## Key Concepts

### Import Methods
1. **Direct import:** `import module_name`
2. **From import:** `from module_name import function_name`
3. **Import with alias:** `import module_name as alias`
4. **Import all:** `from module_name import *` (not recommended)

### Command Line Arguments
- Access via `sys.argv`
- `sys.argv[0]` is the script name
- `sys.argv[1:]` are the actual arguments

### Module Protection
Use `if __name__ == "__main__":` to prevent code execution when imported.

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-import_modules`

## Author

**Holberton School Student**