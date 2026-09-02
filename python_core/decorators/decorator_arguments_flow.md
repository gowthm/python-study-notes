# Python Decorator Execution Flow (With Arguments)

## Program

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before calling function")

        result = func(*args, **kwargs)

        print("After calling function")

        return result

    return wrapper


@decorator
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


result = add(10, 20)
print(result)
```

---

# Step 1: Python Creates the `decorator` Function

Python first reads:

```python
def decorator(func):
```

At this point, **nothing is executed**. Python only creates the `decorator` function object and stores it in memory.

Memory:

```
decorator
    │
    ▼
Function Object
```

---

# Step 2: Python Creates the Original `add` Function

Python reads:

```python
def add(a, b):
```

Now the original `add()` function is created.

Memory:

```
decorator ───► decorator()

add ─────────► Original add()
```

The `add()` function is a normal function that adds two numbers.

---

# Step 3: Python Encounters `@decorator`

Python sees:

```python
@decorator
def add(a, b):
```

Python automatically converts this into:

```python
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

add = decorator(add)
```

This means Python immediately calls:

```python
decorator(add)
```

---

# Step 4: Execute `decorator(add)`

Inside the decorator,

```python
func
```

receives the **original `add` function**.

```
func
 │
 ▼
Original add()
```

Python now creates another function:

```python
def wrapper(*args, **kwargs):
```

At this point **wrapper is only created**, not executed.

---

# Step 5: Return the Wrapper Function

Decorator executes:

```python
return wrapper
```

Notice there are **no parentheses**.

This means:

- Python returns the **wrapper function object**
- Python does **not execute** `wrapper()`

Now the returned wrapper replaces the original function.

Internally:

```python
add = wrapper
```

Memory becomes:

```
add
 │
 ▼
wrapper()
 │
 ▼
func
 │
 ▼
Original add()
```

The original `add()` still exists because `wrapper` remembers it through `func`.

---

# Step 6: Call `add(10, 20)`

Program executes:

```python
result = add(10, 20)
```

But remember:

```
add == wrapper
```

Therefore Python actually executes:

```python
wrapper(10, 20)
```

---

# Step 7: Store Arguments

Inside wrapper,

```python
args = (10, 20)
kwargs = {}
```

Explanation:

- `10` and `20` are positional arguments.
- They are packed into the tuple `args`.
- No keyword arguments were passed, so `kwargs` is an empty dictionary.

---

# Step 8: Execute First Statement

Wrapper executes:

```python
print("Before calling function")
```

Output:

```
Before calling function
```

---

# Step 9: Call the Original Function

Wrapper executes:

```python
result = func(*args, **kwargs)
```

Here,

```
func
```

still points to the original `add`.

Python unpacks:

```python
func(*args)
```

which becomes:

```python
func(10, 20)
```

This is actually:

```python
add(10, 20)
```

Original function executes:

```python
print(f"Adding {a} + {b}")
```

Output:

```
Adding 10 + 20
```

Original function returns:

```python
30
```

Now inside wrapper,

```python
result = 30
```

---

# Step 10: Execute Next Statement

Wrapper executes:

```python
print("After calling function")
```

Output:

```
After calling function
```

---

# Step 11: Return Result

Wrapper executes:

```python
return result
```

which returns:

```python
30
```

Now,

```python
result = add(10,20)
```

becomes

```python
result = 30
```

---

# Step 12: Print Result

Program executes:

```python
print(result)
```

Output:

```
30
```

---

# Complete Execution Flow

```
Program Starts
      │
      ▼
Create decorator()
      │
      ▼
Create original add()
      │
      ▼
@decorator
      │
      ▼
add = decorator(add)
      │
      ▼
func = original add()
      │
      ▼
Create wrapper()
      │
      ▼
return wrapper
      │
      ▼
add → wrapper
      │
      ▼
add(10,20)
      │
      ▼
wrapper(10,20)
      │
      ├── args = (10,20)
      ├── kwargs = {}
      ├── print("Before calling function")
      ├── func(*args, **kwargs)
      │        │
      │        ▼
      │   Original add(10,20)
      │        │
      │        ├── print("Adding 10 + 20")
      │        └── return 30
      │
      ├── print("After calling function")
      └── return 30
      │
      ▼
print(result)
```

---

# Final Output

```
Before calling function
Adding 10 + 20
After calling function
30
```

---

# Important Notes

- `@decorator` is equivalent to:

```python
add = decorator(add)
```

- `func` stores a reference to the **original function**.

- `wrapper` is the **new function** that replaces the original one.

- `return wrapper` returns the function itself; it does **not** execute it.

- After decoration:

```
add
 │
 ▼
wrapper()
 │
 ▼
func
 │
 ▼
Original add()
```

- Calling:

```python
add(10,20)
```

actually executes:

```python
wrapper(10,20)
```

- Inside `wrapper`, the original function is called using:

```python
func(*args, **kwargs)
```

- `*args` packs all positional arguments into a tuple.

- `**kwargs` packs all keyword arguments into a dictionary.

- Using `func(*args, **kwargs)` unpacks those arguments and forwards them to the original function.

This is why one decorator can work with **any function**, regardless of how many positional or keyword arguments it accepts.