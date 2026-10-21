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
        return left / right
    raise ValueError("Unsupported operation")


def main():
    parser = argparse.ArgumentParser(description="A small calculator")
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    args = parser.parse_args()
    print(calculate(args.left, args.right, args.operation))


if __name__ == "__main__":
    main()
