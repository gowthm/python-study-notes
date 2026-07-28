# 🏛️ Python OOP: Classes & Objects

Object-Oriented Programming (OOP) is a programming paradigm that uses **classes** and **objects** to structure software into reusable, modular blueprints.

---

## 📂 Example Scripts & Guides

This directory contains resources illustrating core Object-Oriented Programming (OOP) concepts in Python:

### 1. Multiple Inheritance
* **File**: [multiple_inheritance.py](file:///d:/python/python-study-notes/OOP%20-%20Classes/multiple_inheritance.py)
* **Description**: Demonstrates how a subclass can inherit from multiple parent classes (e.g., `Smartphone` inheriting from both `Camera` and `Phone`).

### 2. Using `super()`
* **File**: [super_method.py](file:///d:/python/python-study-notes/OOP%20-%20Classes/super_method.py)
* **Description**: Illustrates calling parent class constructors and methods using Python's built-in `super()` function.

### 3. Method Resolution Order (MRO)
* **Guide**: [method_resolution_order.md](file:///d:/python/python-study-notes/OOP%20-%20Classes/method_resolution_order.md)
* **Description**: Explains Python's MRO, the C3 Linearization algorithm, and how Python resolves the classic "Diamond Problem".

### 4. `@classmethod` vs `@staticmethod`
* **Guide**: [classmethod_staticmethod.md](file:///d:/python/python-study-notes/OOP%20-%20Classes/classmethod_staticmethod.md)
* **Description**: Breaks down the difference between instance methods, class methods, and static methods, and when to use each.

### 5. The `@property` Decorator
* **Guide**: [property.md](file:///d:/python/python-study-notes/OOP%20-%20Classes/property.md)
* **File**: [property_example.py](file:///d:/python/python-study-notes/OOP%20-%20Classes/property_example.py)
* **Description**: Shows how to use getters and setters to validate data while keeping attribute-style access.

### 6. Composition (`Car` ➜ `Engine`)
* **File**: [example_composition.py](file:///d:/python/python-study-notes/OOP%20-%20Classes/example_composition.py)
* **Description**: A practical "has-a" example — a `Car` is composed of an `Engine` instead of inheriting from it.

### 7. The Data Model (Dunder Methods)
* **Guide**: [data_model.md](file:///d:/python/python-study-notes/OOP%20-%20Classes/data_model.md)
* **Description**: A quick reference for Python's special ("dunder") methods that hook a class into built-in language behavior.

---

## 🧱 The Constructor: `__init__()`

The `__init__()` method is Python's constructor. It is automatically called when a new instance of a class is created, allowing you to initialize the object's attributes.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## ⚙️ Methods in Classes

Methods are functions defined inside a class that describe the behaviors of the objects created from that class. The first parameter of an instance method is always `self`.

```python
class Car:
    def start(self):
        print("Starting the car...")

# Usage:
car = Car()
car.start()  # Output: Starting the car...
```

---

## ❓ Understanding `self`

In Python, `self` is a reference to the current instance of the class. It is used to access variables and methods associated with the specific object.

### How `self` Works Under the Hood

When you create an object and call a method:

```python
s1 = Student("Alice")
```

Python automatically translates this to:
```python
Student.__init__(s1, "Alice")
```

Notice that `s1` is passed as the first argument. Inside the method, that instance is referenced as `self`.

* **`self`** refers to the specific object `s1`.
* **`name`** is the value `"Alice"`.
* **`self.name = name`** creates an attribute called `name` on the `s1` object (equivalent to `s1.name = "Alice"`).

```python
print(s1.name)  # Output: Alice
```

### Why is `self` Needed?

It allows each object to maintain and store its own independent data:

```python
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)  # Output: Alice
print(s2.name)  # Output: Bob
```

* When creating `s1`, `self` refers to `s1`.
* When creating `s2`, `self` refers to `s2`.

### Is `self` a Keyword?

> [!NOTE]
> **No, `self` is not a Python keyword.** It is simply a strong convention. You could name it `this` or anything else:
> ```python
> class Student:
>     def __init__(this, name):
>         this.name = name
> ```
> However, using anything other than `self` is highly discouraged as it violates PEP 8 standards and reduces code readability for other developers.

---

## 🧩 Composition

**Composition** is an OOP concept that models a **"has-a"** relationship by combining simpler objects to build more complex ones. Instead of inheriting properties from a parent class (as with inheritance), a composite class delegates responsibility by storing instances of other classes as its attributes.

> 📖 **Reference**: [An Overview of Inheritance in Python – Real Python](https://realpython.com/inheritance-composition-python/#an-overview-of-inheritance-in-python)

### 🤔 Why Use Composition?

* 🔄 **Flexibility**: You can swap out component behaviors dynamically at runtime.
* 🔗 **Low Coupling**: It keeps classes independent and prevents breaking changes from cascading down a deep hierarchy.
* 🎯 **Separation of Concerns**: Each class handles exactly one responsibility.

### ⚖️ Composition vs. Inheritance

Many developers lean toward the design principle **"Favor composition over inheritance."** A quick breakdown helps explain why:

* **Inheritance ("Is-A")**: A `Car` **is a** `Vehicle`. It creates a tight architectural bond where the child automatically pulls in all traits from the parent.
* **Composition ("Has-A")**: A `Car` **has an** `Engine`. It builds systems out of individual, highly swappable building blocks rather than a rigid family tree.

#### 📊 Visual Comparison

**Inheritance** ("is-a"):

![Diagram showing basic inheritance in Python](https://files.realpython.com/media/ic-basic-inheritance.f8dc9ffee4d7.jpg)

**Composition** ("has-a"):

![Diagram showing basic composition in Python](https://files.realpython.com/media/ic-basic-composition.8a15876f7db2.jpg)

> 📖 **Reference**: [Composition in Python – Real Python](https://realpython.com/inheritance-composition-python/#composition-in-python)

See [example_composition.py](file:///d:/python/python-study-notes/OOP%20-%20Classes/example_composition.py) for a runnable `Car` + `Engine` example.

---

## 🔄 Python vs. JavaScript/TypeScript

If you are coming from JavaScript or TypeScript, here is how the class concepts map to Python:

| JavaScript / TypeScript | Python |
| :--- | :--- |
| `class User` | `class User:` |
| `constructor()` | `__init__()` |
| `this` | `self` |
| `extends` | `class Dog(Animal):` |
| `super()` | `super()` |
| `new User()` | `User()` |
| `this.name` | `self.name` |
| Instance methods | Instance methods |
| Static methods | `@staticmethod` |
| Class properties | Class variables |
