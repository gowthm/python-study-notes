# 🛠️ Python Functions (`def`)

In Python, a **Function** is a reusable block of organized, executable code that is designed to perform a single, related action. Functions provide better modularity for your application and promote high code reusability.

---

## 📺 The TV Remote Analogy

To understand how functions work as objects vs. when they execute, think of a function like a television remote control:

> [!NOTE]
> **Function Reference vs. Execution**
> * 📲 **`remote`**: You are holding the physical remote. This represents the **function object** itself (its reference/instruction manual).
> * 🔘 **`remote()`**: You press the power button. This represents **executing/calling** the function (performing the actual work).

Therefore:
* `my_function` is the reference (the instruction manual).
* `my_func()` is the invocation (doing the work).

---

## 📂 Example Scripts & Guides

This directory includes resources explaining functions and advanced metadata preservation:

### 1. Function Chaining & Calls
* **Referenced in**: `firstFunc` and `secondFunc` are basic examples showing how a function can call another function and return its value.

### 2. Metadata Preservation with `functools.wraps`
* **Script File**: [metadata_preservation.py](file:///d:/python/python-study-notes/functions/metadata_preservation.py)
* **Description**: Shows how custom decorators can accidentally overwrite function docstrings and names, and how to use `@wraps(func)` to preserve them.

### 3. Introspection and Wraps Explanation
* **Guide**: [metadata_preservation_guide.md](file:///d:/python/python-study-notes/functions/metadata_preservation_guide.md)
* **Description**: A comprehensive visual and text guide explaining why metadata preservation is critical for debugging, framework code, and documentation.