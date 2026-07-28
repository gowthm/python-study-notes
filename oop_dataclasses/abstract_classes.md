# 🏛️ Abstract Classes & Abstract Methods

In Python, `@abstractmethod` is a decorator from the standard `abc` (Abstract Base Class) module that forces child subclasses to implement a specific method. 

If a subclass does not implement the decorated method, Python will prevent instantiation of that subclass at runtime.

---

## 🗺️ Conceptual Analogy

Think of an abstract method as a contract: you are defining a common interface (e.g., all animals must be able to `speak()`), but leaving the actual implementation details up to the specific subclass (e.g., a Dog says "Woof", a Cat says "Meow").

This is equivalent to interfaces or abstract classes in other languages like TypeScript:

```typescript
abstract class Animal {
    abstract speak(): void;
}

class Dog extends Animal {
    speak() {
        console.log("Woof");
    }
}

class Cat extends Animal {
    // Error: Non-abstract class 'Cat' does not implement inherited abstract member 'speak' from class 'Animal'.
}
```

---

## ⚙️ Defining Abstract Classes in Python

To define an abstract class in Python, inherit from the `ABC` helper class, and use the `@abstractmethod` decorator:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

Here:
* **`ABC`** marks `Animal` as an abstract base class.
* **`@abstractmethod`** specifies that every subclass of `Animal` must override and implement the `speak` method.

---

## ⚡ Implementations

### 1. Correct Implementation
Subclasses that implement all abstract methods can be instantiated normally:

```python
class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak())  # Output: Woof
```

### 2. Missing Implementation
Subclasses that fail to implement any abstract method will raise a `TypeError` when instantiation is attempted:

```python
class Cat(Animal):
    pass

cat = Cat()
```

**Output:**
```text
TypeError: Can't instantiate abstract class Cat with abstract method speak
```

> [!NOTE]
> Defining the `Cat` class is syntactically valid in Python, but creating an instance (`Cat()`) is not allowed and throws an error at runtime.

---

## ❓ Why use `pass`?

In abstract method definitions, we write:

```python
@abstractmethod
def speak(self):
    pass
```

`pass` acts as a syntax placeholder because Python requires an indented block inside function bodies. Since abstract classes define interface blueprints rather than actual behaviors, they have no implementation logic.

Alternatively, you could write:

```python
@abstractmethod
def speak(self):
    raise NotImplementedError
```

However, this is redundant because inheriting from `ABC` and using `@abstractmethod` already prevents instantiation and guarantees subclass implementations.

---

## 🔄 Abstract Concept Reference

| Concept | Description |
| :--- | :--- |
| `ABC` | Inherited class that designates a base class as abstract. |
| `@abstractmethod` | Decorator declaring a method that child subclasses are required to implement. |
| **Purpose** | Establishes design blueprints and strict interfaces across classes. |
| **TS Equivalent** | `abstract class` / `abstract method` / `interface` |
| **Benefit** | Catches incomplete subclass APIs early and improves structural design consistency. |
