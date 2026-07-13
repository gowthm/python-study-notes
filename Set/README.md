# 🎨 Python Sets (set)

A **set** in Python is an unordered collection of unique elements. Sets are mutable, but they can only contain hashable (immutable) items (such as strings, numbers, and tuples). Under the hood, sets are implemented using hash tables, allowing $O(1)$ average-time complexity for membership tests, additions, and deletions.

Think of a set like a collection of items in a bag:
* 🏷️ **Unique**: No duplicate items are allowed.
* 🌪️ **Unordered**: Items do not have a defined index or order of insertion.

---

## 📂 Example Scripts

Here is a guide to the study scripts contained in this directory:

### 1. Basic Set Methods and Operations
* **File**: [set_methods.py](file:///d:/python/python-study-notes/Set/set_methods.py)
* **Description**: Shows how to initialize two sets (representing backend and frontend programming languages), add/remove items, and perform basic set operations.
* **Key Concept**: Duplicate elements added to a set are silently ignored. Removing an item that does not exist using `.remove()` raises a `KeyError` (use `.discard()` to avoid this).

---

## 📐 Mathematical Set Operations

Sets in Python shine when performing standard mathematical operations:

| Operation | Python Method | Operator | Description |
| :--- | :--- | :---: | :--- |
| **Union** | `setA.union(setB)` | `setA \| setB` | All unique items in both sets. |
| **Intersection** | `setA.intersection(setB)` | `setA & setB` | Items present in both sets. |
| **Difference** | `setA.difference(setB)` | `setA - setB` | Items in setA but not in setB. |
| **Symmetric Difference** | `setA.symmetric_difference(setB)` | `setA ^ setB` | Items in either setA or setB but not both. |

---

## ⚡ Set Tips & Best Practices

> [!TIP]
> **Use `.discard()` to Safely Remove Elements**
> Unlike `.remove(item)`, which throws a `KeyError` if the item is not found, `.discard(item)` will fail silently if the item is missing, making your code safer when the existence of an item is uncertain.

> [!NOTE]
> **Performance Edge**
> Membership checks (e.g. `if item in my_set:`) are significantly faster for sets than for lists because they run in $O(1)$ time rather than scanning the entire collection in $O(N)$ time.
