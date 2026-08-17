# 🔒 Python Closures

A **closure** is a function that remembers variables from the scope where it was defined, even after that scope has finished executing.

---

## 🗺️ Where Closures Live (LEGB Scope)

Python resolves a name by searching outward through four scopes, in this order — the first match wins:

```
┌─────────────────────────────────────────────────────────────┐
│ B — Builtins        len, print, range                       │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ G — Global (module level)                               │ │
│ │ ┌──────────────────────────────┐                        │ │
│ │ │ E — Enclosing function       │   ← closures live here │ │
│ │ │ ┌──────────────────────────┐ │                        │ │
│ │ │ │ L — Local (current call) │ │                        │ │
│ │ │ └──────────────────────────┘ │                        │ │
│ │ └──────────────────────────────┘                        │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

     first match wins; search stops there
```

---

## 💡 Basic Example

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}"
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))
```

`greet` remembers `greeting` from `make_greeter`'s scope, even though `make_greeter` already finished running.

---

## 🧠 What Happens Under the Hood

```
make_greeter("Hello")
        │  creates a cell holding "Hello"
        ▼
   ┌───────────────┐
   │ cell: "Hello" │
   └───────▲───────┘
           │  referenced by
   ┌───────┴──────────────────────────────────────┐
   │ function `greet`                             │
   │   __code__                                   │
   │   __closure__  →  (<cell ...: str "Hello">,) │
   └──────────────────────────────────────────────┘
```

The frame of `make_greeter` is destroyed, but the **cell** is kept alive by the reference held in `greet.__closure__`.

---

## 🔄 `nonlocal` — Rebinding an Enclosing Variable

Assigning to a name inside a nested function creates a *new local* by default — it does not touch the enclosing variable. `nonlocal` fixes that by saying "this name belongs to the enclosing function":

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count       # ✅ rebind the enclosing variable
        count += 1
        return count
    return increment

c = make_counter()
print(c(), c(), c())   # 1 2 3
```

| Keyword    | Rebinds a name in...                     |
| ---------- | ----------------------------------------- |
| *(none)*   | the local scope (creates a new local)      |
| `nonlocal` | the nearest enclosing function scope       |
| `global`   | the module scope                           |

---

## ⚖️ Closure vs. Class

A closure is a lightweight object. These two are near-equivalent:

```python
# closure                          # class
def make_counter():                class Counter:
    n = 0                              def __init__(self):
    def inc():                             self.n = 0
        nonlocal n                     def __call__(self):
        n += 1                             self.n += 1
        return n                           return self.n
    return inc
```

> [!NOTE]
> Both hold onto state between calls — the closure keeps it in a hidden **cell**, the class keeps it as an **instance attribute**.
