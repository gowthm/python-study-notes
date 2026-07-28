"""
A simple CLI tool that performs a math operation (sum, minus, multiply,
divide) across a list of numbers, built with argparse.

Usage:
    uv run simple_cli_tool.py multiply 5 6 7 8
"""

import argparse
import sys

parse = argparse.ArgumentParser(description="A simple CLI tool perform math operations")

parse.add_argument(
    "operation",
    choices=['sum', 'minus', 'multiply', 'divide'],
    help="The math operation to perform"
)

parse.add_argument(
    "numbers",
    type=float,
    nargs="+",
    help="List of numbers to operate on"
)

args = parse.parse_args()

result = args.numbers[0]

if args.operation == 'sum':
    result = sum(args.numbers)
elif args.operation == 'minus':
    for num in args.numbers[1:]:
        result -= num
elif args.operation == 'multiply':
    for num in args.numbers[1:]:
        result *= num
elif args.operation == 'divide':
    for num in args.numbers[1:]:
        if num == 0:
            print("Cannot divide by 0")
            sys.exit(0)
        result /= num

print(f"Operation: {args.operation.upper()}")
print(f"Numbers: {args.numbers}")
print(f"Result: {result}")
