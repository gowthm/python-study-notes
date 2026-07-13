# 📖 Python Dictionaries (dict)

A **dictionary** in Python is an unordered (preserved insertion order from 3.7+), mutable collection of **key-value pairs**. It is implemented as a hash table, providing extremely fast $O(1)$ average-time complexity for lookups, insertions, and deletions.

Think of a dictionary like a real-world phone book or glossary:
* 🔑 **Key**: The unique lookup term (must be hashable/immutable, e.g., string, number, tuple).
* 📄 **Value**: The corresponding data associated with the key (can be any type and duplicate values are allowed).

---

## 📂 Example Scripts

Here is a guide to the study scripts contained in this directory:

### 1. Basic CRUD Operations
* **File**: [dict_crud_basics.py](file:///d:/python/python-study-notes/Dict/dict_crud_basics.py)
* **Description**: Demonstrates how to initialize a dictionary, read elements by key, update values, and delete key-value pairs using the `.pop()` method.
* **Key Concept**: Accessing a key directly using `dict[key]` will raise a `KeyError` if the key does not exist.

### 2. Frequency Counting & Safely Fetching Values
* **File**: [dict_frequency_counter.py](file:///d:/python/python-study-notes/Dict/dict_frequency_counter.py)
* **Description**: Demonstrates counting frequency of items in a list using the `.get(key, default)` method to avoid manual membership checks.
* **Key Concept**: Using `.get(key, default)` returns the value if the key exists; otherwise, it returns the specified default value (e.g., `0`), preventing `KeyError`.

### 3. Shopping Cart Simulation
* **File**: [product_checkout.py](file:///d:/python/python-study-notes/Dict/product_checkout.py)
* **Description**: A mini checkout simulation using dictionaries. It tracks product prices, accepts incoming items with custom quantities using a helper function, and calculates the total checkout price.
* **Key Concept**: Iterating over dictionary items using `.items()` to access both keys and values simultaneously.

---

## ⚡ Dictionary Tips & Best Practices

> [!TIP]
> **Use `.get()` for Safe Lookups**
> Avoid checking `if key in dict:` before fetching values. Instead, use `dict.get(key, default_value)` to simplify your code and make it more pythonic.

> [!NOTE]
> **Dictionary Iteration Options**
> * To iterate over keys: `for key in my_dict:` (or `my_dict.keys()`)
> * To iterate over values: `for val in my_dict.values():`
> * To iterate over both: `for key, val in my_dict.items():`
