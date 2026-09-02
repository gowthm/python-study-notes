# 🔄 Python Iterators

An **Iterator** is a stateful object that remembers its current position during iteration and returns the next element when requested. It is the underlying mechanism that drives all looping constructs in Python.

---

## 🗺️ Conceptual Overview

Here is a visual map of how Iterables and Iterators relate to one another in Python:

![Iterators Concept Diagram](file:///d:/python/python-study-notes/iterators/iterators.jpg)

---

## 💡 Iterable vs. Iterator

To master Python loops, it is essential to distinguish between these two concepts:

1. **Iterable**: 
   * Any object that you can loop over (e.g., Lists, Tuples, Sets, Dictionaries, Strings).
   * It implements the `__iter__()` method, which is called by the `iter()` function to return a new iterator.
2. **Iterator**:
   * The actual helper engine that fetches elements one-by-one.
   * It implements the **Iterator Protocol**, which requires two methods:
     * `__iter__()`: Returns the iterator object itself.
     * `__next__()`: Returns the next item in line. When no elements remain, it must raise a `StopIteration` exception to terminate the loop.

---

## 📂 Example Scripts & Comparisons

### 1. Custom Iterator Class
* **File**: [count_up_to.py](file:///d:/python/python-study-notes/iterators/count_up_to.py)
* **Description**: Shows how to construct a custom iterator class from scratch to count from 1 up to a specified limit.

### Code Implementation
```python
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current
```

---

## ⚙️ How the `for` Loop Works Under the Hood

When you write a loop like `for x in something:`, Python executes the following steps behind the scenes:

1. **Obtains an Iterator**: It calls `iterator = iter(something)` (which internally calls `something.__iter__()`).
2. **Retrieves Items**: It repeatedly calls `next(iterator)` (which internally calls `iterator.__next__()`) and assigns the result to `x`.
3. **Catches StopIteration**: When the iterator runs out of elements, it raises `StopIteration`. The `for` loop catches this exception and exits gracefully without raising any errors.

---

## 🎯 Summary Comparison (In a nutshell)

> [!IMPORTANT]
> **The Three Patterns in One Sentence Each:**
> * 🏃‍♂️ **Regular function**: Runs from top to bottom in one shot and hands back the whole result at the end.
> * 🛠️ **Iterator class**: A hand-built object with `__iter__` and `__next__` methods; you write all the state management yourself.
> * ⚡ **Generator function**: Looks like a regular function but has `yield` in it; Python automatically turns it into an iterator that pauses and resumes.