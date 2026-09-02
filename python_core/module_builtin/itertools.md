# 🧰 The `itertools` Module

The **`itertools`** module provides fast, memory-efficient iterator building blocks. Unlike lists, they usually return **iterators** rather than fully computed lists, so values are produced lazily, one at a time.

---

## 🔢 `count()` — Infinite Numbers

Generates an infinite, evenly-spaced sequence of numbers starting from a given value.

```python
from itertools import count

for i in count(10):
    print(i)
    if i == 15:
        break
```

---

## 🔁 `cycle()` — Repeat Forever

Repeats the items of an iterable indefinitely, cycling back to the start once it's exhausted.

```python
from itertools import cycle

colors = cycle(["red", "green"])

for _ in range(5):
    print(next(colors))
```

---

## 🔂 `repeat()` — Repeat a Value

Repeats a single value a fixed number of times (or forever, if no count is given).

```python
from itertools import repeat

for x in repeat("ML", 3):
    print(x)
```

---

## 🔗 `chain()` — Combine Iterables

Combines multiple iterables into one continuous stream, without creating a new list.

```python
from itertools import chain

for x in chain([1, 2], [3, 4], [5]):
    print(x)
```

---

## ✂️ `islice()` — Slice an Iterator

Slices an iterator the same way you would slice a list, but without consuming it all at once.

```python
from itertools import count, islice

nums = count(1)
print(list(islice(nums, 5)))
```

---

## 🎯 Summary Comparison (In a Nutshell)

| Feature                        | Creates All Data Immediately? | Memory Usage |         Reusable?        |
| ------------------------------- | :----------------------------: | :-----------: | :-----------------------: |
| List                            |               Yes               |     High      |            Yes            |
| List comprehension               |               Yes               |     High      |            Yes            |
| Generator expression             |               No                |      Low      |     No (single pass)      |
| Generator function (`yield`)     |               No                |      Low      |     No (single pass)      |
| `itertools` iterators            |               No                |   Very Low    | Usually No (single pass)  |
