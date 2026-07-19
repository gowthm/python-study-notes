# 📦 Python Dataclasses

Introduced in Python 3.7 (PEP 557), the `dataclasses` module provides a decorator and functions to automatically generate special methods (like `__init__()`, `__repr__()`, and `__eq__()`) for custom classes. 

It is designed to eliminate boilerplate code when creating classes that primarily store data.

---

## 📂 Example Scripts & Guides

This directory contains resources illustrating advanced object-oriented design and dataclass features in Python:

### 1. Complete E-Commerce Example
* **File**: [example.py](file:///d:/python/python-study-notes/OOP%20-%20dataclasses/example.py)
* **Description**: A practical script simulating products, customers, and orders using dataclasses, combined with abstract classes for payment processing.

### 2. Abstract Classes & Interfaces
* **Guide**: [abstract_classes.md](file:///d:/python/python-study-notes/OOP%20-%20dataclasses/abstract_classes.md)
* **Description**: Explains Python's `abc` module, defining abstract base classes, and enforcing interface contracts with `@abstractmethod`.

### 3. TypeScript vs. Python Reference
* **Guide**: [ts_vs_py.md](file:///d:/python/python-study-notes/OOP%20-%20dataclasses/ts_vs_py.md)
* **Description**: A side-by-side syntactic mapping of object-oriented concepts from TypeScript to Python.

---

## ⚖️ Standard Class vs. Dataclass

Here is a side-by-side comparison of creating a data-holding class.

### 1. The Standard Way
Writing a standard class requires defining the constructor, string representation, and comparison methods manually:

```python
class Product:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)
```

### 2. The Dataclass Way
Using the `@dataclass` decorator, Python generates all of the above code automatically:

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
```

---

## ⚡ Key Features of Dataclasses

### 1. Auto-Generated Methods
By default, `@dataclass` automatically adds the following methods to your class:
* **`__init__()`**: Constructor that initializes the attributes in the order they are defined.
* **`__repr__()`**: Returns a clean, human-readable string representation of the object (e.g., `Product(name='Laptop', price=999.9, quantity=1)`).
* **`__eq__()`**: Allows comparing objects by comparing their values as a tuple of attributes.

```python
p1 = Product("Laptop", 999.9)
p2 = Product("Laptop", 999.9)

print(p1)          # Output: Product(name='Laptop', price=999.9, quantity=1)
print(p1 == p2)    # Output: True
```

### 2. Default Values
You can assign default values directly to fields:

```python
@dataclass
class User:
    username: str
    role: str = "Member"
```

> [!WARNING]
> **Fields with default values must be defined AFTER fields without default values.** Otherwise, Python will raise a `SyntaxError`.

### 3. Mutable Default Values (`default_factory`)
If you want to use a mutable object (like a list or a dictionary) as a default value, you cannot assign it directly. Instead, you must use `field(default_factory=...)`.

> [!CAUTION]
> **Incorrect (raises ValueError):**
> ```python
> @dataclass
> class Group:
>     members: list = []  # ValueError: mutable default <class 'list'> is not allowed
> ```

> [!TIP]
> **Correct:**
> ```python
> from dataclasses import dataclass, field
> 
> @dataclass
> class Group:
>     name: str
>     members: list = field(default_factory=list)
> ```

### 4. Read-Only / Immutable Dataclasses (`frozen=True`)
To make a dataclass read-only and prevent modifying its attributes after creation, set `frozen=True`.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(10, 20)
# p.x = 15  # Raises FrozenInstanceError: cannot assign to field 'x'
```

---

## 🔄 Summary of Main Options

The `@dataclass` decorator accepts several boolean parameters to customize class generation:

| Option | Default | Description |
| :--- | :---: | :--- |
| `init` | `True` | Generates the `__init__()` method. |
| `repr` | `True` | Generates the `__repr__()` method. |
| `eq` | `True` | Generates the `__eq__()` method for value comparisons. |
| `order` | `False` | Generates comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`). |
| `unsafe_hash` | `False` | Forces the generation of a `__hash__()` method. |
| `frozen` | `False` | Makes the object immutable and hashable if `frozen=True`. |
