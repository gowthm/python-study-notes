# 🧬 The Data Model (Dunder Methods)

These are **special methods** (double underscore, "dunder") that hook your class into Python's built-in behavior — things like `print()`, `+`, `len()`, and `==` all defer to them.

| Dunder method | Triggered by | Example |
| :--- | :--- | :--- |
| `__init__` | `MyClass(...)` | Constructor — initializes a new instance |
| `__str__` | `print(obj)` / `str(obj)` | Human-readable description |
| `__repr__` | `repr(obj)` / the REPL | Unambiguous, developer-facing description |
| `__len__` | `len(obj)` | Returns the object's "length" |
| `__eq__` | `obj1 == obj2` | Defines equality between two instances |
| `__add__` | `obj1 + obj2` | Defines the `+` operator |

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

> 📖 **Related**: [`OOP - dataclasses`](file:///d:/python/python-study-notes/OOP%20-%20dataclasses/README.md) covers `@dataclass`, which auto-generates `__init__`, `__repr__`, and `__eq__` for you instead of writing them by hand as shown above.
