# 🛡️ Metadata Preservation Guide

## Why should we use functools.wraps?

**Answer:**

`functools.wraps` preserves the original function's metadata when writing decorators. Without it, the decorated function loses its original name, docstring, annotations, and other metadata because it is replaced by the wrapper function. This is important for debugging, logging, documentation generation, introspection, and frameworks that inspect functions.


```python
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)

    return wrapper

print(greet.__doc__)
```


## What does @wraps(func) actually do?

```python
wrapper.__name__ = func.__name__
wrapper.__doc__ = func.__doc__
wrapper.__module__ = func.__module__
wrapper.__annotations__ = func.__annotations__
wrapper.__wrapped__ = func
...
```


## Visual Representation

### Without @wraps
```text
greet
 │
 ▼
wrapper
 │
 ├── __name__ = "wrapper"
 ├── __doc__ = None
 ├── __module__ = current module
 │
 ▼
Original greet()
```

### With @wraps
```text
greet
 │
 ▼
wrapper
 │
 ├── __name__ = "greet"
 ├── __doc__ = "Greets the user"
 ├── __module__ = original module
 ├── __wrapped__ = original greet
 │
 ▼
Original greet()
```

> [!NOTE]
> Notice that the function still executes through wrapper. Only its metadata is copied.