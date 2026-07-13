# ⚡ Python Generators (yield)

A **Generator** is a special type of function in Python that returns an iterator object (called a generator iterator). Unlike regular functions that compute all values and return them in a single batch, generators produce values **lazily** (one at a time, on demand) using the `yield` statement.

---

## 🍕 The Pizza Analogy

> [!NOTE]
> **Regular Function vs. Generator Function**
> * **Regular Function**: Like ordering 3 pizzas and waiting until all 3 arrive together. You get everything at once, but you have to wait for all of them to be prepared and delivered in one go.
> * **Generator**: Like a pizza place that delivers one pizza at a time. You eat the first, then ask for the second, and then the third. Although it might feel spaced out, the kitchen only makes one pizza at a time, consuming minimal counter space.

---

## 📂 Visualizing Generators

This directory includes a side-by-side interactive visual comparison between a regular function and a generator function:

* **Comparison File**: [regular_function_vs_generator_comparison.html](file:///d:/python/python-study-notes/generator/regular_function_vs_generator_comparison.html)
* **Description**: An interactive webpage showing how a regular function runs to completion immediately (with variables lost afterwards), while a generator pauses at each `yield` step, keeping its local state alive between calls.

---

## ⚡ Benefits of Generators

1. **Memory Efficiency**: Since elements are yielded one-by-one, generators do not need to store the entire collection in memory. This is critical when working with large datasets or infinite streams.
2. **State Preservation**: When a generator yields a value, the execution is suspended, and the values of local variables are saved. When `next()` is called again, execution resumes immediately after the `yield` statement.