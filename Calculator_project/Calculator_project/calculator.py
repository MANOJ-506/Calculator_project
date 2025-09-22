#!/usr/bin/env python3
"""
Simple CLI Calculator
- Implements add, subtract, multiply, divide
- Runs in a loop until exit
- Validates input and handles errors
"""

from typing import Optional, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> Optional[Number]:
    """Prompt user for a numeric input. Returns None if user cancels."""
    while True:
        val = input(prompt).strip()
        if val.lower() in ("q", "quit"):
            return None
        try:
            # parse as float first, then convert to int if integer value
            num = float(val)
            if num.is_integer():
                return int(num)
            return num
        except ValueError:
            print("Invalid number. Try again (or type 'q' to cancel).")


def print_menu() -> None:
    """Display calculator menu."""
    print("\n==== Simple CLI Calculator ====")
    print("1) Add (+)")
    print("2) Subtract (-)")
    print("3) Multiply (*)")
    print("4) Divide (/)")
    print("5) View history")
    print("0) Exit")
    print("===============================\n")


def main() -> None:
    """Main program loop."""
    history: list[str] = []
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        print_menu()
        choice = input("Enter choice (0-5): ").strip()

        if choice == "0":
            print("Exiting... Goodbye!")
            break

        if choice == "5":
            if not history:
                print("No history yet.")
            else:
                print("\n--- History ---")
                for i, record in enumerate(history, 1):
                    print(f"{i}. {record}")
            continue

        if choice not in operations:
            print("Invalid option. Try again.")
            continue

        symbol, func = operations[choice]

        a = get_number("Enter first number (or 'q' to cancel): ")
        if a is None:
            continue

        b = get_number("Enter second number (or 'q' to cancel): ")
        if b is None:
            continue

        try:
            result = func(a, b)
            # normalize float like 5.0 -> 5
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            expression = f"{a} {symbol} {b} = {result}"
            print("Result:", expression)
            history.append(expression)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
