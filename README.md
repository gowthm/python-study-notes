# 🐍 Python Study Notes

Welcome to the Python Study Notes repository! This repository contains a collection of well-documented study guides, conceptual explanations, and clean Python scripts demonstrating core language features.

---

## 🗺️ Topics Index

Explore the different study folders below:

| Topic | Description | Key Subconcepts | Documentation Link |
| :--- | :--- | :--- | :---: |
| **Functions** | Modularity and metadata preservation | TV Remote Analogy, `functools.wraps` | [View Guide](file:///d:/python/python-study-notes/functools_wrap/README.md) |
| **Decorators** | Extending functions without source edits | Rebinding (`hello = decorator(hello)`), wrappers, args flow | [View Guide](file:///d:/python/python-study-notes/decorators/README.md) |
| **Context Managers** | Automated setup and cleanup operations | `with` block execution protocol, custom timers | [View Guide](file:///d:/python/python-study-notes/context_managers/README.md) |
| **Dictionaries** | Hash-table based key-value collection | CRUD, `.get()` default value lookup, loops | [View Guide](file:///d:/python/python-study-notes/dict/README.md) |
| **Sets** | Unordered collection of unique items | `.add()`, `.discard()`, Union, Intersection, Difference | [View Guide](file:///d:/python/python-study-notes/set/README.md) |
| **Iterators** | Stateful looping engine behind `for` loops | Iterable vs. Iterator, Iterator Protocol, `StopIteration` | [View Guide](file:///d:/python/python-study-notes/iterators/README.md) |
| **Generators** | Memory-efficient lazy evaluation | `yield` vs. `return`, local state retention | [View Guide](file:///d:/python/python-study-notes/generator/README.md) |
| **Lambda Functions** | Small anonymous one-expression functions | `map()`, `filter()`, `sorted(key=...)` | [View Guide](file:///d:/python/python-study-notes/lambda_functions/README.md) |
| **OOP — Classes** | Core class concepts | `self`, `super()`, MRO, `@property`, `@classmethod`/`@staticmethod`, composition, dunder methods | [View Guide](file:///d:/python/python-study-notes/oop_classes/README.md) |
| **OOP — Dataclasses** | Boilerplate-free data-holding classes | `@dataclass`, `field(default_factory=...)`, `frozen=True`, abstract classes | [View Guide](file:///d:/python/python-study-notes/oop_dataclasses/README.md) |
| **Exception Handling** | The `requests` library's exception hierarchy | `RequestException`, `HTTPError`, `Timeout`, `ConnectionError` | [View Guide](file:///d:/python/python-study-notes/exception/exception_hierarchy.md) |
| **NumPy** | Numerical arrays and vectorized computing | `ndarray`, broadcasting, universal functions, indexing | [View Guide](file:///d:/python/python-study-notes/numpy/README.md) |
| **Python Internals** | What's happening in memory as code runs | Call stack, heap, step-through visualizer | [View Guide](file:///d:/python/python-study-notes/internal_python/README.md) |
| **Study Scripts** | Standalone networking & CLI practice scripts | `http.server`, `requests`, `argparse` | [View Guide](file:///d:/python/python-study-notes/study_scripts/README.md) |

> 🚧 **Scaffolded, not yet written**: `arguments/`, `async_python/`, `type_hints/` are placeholder folders reserved for future topics.

---

## 🛠️ General Best Practices for Python Study

* 🧪 **Hands-on Experimentation**: Each topic guide lists associated Python scripts. Run them locally to see how standard inputs and edge cases are handled.
* 📦 **Avoid Global State**: Encapsulate logic inside clean functions and keep variables localized.
* 📈 **Performance Awareness**: Understand the computational complexity ($O(1)$ lookup for dicts/sets vs. $O(N)$ lookup for lists).