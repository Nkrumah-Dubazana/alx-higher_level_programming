#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the sum, difference, multiplication of 10 and 5"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
