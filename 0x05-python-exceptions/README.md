Python - Error and Exception Handling

This project focuses on understanding and implementing error and exception handling in Python through the use of try-except blocks.

Function Definitions 🛠️

Below are the definitions for the functions developed in this project:

| File                          | Definition                                    |
|-------------------------------|-----------------------------------------------|
| 0-safe_print_list.py          | `def safe_print_list(my_list=[], x=0):`       |
| 1-safe_print_integer.py       | `def safe_print_integer(value):`              |
| 2-safe_print_list_integers.py | `def safe_print_list_integers(my_list=[], x=0):` |
| 3-safe_print_division.py      | `def safe_print_division(a, b):`              |
| 4-list_division.py            | `def list_division(my_list_1, my_list_2, list_length):` |
| 5-raise_exception.py          | `def raise_exception():`                     |
| 6-raise_exception_msg.py      | `def raise_exception_msg(message=""):`       |
| 100-safe_print_integer_err.py | `def safe_print_integer_err(value):`         |
| 101-safe_function.py          | `def safe_function(fct, *args):`             |
| 102-magic_calculation.py      | `def magic_calculation(a, b);`               |
| 103-python.c                  | C functions to print Python object details:  |
|                               | - `void print_python_list(PyObject *p);`     |
|                               | - `void print_python_bytes(PyObject *p);`    |
|                               | - `void print_python_float(PyObject *p);`    |

Project Tasks 📝

1. **Safe List Printing**
   - `0-safe_print_list.py`: Prints `x` elements of a list in a single line, ending with a newline.
   - The `x` parameter denotes the number of elements to print, which may exceed the list's length.
   - Returns the actual number of elements printed.
   - Implemented without importing modules or using `len()`.

2. **Safe Integer Printing**
   - `1-safe_print_integer.py`: Prints an integer using the `"{:d}".format()` method.
   - The `value` parameter can be of any type.
   - Returns `True` if the value was printed correctly (i.e., was an integer), otherwise `False`.
   - Implemented without importing modules or using `type()`.

3. **Printing and Counting Integers**
   - `2-safe_print_list_integers.py`: Prints the first `x` elements of a list that are integers.
   - The `my_list` parameter may contain any type.
   - The `x` parameter denotes the number of elements to print, possibly exceeding the list's length.
   - Returns the actual number of integers printed.
   - Implemented without importing modules or using `len()`.

4. **Division of Integers with Debugging**
   - `3-safe_print_division.py`: Divides two integers and prints the result, utilizing a `finally:` block.
   - Assumes the arguments are integers.
   - Returns the division result, or `None` upon failure.
   - Implemented without importing modules.

5. **List Division**
   - `4-list_division.py`: Divides elements of two lists element-by-element.
   - Returns a new list with the division results.
   - Handles various errors such as type mismatches and division by zero, printing appropriate messages.
   - Implemented without importing modules.

6. **Raising Exceptions**
   - `5-raise_exception.py`: Raises a type exception.
   - Implemented without importing modules.

7. **Raising an Exception with a Message**
   - `6-raise_exception_msg.py`: Raises a name exception with a specified message.
   - Implemented without importing modules.

8. **Safe Integer Printing with Error Handling**
   - `100-safe_print_integer_err.py`: Prints an integer with type checking, handling errors by printing to stderr.
   - Returns `True` if the value was printed correctly.
   - Implemented without importing modules.

9. **Executing Functions Safely**
   - `101-safe_function.py`: Executes a function safely, handling exceptions by printing errors to stderr.
   - Assumes `fct` is always a function pointer.
   - Returns the function's result, or `None` upon failure.

10. **Matching Bytecode**
    - `102-magic_calculation.py`: A Python function created to match a specific bytecode.

11. **CPython Inspection**
    - `103-python.c`: C functions for inspecting Python lists, bytes, and float objects.
