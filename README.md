# 🐍 Python Study Notes

Welcome to the Python Study Notes repository! This repository contains a collection of well-documented study guides, conceptual explanations, and clean Python scripts demonstrating core language features.

---

## 🗺️ Topics Index

Explore the different study folders below:

| Topic | Description | Key Subconcepts | Documentation Link |
| :--- | :--- | :--- | :---: |
| **Functions** | Modularity and metadata preservation | TV Remote Analogy, `functools.wraps` | [View Guide](file:///d:/python/python-study-notes/functools.wrap/README.md) |
| **Decorators** | Extending functions without source edits | Rebinding (`hello = decorator(hello)`), wrappers, args flow | [View Guide](file:///d:/python/python-study-notes/decorators/README.md) |
| **Context Managers** | Automated setup and cleanup operations | `with` block execution protocol, custom timers | [View Guide](file:///d:/python/python-study-notes/context_managers/README.md) |
| **Dictionaries** | Hash-table based key-value collection | CRUD, `.get()` default value lookup, loops | [View Guide](file:///d:/python/python-study-notes/dict/README.md) |
| **Sets** | Unordered collection of unique items | `.add()`, `.discard()`, Union, Intersection, Difference | [View Guide](file:///d:/python/python-study-notes/set/README.md) |
| **Iterators** | Stateful looping engine behind `for` loops | Iterable vs. Iterator, Iterator Protocol, `StopIteration` | [View Guide](file:///d:/python/python-study-notes/iterators/README.md) |
| **Generators** | Memory-efficient lazy evaluation | `yield` vs. `return`, local state retention | [View Guide](file:///d:/python/python-study-notes/generator/README.md) |

---

## 🛠️ General Best Practices for Python Study

* 🧪 **Hands-on Experimentation**: Each topic guide lists associated Python scripts. Run them locally to see how standard inputs and edge cases are handled.
* 📦 **Avoid Global State**: Encapsulate logic inside clean functions and keep variables localized.
* 📈 **Performance Awareness**: Understand the computational complexity ($O(1)$ lookup for dicts/sets vs. $O(N)$ lookup for lists).