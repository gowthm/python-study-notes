# 🔢 Python List vs. NumPy Array

A quick reference comparing Python's built-in `list` with NumPy's `ndarray` — what they store, how they perform, and *why* NumPy is faster under the hood.

---

## 📊 Feature Comparison

| Feature                 | Python List                          | NumPy Array                                 |
| ------------------------ | ------------------------------------- | --------------------------------------------- |
| Data types               | Can store mixed data types            | Typically stores a single data type           |
| Performance              | Slower for numerical computations     | Much faster for numerical computations        |
| Memory usage              | Higher                                 | More memory-efficient                          |
| Mathematical operations  | Limited                                | Supports vectorized operations                 |
| Dimensions                | Nested lists for multiple dimensions  | Native support for multi-dimensional arrays    |

---

## 🧭 When to Use Each

**Use Python lists when:**
- You need a general-purpose collection.
- Elements may have different data types.
- Your dataset is relatively small.
- You frequently add or remove elements.

**Use NumPy arrays when:**
- Working with numerical data.
- Performing mathematical or statistical operations.
- Handling large datasets.
- Doing scientific computing, machine learning, or data analysis.

---

## 🧱 1. Python List Internally

When you do:

```python
a = [10, 20, 30]
```

A Python list is **not** one continuous block containing the actual integers. Conceptually, memory looks roughly like this:

```
a
│
▼
┌─────────┬─────────┬─────────┐
│ pointer │ pointer │ pointer │
└────┬────┴────┬────┴────┬────┘
     │         │         │
     ▼         ▼         ▼
    10        20        30
 PyObject  PyObject  PyObject
```

The list contains **references/pointers** to Python objects — each integer is itself a separate Python object. So:

```python
a = [10, 20, 30]
```

roughly means:

```
List
 ├── pointer ──> Python integer object 10
 ├── pointer ──> Python integer object 20
 └── pointer ──> Python integer object 30
```

This gives Python lists a lot of flexibility. For example:

```python
a = [10, "hello", 3.14, True]
```

This is totally valid, because the list doesn't require all elements to have the same underlying type.

```python
result = []
for x in lst:
    result.append(x * 2)
```

This loop is executed entirely by the Python interpreter. For one million elements:

```
Python
  │
  ├── get element
  ├── execute Python bytecode
  ├── multiply Python integers
  ├── create/reference result
  ├── append
  │
  ├── get next element
  ├── execute Python bytecode
  ├── multiply
  └── ...
       × 1,000,000
```

---

## 🧮 2. NumPy Array Internally

Now:

```python
import numpy as np

arr = np.array([10, 20, 30])
```

NumPy works very differently. Conceptually:

```
arr
 │
 ▼
┌────┬────┬────┐
│ 10 │ 20 │ 30 │
└────┴────┴────┘
```

The numbers are stored in a **contiguous memory buffer**. For example, with `int64`:

```
Memory address
1000 → 10
1008 → 20
1016 → 30
```

Each integer occupies the same amount of space. NumPy also keeps metadata describing the buffer:

```
NumPy ndarray
│
├── pointer  → data buffer
├── dtype    → int64
├── shape    → (3,)
├── strides  → (8,)
└── ndim     → 1
```

So:

```python
arr.dtype   # int64
arr.shape   # (3,)
```

---

## ⚙️ List Comprehension vs. Vectorized Operation

```python
a = [1, 2, 3, 4]
result = [x * 2 for x in a]
```

Internally, think of it like this — the iteration happens entirely at the **Python interpreter** level:

```
          Your Python code
                 │
                 ▼
        ┌──────────────────┐
        │ Python            │
        │ Interpreter       │
        └────────┬──────────┘
                 │
                 ▼
          Start Python loop
                 │
        ┌────────┴────────┐
        ▼                 │
   get x = 1               │
        │                 │
        ▼                 │
   Python multiply         │
      1 × 2                │
        │                 │
        ▼                 │
   create Python result    │
        │                 │
        └──────► next iteration
```

And this happens again for `2`, `3`, `4`.

Now with NumPy:

```python
import numpy as np

a = np.array([1, 2, 3, 4])
result = a * 2
```

The path is different — Python starts the operation and hands it off to compiled code:

```
          Your Python code
                 │
                 ▼
        ┌──────────────────┐
        │ Python            │
        │ Interpreter       │
        └────────┬──────────┘
                 │  a * 2
                 ▼
        ┌──────────────────┐
        │ NumPy             │
        │ Python API        │
        └────────┬──────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Compiled native   │
        │ NumPy code        │
        │ (mostly C/C++)    │
        └────────┬──────────┘
                 │
                 ▼
          loop over array
          ┌──────┼──────┐
          ▼      ▼      ▼
         1×2    2×2    3×2 ...
                 │
                 ▼
          numeric buffer
```

So Python is still involved — it starts the operation and calls NumPy — but Python does **not** individually interpret every multiplication.

---

## 🎯 The Really Important Distinction

**Python list:**

```
Python → "Give me the next element"
Python → "Multiply it"
Python → "Store it"
Python → "Next element"
Python → "Multiply it"
...
```

**NumPy array:**

```
Python → "NumPy, multiply this entire array by 2."
                 │
                 ▼
          NumPy compiled code
                 │
                 ▼
    loop through millions of numeric elements
```

> [!IMPORTANT]
> Python lists interpret every single operation one element at a time. NumPy hands the *whole* operation off to compiled C code in one call — that's the source of its speed.
