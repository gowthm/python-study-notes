# 📥 Function Arguments

Notes on positional/keyword arguments, `*args`, and `**kwargs`.

---

## 🧭 The Four Kinds of Argument Passing

Before the star syntax, get the vocabulary straight — there are two sides to every function:

```
   DEFINITION SIDE                       CALL SIDE
   def greet(name, greeting):            greet("Ada", greeting="Hi")
             └──┬──┘                            └─┬─┘  └─────┬─────┘
              parameters                   positional     keyword
                                            argument       argument
```

- **Parameters** are the names in the `def`.
- **Arguments** are the values at the call.
- **Positional** arguments are matched by order. **Keyword** arguments are matched by name.

---

## ⭐ `*args` — Collect the Leftover Positional Arguments

```python
def total(*args):
    print(type(args), args)
    return sum(args)

total(1, 2, 3)      # <class 'tuple'> (1, 2, 3)  →  6
total()             # <class 'tuple'> ()         →  0
```

`args` is a **tuple** — always, even when empty. The name `args` is pure convention; `*values` works identically. The `*` is the operator, the name is yours.

Mixing with normal parameters:

```python
def log(level, *messages):
    for m in messages:
        print(f"[{level}] {m}")

log("INFO", "loading model", "warming cache")
```

Routing diagram:

```
   call:  log("INFO", "loading model", "warming cache")
                 │            │                │
                 ▼            └────────┬───────┘
   def log(level, *messages)           ▼
             │                 messages = ("loading model", "warming cache")
             ▼
        level = "INFO"
```

---

## ⭐⭐ `**kwargs` — Collect the Leftover Keyword Arguments

```python
def configure(**kwargs):
    print(type(kwargs), kwargs)

configure(lr=1e-3, epochs=10)
# <class 'dict'> {'lr': 0.001, 'epochs': 10}
```

`kwargs` is a **dict**, always. Keys are strings.

| Slot              | Syntax              | Can be passed how?          |
| ----------------- | -------------------- | ----------------------------- |
| positional-only    | before `/`            | by position only               |
| standard            | between `/` and `*`   | position or keyword            |
| var-positional      | `*args`               | position only, unlimited       |
| keyword-only        | after `*` or `*args`  | by keyword only                 |
| var-keyword          | `**kwargs`            | keyword only, unlimited         |

---

## ⚠️ The Mutable Default Argument Trap

### 1. The Bug

```python
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['apple', 'banana']   ← 😱 where did apple come from?
print(add_item("cherry"))   # ['apple', 'banana', 'cherry']
```

Most people expect a fresh `[]` on every call. That is not what happens.

### 2. The Mechanism — This Is the Whole Explanation

Default values are evaluated **exactly once**, when the `def` statement runs, and the resulting objects are stored as attributes on the function object.

```
┌──────────────────────────────────────────────────────┐
│  When Python executes the `def` line (import time):  │
│ []  ← this list is created ONE time                  │
│   │                                                   │
│   └──► stored in  add_item.__defaults__ = ([],)      │
└──────────────────────────────────────────────────────┘
                          │
        every call that omits `basket` binds the name
        to that SAME object — no copy is ever made
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   call #1            call #2           call #3
   append("apple")   append("banana")  append("cherry")
        └─────────────────┴─────────────────┘
                          ▼
                 one shared list, mutated 3×
```

### 3. Try It Yourself

```python
def add_items(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_items.__defaults__)   # ([],)
print(add_items("orange"))      # ['orange']
print(add_items("banana"))      # ['orange', 'banana']

print(add_items.__defaults__)   # (['orange', 'banana'],)
```

> [!IMPORTANT]
> Never use a mutable object (`list`, `dict`, `set`) as a default value. Use `None` as the default and create the fresh object inside the function body instead:
> ```python
> def add_item(item, basket=None):
>     if basket is None:
>         basket = []
>     basket.append(item)
>     return basket
> ```
