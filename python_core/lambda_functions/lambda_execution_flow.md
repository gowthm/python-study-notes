# ⚡ Lambda Execution Flow

A step-by-step trace of what happens when a lambda is defined and then called.

```text
add = lambda a, b: a + b
      │
      ▼
Call add(10, 20)
      │
      ▼
a = 10
b = 20
      │
      ▼
Evaluate expression
      │
      ▼
10 + 20
      │
      ▼
Return 30
```
