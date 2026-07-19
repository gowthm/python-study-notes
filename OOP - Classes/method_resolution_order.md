# 🔍 Method Resolution Order (MRO)

**Method Resolution Order (MRO)** is the deterministic sequence Python uses to search for methods or attributes in a class hierarchy.

---

## ⚙️ Core Principles of MRO

Python structures its search order using the **C3 Linearization** algorithm. This framework adheres strictly to three logical constraints:

1. 👶 **Children First**: Python always checks a child class before moving up to its parent classes.
2. ⬅️ **Left-to-Right Priority**: Parent classes are searched in the exact order they are specified in the inheritance tuple.
3. ⚖️ **Monotonicity**: The relative order of parent classes cannot shift across any derived child classes.

---

## 💎 The Diamond Problem Example

The classic "Diamond Problem" occurs when a child class inherits from two parent classes that share a common grandparent.

```python
class A:
    def show(self):
        print("Process A")

class B(A):
    def show(self):
        print("Process B")

class C(A):
    def show(self):
        print("Process C")

class D(B, C):
    pass

obj = D()
obj.show()  # Outputs: Process B
```

### MRO for Class `D`
For the class hierarchy above, Python searches in this order:
`D -> B -> C -> A -> object`