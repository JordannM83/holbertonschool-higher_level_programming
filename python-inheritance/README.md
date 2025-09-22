# Python - Inheritance

This project covers the concept of inheritance in Python programming language, including class inheritance, method overriding, and built-in functions to work with object types and inheritance.

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation
- All your classes should have a documentation
- All your functions (inside and outside a class) should have a documentation
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

## Tasks

0. **Lookup** - Write a function that returns the list of available attributes and methods of an object
1. **My list** - Write a class MyList that inherits from list
2. **Exact same object** - Write a function that returns True if the object is exactly an instance of the specified class
3. **Same class or inherit from** - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
4. **Only sub class of** - Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class
5. **Geometry module** - Write an empty class BaseGeometry
6. **Improve Geometry** - Write a class BaseGeometry with an area() method that raises an Exception
7. **Integer validator** - Write a class BaseGeometry with area() and integer_validator() methods
8. **Rectangle** - Write a class Rectangle that inherits from BaseGeometry
9. **Full rectangle** - Write a class Rectangle that inherits from BaseGeometry with area() method implemented
10. **Square #1** - Write a class Square that inherits from Rectangle
11. **Square #2** - Write a class Square that inherits from Rectangle with proper string representation

## Author

This project was created as part of the Holberton School curriculum.
