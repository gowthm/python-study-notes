# 🌳 NumPy Core Flowgraph

A hierarchical outline of NumPy's public API surface — from the `ndarray` core through modules like `linalg`, `random`, and `fft`.

```
NumPy (numpy)
│
├── Core
│   │
│   ├── ndarray
│   │   │
│   │   ├── Construction
│   │   │   ├── array()
│   │   │   ├── asarray()
│   │   │   ├── copy()
│   │   │   ├── empty()
│   │   │   ├── zeros()
│   │   │   ├── ones()
│   │   │   ├── full()
│   │   │   ├── arange()
│   │   │   ├── linspace()
│   │   │   ├── logspace()
│   │   │   ├── geomspace()
│   │   │   ├── identity()
│   │   │   ├── eye()
│   │   │   ├── diag()
│   │   │   ├── fromiter()
│   │   │   ├── frombuffer()
│   │   │   ├── fromfile()
│   │   │   └── fromfunction()
│   │   │
│   │   ├── Attributes
│   │   │   ├── shape
│   │   │   ├── ndim
│   │   │   ├── dtype
│   │   │   ├── size
│   │   │   ├── itemsize
│   │   │   ├── nbytes
│   │   │   ├── strides
│   │   │   ├── flags
│   │   │   ├── T
│   │   │   ├── real
│   │   │   ├── imag
│   │   │   ├── flat
│   │   │   ├── base
│   │   │   └── data
│   │   │
│   │   ├── Shape
│   │   │   ├── reshape()
│   │   │   ├── resize()
│   │   │   ├── flatten()
│   │   │   ├── ravel()
│   │   │   ├── squeeze()
│   │   │   ├── transpose()
│   │   │   ├── swapaxes()
│   │   │   ├── moveaxis()
│   │   │   └── repeat()
│   │   │
│   │   ├── Indexing
│   │   │   ├── Integer
│   │   │   ├── Slice
│   │   │   ├── Boolean
│   │   │   ├── Fancy
│   │   │   ├── Ellipsis (...)
│   │   │   └── newaxis
│   │   │
│   │   ├── Iteration
│   │   │   ├── iter()
│   │   │   ├── flat
│   │   │   └── nditer
│   │   │
│   │   ├── Math
│   │   │   ├── sum()
│   │   │   ├── mean()
│   │   │   ├── std()
│   │   │   ├── var()
│   │   │   ├── prod()
│   │   │   ├── min()
│   │   │   ├── max()
│   │   │   ├── argmin()
│   │   │   ├── argmax()
│   │   │   ├── cumsum()
│   │   │   ├── cumprod()
│   │   │   ├── any()
│   │   │   ├── all()
│   │   │   └── clip()
│   │   │
│   │   ├── Sorting
│   │   │   ├── sort()
│   │   │   ├── argsort()
│   │   │   ├── partition()
│   │   │   └── argpartition()
│   │   │
│   │   ├── Searching
│   │   │   ├── where()
│   │   │   ├── nonzero()
│   │   │   ├── argwhere()
│   │   │   ├── searchsorted()
│   │   │   └── compress()
│   │   │
│   │   ├── Conversion
│   │   │   ├── astype()
│   │   │   ├── tolist()
│   │   │   ├── item()
│   │   │   ├── tobytes()
│   │   │   └── dump()
│   │   │
│   │   ├── Operators
│   │   │   ├── +
│   │   │   ├── -
│   │   │   ├── *
│   │   │   ├── /
│   │   │   ├── //
│   │   │   ├── %
│   │   │   ├── **
│   │   │   ├── @
│   │   │   ├── &
│   │   │   ├── |
│   │   │   ├── ^
│   │   │   └── Comparisons
│   │   │
│   │   └── Memory
│   │       ├── Views
│   │       ├── Copies
│   │       ├── Buffer
│   │       └── Contiguous arrays
│   │
│   ├── dtype
│   │   ├── int
│   │   ├── uint
│   │   ├── float
│   │   ├── complex
│   │   ├── bool
│   │   ├── str
│   │   ├── bytes
│   │   ├── datetime64
│   │   ├── timedelta64
│   │   ├── object
│   │   └── structured dtype
│   │
│   ├── Broadcasting
│   ├── Copies vs Views
│   ├── Memory Layout
│   └── nditer
│
├── Universal Functions (ufunc)
│   ├── Arithmetic
│   ├── Trigonometric
│   ├── Hyperbolic
│   ├── Exponential
│   ├── Logarithmic
│   ├── Rounding
│   ├── Comparison
│   ├── Logical
│   ├── Bitwise
│   ├── Floating-point
│   └── Special math
│
├── Array Manipulation
│   ├── reshape
│   ├── transpose
│   ├── concatenate
│   ├── stack
│   ├── split
│   ├── tile
│   ├── repeat
│   ├── flip
│   ├── rotate
│   ├── insert
│   ├── delete
│   └── append
│
├── Statistics
│   ├── sum
│   ├── mean
│   ├── median
│   ├── std
│   ├── var
│   ├── percentile
│   ├── quantile
│   ├── average
│   ├── covariance
│   └── correlation
│
├── Searching / Sorting / Set
│   ├── unique
│   ├── isin
│   ├── intersect1d
│   ├── union1d
│   ├── setdiff1d
│   ├── sort
│   ├── argsort
│   └── where
│
├── Linear Algebra (linalg)
│   ├── dot
│   ├── matmul
│   ├── inner
│   ├── outer
│   ├── cross
│   ├── inverse
│   ├── determinant
│   ├── eigenvalues
│   ├── solve
│   ├── SVD
│   ├── QR
│   └── norms
│
├── Random
│   ├── Generator
│   ├── Integers
│   ├── Uniform
│   ├── Normal
│   ├── Choice
│   ├── Shuffle
│   ├── Permutation
│   └── Distributions
│
├── FFT
│   ├── fft
│   ├── ifft
│   ├── fft2
│   ├── fftn
│   └── helpers
│
├── Polynomial
│   ├── Polynomial
│   ├── Chebyshev
│   ├── Legendre
│   ├── Hermite
│   └── Laguerre
│
├── Strings
│   ├── add
│   ├── split
│   ├── replace
│   ├── strip
│   ├── upper
│   ├── lower
│   └── formatting
│
├── Datetime
│   ├── datetime64
│   ├── timedelta64
│   ├── business day
│   └── arithmetic
│
├── Masked Arrays
│
├── File I/O
│   ├── save
│   ├── load
│   ├── savetxt
│   ├── loadtxt
│   ├── savez
│   └── genfromtxt
│
├── Constants
│   ├── pi
│   ├── e
│   ├── inf
│   ├── nan
│   └── newaxis
│
├── Typing
│
├── Testing
│
└── C API
```