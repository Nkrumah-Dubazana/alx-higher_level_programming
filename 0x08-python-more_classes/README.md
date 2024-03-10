# Python - More Classes and Objects

In this segment of our Python exploration, we dive deeper into object-oriented programming, focusing on class methods, static methods, and the distinction between class and instance attributes. Moreover, we delve into the usage of special methods like `__str__` and `__repr__` to enhance the functionality and representation of our classes.

## Testing :heavy_check_mark:

- **tests**: This directory contains test files, provided by Holberton School, to ensure our classes and methods perform as expected.

## Tasks Overview :page_with_curl:

### 0. Simple Rectangle

- **File**: `0-rectangle.py`
  - Defines an empty class named `Rectangle` that represents a rectangle.

### 1. The Real Definition of a Rectangle

- **File**: `1-rectangle.py`
  - Enhances the `Rectangle` class with width and height attributes, complete with property getters and setters for both. Implements initialization that allows for optional width and height parameters.

### 2. Area and Perimeter

- **File**: `2-rectangle.py`
  - Adds methods to calculate the area and perimeter of a rectangle within the `Rectangle` class.

### 3. String Representation

- **File**: `3-rectangle.py`
  - Implements the `__str__` method to enable printing the rectangle using the `#` character.

### 4. Eval is Magic

- **File**: `4-rectangle.py`
  - Integrates the `__repr__` method to allow for the recreation of a `Rectangle` instance from its string representation.

### 5. Detect Instance Deletion

- **File**: `5-rectangle.py`
  - Includes a `__del__` method that prints a farewell message upon the deletion of a `Rectangle` instance.

### 6. How Many Instances

- **File**: `6-rectangle.py`
  - Introduces a class attribute `number_of_instances` to keep track of the number of `Rectangle` instances.

### 7. Change Representation

- **File**: `7-rectangle.py`
  - Adds a class attribute `print_symbol` used in the string representation of `Rectangle`, demonstrating flexibility in symbol choice.

### 8. Compare Rectangles

- **File**: `8-rectangle.py`
  - Incorporates a static method `bigger_or_equal` to compare the area of two rectangles and return the larger or confirm their equality.

### 9. A Square is a Rectangle

- **File**: `9-rectangle.py`
  - Introduces a class method `square` that returns a new `Rectangle` instance with equal width and height, effectively acting as a square.

### 10. N Queens Puzzle

- **File**: `101-nqueens.py`
  - This Python script tackles the N queens puzzle by determining all possible arrangements for N non-attacking queens on an N×N chessboard. It emphasizes the importance of argument validation and the implementation of a classic algorithmic challenge.

This comprehensive overview bridges basic object-oriented concepts with more advanced Python features, fostering a deeper understanding of class interactions and object manipulation.
