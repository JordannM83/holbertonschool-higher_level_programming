# Tests Directory - Python Test-driven Development

This directory contains all test files for the Python Test-driven Development project. The tests are designed to validate the functionality of each module and ensure code quality through comprehensive testing.

## 📋 Test Files Overview

### Doctest Files (.txt)
These files contain interactive Python session examples used for testing functions:

| File | Module Tested | Description |
|------|---------------|-------------|
| `0-add_integer.txt` | `0-add_integer.py` | Tests for integer addition function |
| `2-matrix_divided.txt` | `2-matrix_divided.py` | Tests for matrix division function |
| `3-say_my_name.txt` | `3-say_my_name.py` | Tests for name printing function |
| `4-print_square.txt` | `4-print_square.py` | Tests for square printing function |
| `5-text_indentation.txt` | `5-text_indentation.py` | Tests for text indentation function |

### Unittest Files (.py)
| File | Module Tested | Description |
|------|---------------|-------------|
| `6-max_integer_test.py` | `6-max_integer.py` | Unit tests for max integer function |

## 🧪 Running Tests

### Running All Doctests
```bash
# From the project root directory
python3 -m doctest ./tests/*
```

### Running Specific Doctests
```bash
# Test a specific module
python3 -m doctest ./tests/0-add_integer.txt
python3 -m doctest ./tests/2-matrix_divided.txt
python3 -m doctest ./tests/3-say_my_name.txt
python3 -m doctest ./tests/4-print_square.txt
python3 -m doctest ./tests/5-text_indentation.txt
```

### Running Doctests with Verbose Output
```bash
python3 -m doctest ./tests/0-add_integer.txt -v
```

### Running Unittests
```bash
# Run all unittest methods
python3 -m unittest tests.6-max_integer_test

# Run with verbose output
python3 -m unittest tests.6-max_integer_test -v

# Run specific test method
python3 -m unittest tests.6-max_integer_test.TestMaxInteger.test_ordered_list
```

### Running Tests with Coverage (Optional)
```bash
# Install coverage if not already installed
pip3 install coverage

# Run tests with coverage
coverage run -m unittest tests.6-max_integer_test
coverage report -m
```

## 📝 Test Structure

### Doctest Format
Doctests are written in the docstring format using interactive Python session syntax:

```python
"""
>>> function_name(arguments)
expected_output

>>> function_name(error_case)
Traceback (most recent call last):
    ...
ExpectedError: error message
"""
```

### Unittest Format
Unit tests are organized in classes inheriting from `unittest.TestCase`:

```python
class TestClassName(unittest.TestCase):
    def test_method_name(self):
        self.assertEqual(actual, expected)
        self.assertRaises(ExceptionType, function, args)
```

## 🎯 Test Categories

### Normal Cases
- Valid inputs with expected outputs
- Boundary values (0, 1, maximum values)
- Different data types where applicable

### Edge Cases
- Empty inputs (empty lists, empty strings)
- Single element inputs
- Maximum/minimum values
- Special characters and formatting

### Error Cases
- Invalid data types
- Out of range values
- Division by zero
- None values
- Negative values where not allowed

## 📊 Test Coverage Areas

Each test file covers:

1. **Functionality Testing**
   - Core function behavior
   - Return values and types
   - Output formatting

2. **Input Validation**
   - Type checking
   - Value range validation
   - Parameter requirements

3. **Error Handling**
   - Exception raising
   - Error messages
   - Recovery mechanisms

4. **Edge Cases**
   - Boundary conditions
   - Empty or null inputs
   - Extreme values

## 🔧 Test File Details

### `0-add_integer.txt`
Tests the `add_integer(a, b=98)` function:
- Integer addition with positive/negative numbers
- Float to integer conversion
- Type error handling for non-numeric inputs
- Default parameter behavior

### `2-matrix_divided.txt`
Tests the `matrix_divided(matrix, div)` function:
- Matrix division with proper formatting (2 decimal places)
- Row size validation
- Division by zero error handling
- Type validation for matrix elements

### `3-say_my_name.txt`
Tests the `say_my_name(first_name, last_name="")` function:
- Name printing with both parameters
- Default last name behavior
- String type validation
- Output format verification

### `4-print_square.txt`
Tests the `print_square(size)` function:
- Square printing with different sizes
- Zero size handling
- Negative size error handling
- Integer type validation

### `5-text_indentation.txt`
Tests the `text_indentation(text)` function:
- Text formatting with sentence separators (. ? :)
- Whitespace handling
- String type validation
- Special character processing

### `6-max_integer_test.py`
Unit tests for `max_integer(list=[])` function:
- Various list configurations (ordered, unordered, mixed)
- Single element and empty list handling
- Different data types (integers, floats, strings)
- None and edge case handling

## 📚 Best Practices

### Writing Good Tests
1. **Test one thing at a time** - Keep tests focused
2. **Use descriptive names** - Test names should explain what they test
3. **Include edge cases** - Don't just test the happy path
4. **Test error conditions** - Verify proper exception handling
5. **Keep tests independent** - Tests should not depend on each other

### Doctest Guidelines
- Use realistic examples that demonstrate function usage
- Include both successful cases and error cases
- Keep examples simple and readable
- Use `<BLANKLINE>` for empty lines in output
- Test with different input combinations

### Unittest Guidelines
- Organize tests in logical test classes
- Use appropriate assertion methods (`assertEqual`, `assertRaises`, etc.)
- Set up and tear down test data when needed
- Use meaningful test method names starting with `test_`

## 🚀 Continuous Integration

These tests are designed to be run in automated testing environments:

```bash
# Example CI command
python3 -m doctest ./tests/* && python3 -m unittest tests.6-max_integer_test
```

## 📖 Documentation Standards

All test files follow the project's documentation standards:
- Clear, descriptive comments
- Proper formatting and indentation
- Comprehensive coverage of function behavior
- Realistic examples and use cases

---

**Note:** Always run tests after making changes to ensure code quality and prevent regressions. The tests serve as both validation tools and living documentation of expected behavior.
