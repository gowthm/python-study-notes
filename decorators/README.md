# 🎀 Python Decorators

A **Decorator** is a design pattern in Python that allows you to extend or modify the behavior of a function or class without permanently modifying its source code. 

In Python, functions are **first-class citizens**, meaning they can be passed around as arguments, returned from other functions, and assigned to variables. A decorator is simply a function that takes another function as an argument, wraps its execution, and returns a new function (the wrapper).

---

## 🗺️ Conceptual Flow

Here is a visual representation of how decorators wrap your functions:

![Decorators Flow](file:///d:/python/python-study-notes/decorators/decorators_flow.png)

---

## 📂 Example Scripts & Guides

This directory contains resources illustrating decorators from basic syntax to execution mechanics:

### 1. Basic Decorator Syntax
* **File**: [decorator_basics.py](file:///d:/python/python-study-notes/decorators/decorator_basics.py)
* **Description**: Shows a minimal decorator implementation that wraps a custom function to print messages.

### 2. Under-the-Hood Mechanics
* **File**: [decorator_mechanics.py](file:///d:/python/python-study-notes/decorators/decorator_mechanics.py)
* **Description**: A deep-dive script demonstrating how Python translates `@decorator` syntax to `hello = decorator(hello)`. It shows how the function name gets rebound to the wrapper.

### 3. Detailed Execution Tracing (With Arguments)
* **Guide**: [decorator_arguments_flow.md](file:///d:/python/python-study-notes/decorators/decorator_arguments_flow.md)
* **Description**: A step-by-step walkthrough explaining memory allocation, parameter handling (`*args`, `**kwargs`), and execution flow when invoking decorated functions with arguments.

---

## ⚡ Decorators in a nutshell

> [!NOTE]
> When you write:
> ```python
> @my_decorator
> def my_func():
>     pass
> ```
> Python compiles it as:
> ```python
> my_func = my_decorator(my_func)
> ```
