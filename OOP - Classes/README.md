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
