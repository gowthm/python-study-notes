# 🧬 The Data Model (Dunder Methods)

These are **special methods** (double underscore, "dunder") that hook your class into Python's built-in behavior — things like `print()`, `+`, `len()`, and `==` all defer to them.

| Dunder method | Triggered by | Example |
| :--- | :--- | :--- |
| `__str__` | `print(obj)` / `str(obj)` | Human-readable description |
| `__len__` | `len(obj)` | Returns the object's "length" |
| `__add__` | `obj1 + obj2` | Defines the `+` operator |

> ➡️ **Moved**: `__init__`, `__repr__`, and `__eq__` are covered in [`oop_dataclasses/README.md`](file:///d:/python/python-study-notes/oop_dataclasses/README.md#1-auto-generated-methods) instead, since `@dataclass` auto-generates exactly those three — no need to explain them twice.

```python
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages


b = Book("Dune", 412)
print(b)       # Output: Dune (412 pages)   -> uses __str__
print(len(b))  # Output: 412                -> uses __len__
```

> 🚧 More dunder methods and examples to be added here as they're covered.
