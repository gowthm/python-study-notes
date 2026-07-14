# ⚡ Python Lambda Functions (Anonymous Functions)

A **Lambda Function** is a small, nameless (anonymous) function defined using the `lambda` keyword. Unlike standard functions defined with `def`, lambda functions are written in a single line, can accept any number of arguments, but evaluate and return only a single expression.

Lambda functions are commonly used as short-lived, one-off operations with higher-order functions like `map()`, `filter()`, `sorted()`, and `max()`.

---

## 🗺️ Conceptual Overview

Here is the general structure of a lambda function:

![Lambda Concept Diagram](https://media.geeksforgeeks.org/wp-content/uploads/20260123120726076161/lambda.webp)

---

## 📂 Example Scripts & Guides

This directory includes resources explaining how to implement and trace lambda functions:

### 1. Lambda Basics and Higher-Order Functions
* **File**: [lambda_basics.py](file:///d:/python/python-study-notes/lambda_functions/lambda_basics.py)
* **Description**: Python examples demonstrating the usage of lambdas inside `map()`, `filter()`, and `sorted()`.

### 2. Execution Flow Tracing
* **File**: [lambda_execution_flow.md](file:///d:/python/python-study-notes/lambda_functions/lambda_execution_flow.md)
* **Description**: A step-by-step layout of variables assignment and evaluation during a lambda invocation.

---

## ⚖️ `def` vs. `lambda`

| Feature | Standard Function (`def`) | Lambda Function (`lambda`) |
| :--- | :--- | :--- |
| **Naming** | Has a defined function name | Anonymous (often nameless or assigned to a variable) |
| **Statements** | Allows multiple statements, loops, and conditions | Limited to a single expression only |
| **Return Behavior** | Requires an explicit `return` statement | Automatically returns the value of the expression |
| **Use Case** | Best for complex, reusable logic | Best for concise, short-lived, one-off operations |
| **Readability** | Easier to document with docstrings and debug | Cleaner for inline functions (like keys in `sorted()`) |

---

## ⚠️ When to Avoid Lambdas

> [!WARNING]
> **Do Not Overuse Lambdas**
> If your function logic requires loops, multiple branches, or complex exception handling, always use standard `def` functions. Lambdas should remain small, single-purpose, and simple to ensure readability is not compromised.