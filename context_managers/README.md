# 📦 Python Context Managers (`with`)

A **Context Manager** is a Python object designed to manage resource allocation and release. By implementing the context management protocol—consisting of the `__enter__()` and `__exit__()` methods—it allows you to use the `with` statement to ensure that resources (like file streams, database connections, sockets, or threads) are cleaned up properly, even if exceptions are raised during execution.

---

## 🤷 Why not just use `try...finally`?

While `try...finally` blocks work, they require repeating resource management and cleanup logic in every location they are used. 

Context managers:
* 🛡️ **Encapsulation**: Put setup and cleanup logic in one place.
* 🧹 **Readability**: Simplify code with clean `with` syntax, eliminating nested boilerplate.
* 🔒 **Safety**: Guarantee resource cleanup and exit execution safely.

---

## 📂 Example Scripts

### 1. Socket Connection Simulation (Without vs. With Context Manager)
* **File**: [socket_context_manager.py](file:///d:/python/python-study-notes/context_managers/socket_context_manager.py)
* **Description**: Contrast manual socket setup/teardown using `try/finally` against clean resource management with a `with` statement.

### 2. Custom Execution Timer
* **File**: [timer_context_manager.py](file:///d:/python/python-study-notes/context_managers/timer_context_manager.py)
* **Description**: A custom class-based context manager `Timer` that tracks and prints the execution duration of any code block inside it.

---

## ⚙️ Execution Flow Protocol

Here is what happens step-by-step when executing a `with` block:

```text
       with MyContext() as obj:
           do_something()
                 │
                 ▼
          [ Create Object ]
                 │
                 ▼
         [ Call __enter__() ]
                 │
                 ▼
   [ Assign returned value to 'obj' ]
                 │
                 ▼
        [ Execute with-block ]
                 │
                 ▼
            Exception?
             ├── No  ──► Call __exit__(None, None, None)
             └── Yes ──► Call __exit__(exc_type, exc_value, traceback)
                 │
                 ▼
        [ Cleanup Resources ]
                 │
                 ▼
       [ Program Continues ]
```

---

## ⚡ Context Manager Tips & Best Practices

> [!TIP]
> **Use the `contextlib` library**
> Instead of writing full classes with `__enter__` and `__exit__`, you can create a generator-based context manager using the `@contextmanager` decorator from Python's standard `contextlib` module:
> ```python
> from contextlib import contextmanager
> 
> @contextmanager
> def open_file(name):
>     f = open(name, 'r')
>     try:
>         yield f
>     finally:
>         f.close()
> ```