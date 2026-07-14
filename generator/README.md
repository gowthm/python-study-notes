# ⚡ Python Generators (yield)

A **Generator** is a special type of function in Python that returns an iterator object (called a generator iterator). Unlike regular functions that compute all values and return them in a single batch, generators produce values **lazily** (one at a time, on demand) using the `yield` statement.

---

## 🍕 The Pizza Analogy

> [!NOTE]
> **Regular Function vs. Generator Function**
> * **Regular Function**: Like ordering 3 pizzas and waiting until all 3 arrive together. You get everything at once, but you have to wait for all of them to be prepared and delivered in one go.
> * **Generator**: Like a pizza place that delivers one pizza at a time. You eat the first, then ask for the second, and then the third. Although it might feel spaced out, the kitchen only makes one pizza at a time, consuming minimal counter space.

---

## 📂 Example Scripts & Visualizers

This directory includes comparisons between regular functions, iterator classes, and generator functions:

### 1. Side-by-Side Step Visualizer
* **Visualizer File**: [regular_function_vs_generator_comparison.html](file:///d:/python/python-study-notes/generator/regular_function_vs_generator_comparison.html)
* **Description**: An interactive webpage showing how a regular function runs to completion immediately (with variables lost afterwards), while a generator pauses at each `yield` step, keeping its local state alive between calls.

### 2. Three-Way Code Comparison
* **Script File**: [regular_generator_iterator.py](file:///d:/python/python-study-notes/generator/regular_generator_iterator.py)
* **Description**: A Python script illustrating how to solve the same task (generating even numbers) using a regular list builder, a manual iterator class, and a generator function.

### 3. Three-Way Interactive Dashboard
* **Dashboard File**: [regular_vs_iterator_vs_generator.html](file:///d:/python/python-study-notes/generator/regular_vs_iterator_vs_generator.html)
* **Description**: An interactive dashboard showing side-by-side execution mechanics, memory complexity, and situations when to choose each pattern.

### 4. Basic Generator Script
* **Script File**: [generator_basics.py](file:///d:/python/python-study-notes/generator/generator_basics.py)
* **Description**: A basic demonstration showing how a generator is defined with `yield` and how to iterate over it using a `for` loop.

---

## ⚡ Benefits of Generators

1. **Memory Efficiency**: Since elements are yielded one-by-one, generators do not need to store the entire collection in memory. This is critical when working with large datasets or infinite streams.
2. **State Preservation**: When a generator yields a value, the execution is suspended, and the values of local variables are saved. When `next()` is called again, execution resumes immediately after the `yield` statement.

---

## 🎯 Summary Comparison (In a nutshell)

> [!IMPORTANT]
> **The Three Patterns in One Sentence Each:**
> * 🏃‍♂️ **Regular function**: Runs from top to bottom in one shot and hands back the whole result at the end.
> * 🛠️ **Iterator class**: A hand-built object with `__iter__` and `__next__` methods; you write all the state management yourself.
> * ⚡ **Generator function**: Looks like a regular function but has `yield` in it; Python automatically turns it into an iterator that pauses and resumes.