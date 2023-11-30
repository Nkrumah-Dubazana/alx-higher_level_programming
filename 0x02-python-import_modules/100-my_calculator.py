#!/usr/bin/python3

def main():
    """Execute basic arithmetic operations."""
    from arithmetic import plus, minus, times, divide
    import sys

    operators = {"+": plus, "-": minus, "*": times, "/": divide}

    if len(sys.arg) != 4:
        print("Correct usage: ./calculator.py <number1> <operation><number2>")
        sys.exit(1)

        if sys.arg[2] not in operators:
            print("Error: Operator not recognized.  Use +, -, *, or /.")
            sys.exit(1)

        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        operation = sys.argv[2]

        result = operators[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

    if __name__ == "__main__":
        main()
