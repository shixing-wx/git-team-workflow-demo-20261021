"""A small calculator used for a Git collaboration exercise."""
import argparse


def calculate(left, right, operation):
    if operation == "add":
        return left + right
    if operation == "subtract":
        return left - right
    if operation == "multiply":
        return left * right
    if operation == "divide":
        if right == 0:
            raise ValueError("Cannot divide by zero")
        return left / right
    raise ValueError("Unsupported operation")


def main():
    parser = argparse.ArgumentParser(description="A small calculator")
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    args = parser.parse_args()
    try:
        result = calculate(args.left, args.right, args.operation)
    except ValueError as error:
        parser.error(str(error))
    print(result)


if __name__ == "__main__":
    main()
