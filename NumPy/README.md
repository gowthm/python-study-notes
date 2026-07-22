# 🔢 NumPy

## 📖 Overview

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides:

- A multidimensional array object
- Various derived objects, such as masked arrays and matrices
- An assortment of routines for fast operations on arrays, including:
  - Mathematical and logical operations
  - Shape manipulation
  - Sorting and selecting
  - I/O
  - Discrete Fourier transforms
  - Basic linear algebra
  - Basic statistical operations
  - Random simulation
  - ...and much more

At the core of the NumPy package is the `ndarray` object. This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance.

NumPy arrays facilitate advanced mathematical and other types of operations on large amounts of data. Typically, such operations are executed more efficiently and with less code than is possible using Python's built-in sequences.

## ⚡ Why Is NumPy Fast?

Vectorization describes the absence of any explicit looping, indexing, etc., in the code — these things are taking place, of course, just "behind the scenes" in optimized, pre-compiled C code. Vectorized code has many advantages, among which are:

- Vectorized code is more concise and easier to read.
- Fewer lines of code generally means fewer bugs.
- The code more closely resembles standard mathematical notation, making it easier to correctly code mathematical constructs.
- Vectorization results in more "Pythonic" code. Without vectorization, our code would be littered with inefficient, difficult-to-read `for` loops.

## 👥 Who Else Uses NumPy?

NumPy fully supports an object-oriented approach, once again starting with `ndarray`. For example, [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray) is a class, possessing numerous methods and attributes. Many of its methods are mirrored by functions in the outermost NumPy namespace, allowing the programmer to code in whichever paradigm they prefer.

## 🚀 Quick Start

### 🏗️ Array Creation

```python
import numpy as np

a = np.array([2, 3, 4])
b = np.array([1.2, 3.5, 5.1])

b.dtype
# dtype('float64')
```

Other useful array-creation functions:

- Basics: `array`, `zeros`, `zeros_like`, `ones`, `ones_like`, `empty`, `empty_like`
- Ranges: `arange`, `linspace`
- Random: `random.Generator.random`, `random.Generator.normal`
- From source: `fromfunction`, `fromfile`

### 🖨️ Printing Arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:

- The last axis is printed from left to right.
- The second-to-last axis is printed from top to bottom.
- The rest are also printed from top to bottom, with each slice separated from the next by an empty line.

One-dimensional arrays are printed as rows, two-dimensional arrays as matrices, and three-dimensional arrays as lists of matrices.

```python
a = np.arange(6)                    # 1d array
print(a)
# [0 1 2 3 4 5]

b = np.arange(12).reshape(4, 3)     # 2d array
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]
```

### ➕ Basic Operations

Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.

#### Universal Functions

NumPy provides familiar mathematical functions such as `sin`, `cos`, and `exp`. In NumPy, these are called "universal functions" (`ufunc`). Within NumPy, these functions operate elementwise on an array, producing an array as output.

```python
B = np.arange(3)
B
# array([0, 1, 2])

np.exp(B)
# array([1.        , 2.71828183, 7.3890561 ])

np.sqrt(B)
# array([0.        , 1.        , 1.41421356])

C = np.array([2., -1., 4.])
np.add(B, C)
# array([2., 0., 6.])
```

**See also:** `all`, `any`, `apply_along_axis`, `argmax`, `argmin`, `argsort`, `average`, `bincount`, `ceil`, `clip`, `conj`, `corrcoef`, `cov`, `cross`, `cumprod`, `cumsum`, `diff`, `dot`, `floor`, `inner`, `invert`, `lexsort`, `max`, `maximum`, `mean`, `median`, `min`, `minimum`, `nonzero`, `outer`, `prod`, `re`, `round`, `sort`, `std`, `sum`, `trace`, `transpose`, `var`, `vdot`, `vectorize`, `where`

### 🔍 Indexing, Slicing and Iterating

One-dimensional arrays can be indexed, sliced, and iterated over, much like lists and other Python sequences.

Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas.

### 🔷 Shape Manipulation

*Changing the shape of an array.*

## 📚 Functions and Methods Overview

Here is a list of some useful NumPy functions and method names, organized by category. See *Routines and objects by topic* for the full reference list.

- **Array Creation:** `arange`, `array`, `copy`, `empty`, `empty_like`, `eye`, `fromfile`, `fromfunction`, `identity`, `linspace`, `logspace`, `mgrid`, `ogrid`, `ones`, `ones_like`, `r_`, `zeros`, `zeros_like`
- **Conversions:** `ndarray.astype`, `atleast_1d`, `atleast_2d`, `atleast_3d`, `mat`
- **Manipulations:** `array_split`, `column_stack`, `concatenate`, `diagonal`, `dsplit`, `dstack`, `hsplit`, `hstack`, `ndarray.item`, `newaxis`, `ravel`, `repeat`, `reshape`, `resize`, `squeeze`, `swapaxes`, `take`, `transpose`, `vsplit`, `vstack`
- **Questions:** `all`, `any`, `nonzero`, `where`
- **Ordering:** `argmax`, `argmin`, `argsort`, `max`, `min`, `ptp`, `searchsorted`, `sort`
- **Operations:** `choose`, `compress`, `cumprod`, `cumsum`, `inner`, `ndarray.fill`, `imag`, `prod`, `put`, `putmask`, `real`, `sum`
- **Basic Statistics:** `cov`, `mean`, `std`, `var`
- **Basic Linear Algebra:** `cross`, `dot`, `outer`, `linalg.svd`, `vdot`

## 📡 Broadcasting Rules

Broadcasting allows universal functions to deal in a meaningful way with inputs that do not have exactly the same shape.

1. If all input arrays do not have the same number of dimensions, a `1` will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.
2. Arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the "broadcast" array.

| A (shape) | B (shape) | Result (shape) |
| --- | --- | --- |
| 2d array: `5 x 4` | 1d array: `1` | 2d array: `5 x 4` |
| 2d array: `5 x 4` | 1d array: `4` | 2d array: `5 x 4` |
| 3d array: `15 x 3 x 5` | 3d array: `15 x 1 x 5` | 3d array: `15 x 3 x 5` |
| 3d array: `15 x 3 x 5` | 2d array: `3 x 5` | 3d array: `15 x 3 x 5` |
| 3d array: `15 x 3 x 5` | 2d array: `3 x 1` | 3d array: `15 x 3 x 5` |

```python
import numpy as np

a = np.array([[ 0.0,  0.0,  0.0],
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
a + b

b = np.array([1.0, 2.0, 3.0, 4.0])
a + b
# Traceback (most recent call last):
# ValueError: operands could not be broadcast together with shapes (4,3) (4,)
```

![Broadcasting example 1](https://numpy.org/doc/stable/_images/broadcasting_1.png)
![Broadcasting example 2](https://numpy.org/doc/stable/_images/broadcasting_2.png)
![Broadcasting example 3](https://numpy.org/doc/stable/_images/broadcasting_3.png)
![Broadcasting example 4](https://numpy.org/doc/stable/_images/broadcasting_4.png)

### Example 1

```python
from numpy import array, argmin, sqrt, sum

observation = array([111.0, 188.0])
codes = array([[102.0, 203.0],
               [132.0, 193.0],
               [45.0, 155.0],
               [57.0, 173.0]])

diff = codes - observation
dist = sqrt(sum(diff**2, axis=-1))
argmin(dist)

print(diff)
print(dist)
print(argmin)
```

### General Broadcasting Rules

When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e., rightmost) dimension and works its way left. Two dimensions are compatible when:

- They are equal, or
- One of them is `1`.
