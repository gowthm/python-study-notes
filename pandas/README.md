# 🐼 Pandas — A SQL Programmer's Guide

**Learning Pandas by mapping every concept back to the SQL you already know.**

If you can think in `SELECT`, `WHERE`, `ORDER BY`, and `JOIN`, you already understand
80% of Pandas. This guide connects the two worlds concept by concept.

---

## 🧱 1. What Is a DataFrame?

A **DataFrame** is a *typed*, *indexed* table stored *in memory*.

Those three words carry the whole idea, so let's take them one at a time.

### 📋 It Is a Table

Just like a SQL table, it is made of **rows and columns**.

### 🏷️ It Is Typed

Every column has one data type shared by all its values.

```
id       integer
name     string
age      integer
salary   integer
```

### 🔢 It Is Indexed

Every row carries a label called the **index**.

```
index     name
0         Gowtham
1         Arun
2         Ravi
```

### 🧠 It Is In-Memory

The data normally lives in your computer's RAM, not on disk.

SQL works like this:

```
PostgreSQL / MySQL
        ↓
      Disk
        ↓
 Database server
```

Pandas works like this:

```
      File
        ↓
  Read into RAM
        ↓
   DataFrame
        ↓
Python operations
```

This is why Pandas feels so fast and convenient — as long as the data fits
comfortably in memory.

> [!IMPORTANT]
> Because a DataFrame lives in RAM, **size is your limit, not disk space**.
> A rough rule of thumb: you want roughly 5–10× the file size available as free
> RAM, since intermediate operations create temporary copies.

---

## 🗺️ 2. The Big Picture

```
                 DATA SOURCE
                      │
          ┌───────────┼───────────┐
          │           │           │
         CSV        JSON       Parquet
          │           │           │
          └───────────┼───────────┘
                      ▼
                  DataFrame
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
      Columns       Rows         Index
         │            │            │
       dtype       values       labels
                      │
                      ▼
                 Operations
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   Filter           Sort           Modify
    WHERE         ORDER BY         UPDATE
```

---

## 🔁 3. SQL ↔ Pandas Vocabulary

| SQL           | Pandas                              |
| ------------- | ----------------------------------- |
| Table         | `DataFrame`                         |
| Column        | `Series`                            |
| Row           | Row                                 |
| `SELECT`      | Column selection                    |
| `WHERE`       | Boolean filtering                   |
| `ORDER BY`    | `sort_values()`                     |
| `LIMIT`       | `head()`                            |
| `GROUP BY`    | `groupby()`                         |
| `DISTINCT`    | `unique()` / `drop_duplicates()`    |
| `JOIN`        | `merge()`                           |
| `UNION ALL`   | `concat()`                          |
| `IS NULL`     | `isna()`                            |
| Primary key   | Index (sometimes, but not always)   |

A quick side-by-side. SQL:

```sql
SELECT *
FROM employees
WHERE salary > 50000
ORDER BY age;
```

Pandas:

```python
df[df["salary"] > 50000].sort_values("age")
```

---

## 🏗️ 4. Creating a DataFrame

There is no `CREATE TABLE` in Pandas — you build a DataFrame from data you already have.

```python
import pandas as pd

# From a dictionary of columns (most common)
df = pd.DataFrame({
    "name":   ["Gowtham", "Arun", "Ravi"],
    "age":    [29, 30, 28],
    "salary": [50000, 60000, 45000],
})

# From a list of row dictionaries (looks like JSON API output)
df = pd.DataFrame([
    {"name": "Gowtham", "age": 29},
    {"name": "Arun",    "age": 30},
])
```

Reading from a file is far more common in practice:

```python
df = pd.read_csv("employees.csv")
df = pd.read_json("airports.json")
df = pd.read_parquet("employees.parquet")
df = pd.read_sql("SELECT * FROM employees", connection)
```

### 🪆 Flattening Nested JSON

JSON APIs return nested objects. `read_json` alone will leave you with a column
full of dictionaries, so flatten it with `json_normalize()`:

```python
from pathlib import Path
import pandas as pd

json_path = Path(__file__).parent / "airports.json"

df = pd.read_json(json_path)          # column "airports" holds dicts
df = pd.json_normalize(df["airports"])  # each key becomes its own column

print(df.loc[df["city"] == "London"])
```

> [!NOTE]
> `json_normalize()` also flattens deeper nesting into dotted column names, so
> `{"location": {"lat": 51.5}}` becomes a column called `location.lat`.

---

## 🔍 5. Inspecting a DataFrame

Before you query anything, look at what you actually loaded. These five calls
should be muscle memory:

```python
df.head()       # first 5 rows          → SQL: SELECT * ... LIMIT 5
df.tail()       # last 5 rows
df.shape        # (rows, columns)       → SQL: SELECT COUNT(*)
df.info()       # dtypes, non-null counts, memory usage
df.describe()   # count/mean/std/min/max for numeric columns
```

| Call             | Answers the question                          |
| ---------------- | --------------------------------------------- |
| `df.head()`      | What does the data look like?                 |
| `df.shape`       | How big is it?                                |
| `df.columns`     | What columns exist?                           |
| `df.dtypes`      | What type is each column?                     |
| `df.info()`      | Where are the nulls, and how much RAM is used? |
| `df.describe()`  | What is the distribution of the numbers?      |

---

## 🧬 6. Data Types (`dtype`)

Typical dtypes you will meet:

```
name       object
age        int64
salary     float64
active     bool
joined     datetime64[ns]
```

`object` is the one to watch. It usually means **Python strings**, and it is
stored very differently from a numeric column:

```
┌──────────────────────────────┐   ┌──────────────────────────────┐
│ df["age"]   dtype = int64    │   │ df["name"]  dtype = object   │
│                              │   │                              │
│ ┌────┬────┬────┐             │   │ ┌───┬───┬───┐                │
│ │ 29 │ 30 │ 28 │             │   │ │ ● │ ● │ ● │                │
│ └────┴────┴────┘             │   │ └─┬─┴─┬─┴─┬─┘                │
│                              │   │   ↓   ↓   ↓                  │
│ one contiguous C block       │   │ 3 pointers to separate       │
│ of raw 8-byte numbers        │   │ Python str objects           │
└──────────────────────────────┘   └──────────────────────────────┘
```

That difference explains a lot of Pandas behaviour:

- **Numeric columns are fast** — operations run in compiled C over one memory block.
- **`object` columns are slow** — every operation has to chase pointers into the
  Python heap, one object at a time.
- **`object` columns use much more memory** — each Python string carries ~50 bytes
  of overhead on top of its characters.

> [!TIP]
> If a column has few distinct values (country, department, status), convert it
> with `df["dept"] = df["dept"].astype("category")`. Pandas then stores small
> integer codes instead of full strings — often a 10× memory saving.

---

## 📏 7. `Series` vs `DataFrame`

This trips up almost everyone at the start.

| | Shape | SQL analogy |
| ------------- | -------- | ---------------- |
| `Series`      | 1D       | A single column  |
| `DataFrame`   | 2D       | A whole table    |

```python
df["name"]        # → Series   (one column)
df[["name"]]      # → DataFrame (a table with one column)
```

The rule: **a single string gives you a Series; a list gives you a DataFrame.**

---

## 🔑 8. The Index Is *Not* Automatically a Primary Key

This is a major conceptual difference from SQL.

In SQL, `PRIMARY KEY` usually means:

- Unique
- The important identifier for the row
- **Enforced by the database**

In Pandas, `df.index` is simply the row label. It does **not** automatically mean:

- unique
- primary key
- business identifier

You can even have duplicate index values, and Pandas will not complain.

> [!WARNING]
> The Pandas index is primarily a **row-labelling and alignment mechanism**.
> It is not a SQL primary key. If you need uniqueness, check it yourself with
> `df.index.is_unique` or `df["id"].duplicated().any()`.

---

## 🎯 9. `iloc` vs `loc`

One of the most important things to get straight.

### `iloc` = Integer Position

The `i` means **integer position** — where the row physically sits.

```python
df.iloc[0]     # the first row, whatever its label is
```

```
Position
0 → Gowtham
1 → Arun
2 → Ravi
```

### `loc` = Label

`loc` uses the **index label**.

Suppose the index is not `0, 1, 2`:

```
index    name
101      Gowtham
205      Arun
500      Ravi
```

Then:

```python
df.loc[101]    # → Gowtham
df.iloc[0]     # → also Gowtham, but for a different reason
```

**The mental split:**

```
iloc → WHERE is the row physically positioned?
loc  → WHAT is the row's label?
```

> [!IMPORTANT]
> Slicing behaves differently between the two:
> `df.iloc[0:3]` excludes position 3 (normal Python slicing),
> but `df.loc[101:500]` **includes** the label `500`.
> Label slices are inclusive on both ends.

---

## 📤 10. Selecting Columns (`SELECT`)

SQL:

```sql
SELECT name, salary
FROM employees;
```

Pandas:

```python
df[["name", "salary"]]     # → DataFrame
```

For a single column:

```python
df["name"]                 # → Series
```

You can also select rows and columns together with `loc`:

```python
df.loc[:, ["name", "salary"]]        # all rows, two columns
df.loc[df["age"] > 28, "salary"]     # matching rows, one column
```

---

## 🧪 11. Boolean Filtering (`WHERE`)

Suppose:

```
name      age    salary
Gowtham   29     50000
Arun      30     60000
Ravi      28     45000
```

SQL:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

Pandas:

```python
df[df["salary"] > 50000]
```

### What Actually Happens

Filtering is a **two-step** process, and seeing both steps makes it click.

**Step 1** — the comparison produces a *boolean Series* (a "mask"):

```python
df["salary"] > 50000
```

```
0    False
1     True
2    False
Name: salary, dtype: bool
```

**Step 2** — that mask is handed back to the DataFrame:

```python
df[[False, True, False]]
```

Pandas keeps only the rows where the mask is `True`.

```
┌─────┬─────────┬─────┬────────┬───────┐
│ idx │ name    │ age │ salary │ mask  │
├─────┼─────────┼─────┼────────┼───────┤
│ 0   │ Gowtham │ 29  │ 50000  │ False │
│ 1   │ Arun    │ 30  │ 60000  │ True  │
│ 2   │ Ravi    │ 28  │ 45000  │ False │
└─────┴─────────┴─────┴────────┴───────┘
                                   ▲
                       df["salary"] > 50000
```

---

## 🔗 12. Multiple Conditions

SQL:

```sql
SELECT *
FROM employees
WHERE age > 28
  AND salary > 50000;
```

Pandas:

```python
df[
    (df["age"] > 28) &
    (df["salary"] > 50000)
]
```

Notice it is `&`, **not** `and`.

### Why Not `and`?

Because `and` works on a **single** Python boolean value.

But `df["age"] > 28` is not a single boolean — it is an entire Series:

```
0     True
1     True
2    False
```

Python has no way to reduce that to one `True`/`False`, so `and` raises
`ValueError: The truth value of a Series is ambiguous`.

Pandas therefore uses **element-wise** operators:

| Operator | Meaning | SQL   |
| -------- | ------- | ----- |
| `&`      | AND     | `AND` |
| `\|`     | OR      | `OR`  |
| `~`      | NOT     | `NOT` |

> [!WARNING]
> **The parentheses are mandatory.** `&` binds more tightly than `>` in Python,
> so `df["age"] > 28 & df["salary"] > 50000` is parsed as
> `df["age"] > (28 & df["salary"]) > 50000` and fails. Always wrap each
> condition: `(a) & (b)`.

---

## 🎣 13. More `WHERE` Patterns

| SQL                              | Pandas                                            |
| -------------------------------- | ------------------------------------------------- |
| `WHERE dept IN ('IT', 'HR')`     | `df[df["dept"].isin(["IT", "HR"])]`               |
| `WHERE age BETWEEN 25 AND 30`    | `df[df["age"].between(25, 30)]`                   |
| `WHERE name LIKE 'G%'`           | `df[df["name"].str.startswith("G")]`              |
| `WHERE name LIKE '%wth%'`        | `df[df["name"].str.contains("wth")]`              |
| `WHERE email IS NULL`            | `df[df["email"].isna()]`                          |
| `WHERE email IS NOT NULL`        | `df[df["email"].notna()]`                         |
| `WHERE dept <> 'IT'`             | `df[df["dept"] != "IT"]`                          |

> [!NOTE]
> The `.str` accessor is how you reach string methods on a whole column at once.
> `df["name"].str.lower()`, `.str.strip()`, `.str.replace()`, `.str.split()` all
> work the same way.

---

## 🔀 14. Sorting (`ORDER BY`)

SQL:

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

Pandas:

```python
df.sort_values("salary", ascending=False)
```

Ascending is the default:

```python
df.sort_values("salary")                    # ASC
df.sort_values("salary", ascending=False)   # DESC
```

### Multiple Columns

SQL:

```sql
ORDER BY department ASC, salary DESC
```

Pandas — pass a list of columns and a matching list of directions:

```python
df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)
```

> [!TIP]
> `sort_values()` keeps the original index labels attached to each row, so after
> sorting your index is shuffled (`2, 0, 1`). Add `.reset_index(drop=True)` if
> you want a clean `0, 1, 2` again.

---

## ✂️ 15. Limiting Rows (`LIMIT`)

```python
df.head(5)      # first 5 rows        → LIMIT 5
df.tail(5)      # last 5 rows
df.sample(5)    # 5 random rows       → ORDER BY RANDOM() LIMIT 5
df.nlargest(5, "salary")   # top 5    → ORDER BY salary DESC LIMIT 5
df.nsmallest(5, "salary")  # bottom 5
```

---

## ✏️ 16. Modifying Data (`UPDATE`)

### ❌ The Trap: Chained Assignment

SQL:

```sql
UPDATE employees
SET salary = 0
WHERE age > 28;
```

The obvious translation is **wrong**:

```python
df[df["age"] > 28]["salary"] = 0     # ⚠️ silently does nothing
```

Here is why. This is *two* separate operations:

```
df[df["age"] > 28]      →  step 1: build a NEW object (possibly a copy)
        ["salary"] = 0  →  step 2: write into that temporary object
```

The temporary object is then thrown away. Your original `df` is untouched, and
Pandas may warn you with `SettingWithCopyWarning` — or, worse, say nothing at all.

### ✅ The Correct Way: One `.loc` Call

```python
df.loc[
    df["age"] > 28,
    "salary"
] = 0
```

This is a **single** indexing operation, so Pandas knows exactly what you mean:

```
DataFrame
    ↓
Rows where age > 28
    ↓
salary column
    ↓
set to 0
```

> [!IMPORTANT]
> **The rule:** if a line has two `[]` in a row *and* an `=`, it is chained
> assignment. Rewrite it as a single `df.loc[rows, columns] = value`.

---

## ➕ 17. Adding, Renaming, and Dropping Columns

```python
# Add a computed column (ALTER TABLE ADD + UPDATE in one step)
df["bonus"] = df["salary"] * 0.10

# Conditional column
import numpy as np
df["band"] = np.where(df["salary"] > 50000, "senior", "junior")

# Rename
df = df.rename(columns={"name": "employee_name"})

# Drop
df = df.drop(columns=["bonus"])          # a column
df = df.drop(index=[0, 2])               # rows by index label
```

> [!NOTE]
> Most Pandas methods **return a new DataFrame** rather than editing in place,
> which is why you see `df = df.rename(...)`. Direct column assignment
> (`df["x"] = ...`) is one of the few genuine in-place operations.

---

## 🕳️ 18. Missing Data (`NULL` vs `NaN`)

SQL has `NULL`. Pandas has `NaN` (and `None`, and `NaT` for dates). They behave
similarly but not identically.

```python
df["email"].isna()          # → IS NULL
df["email"].notna()         # → IS NOT NULL
df["email"].isna().sum()    # how many nulls in this column
df.isna().sum()             # null count for every column
```

Handling them:

```python
df = df.dropna()                          # drop rows with ANY null
df = df.dropna(subset=["email"])          # drop only if email is null
df = df.fillna(0)                         # replace all nulls with 0
df["email"] = df["email"].fillna("n/a")   # per column
```

> [!WARNING]
> Just like SQL's `NULL`, **`NaN` is not equal to anything — including itself**.
> `df["email"] == None` will never match. Always use `.isna()`.
> One more gotcha: a column of integers that gains a single `NaN` is promoted
> from `int64` to `float64`, because `NaN` is a float.

---

## 📊 19. Grouping and Aggregation (`GROUP BY`)

SQL:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

Pandas:

```python
df.groupby("department")["salary"].mean()
```

### Split → Apply → Combine

That single line is really three steps, and this is *the* mental model for `groupby`:

```
     1. SPLIT by key                  2. APPLY mean()                 3. COMBINE result
┌────────────────────────┐       ┌────────────────────────┐       ┌────────────────────────┐
│ dept   salary          │       │ group 'IT'             │       │ dept   salary          │
│ ────   ──────          │       │   50000                │       │ ────   ──────          │
│ IT     50000           │       │   70000                │       │ IT     60000           │
│ HR     40000           │  ──▶  │                        │  ──▶  │ HR     50000           │
│ IT     70000           │       │ group 'HR'             │       │                        │
│ HR     60000           │       │   40000  60000         │       │                        │
└────────────────────────┘       └────────────────────────┘       └────────────────────────┘
```

### Common Aggregations

```python
df.groupby("department")["salary"].mean()
df.groupby("department")["salary"].sum()
df.groupby("department").size()                 # → COUNT(*) per group
df.groupby(["department", "city"])["salary"].max()   # group by two keys
```

### Several Aggregations at Once

SQL:

```sql
SELECT department,
       COUNT(*)    AS headcount,
       AVG(salary) AS avg_salary,
       MAX(salary) AS top_salary
FROM employees
GROUP BY department;
```

Pandas:

```python
df.groupby("department").agg(
    headcount=("salary", "count"),
    avg_salary=("salary", "mean"),
    top_salary=("salary", "max"),
)
```

### `HAVING`

`HAVING` filters *after* grouping, so in Pandas you simply filter the result:

```python
result = df.groupby("department")["salary"].mean()
result[result > 50000]                      # → HAVING AVG(salary) > 50000
```

> [!TIP]
> `groupby()` puts the grouping key into the **index**. Add
> `.reset_index()` to turn it back into a normal column, or pass
> `as_index=False` to `groupby()`.

---

## 🎲 20. Distinct Values and Counting

| SQL                                             | Pandas                            |
| ----------------------------------------------- | --------------------------------- |
| `SELECT DISTINCT dept`                          | `df["dept"].unique()`             |
| `SELECT COUNT(DISTINCT dept)`                   | `df["dept"].nunique()`            |
| `SELECT dept, COUNT(*) GROUP BY dept`           | `df["dept"].value_counts()`       |
| `SELECT DISTINCT *`                             | `df.drop_duplicates()`            |
| Deduplicate on one column                       | `df.drop_duplicates(subset=["email"])` |

`value_counts()` is the single most useful exploration method in Pandas — reach
for it whenever you meet a new categorical column.

---

## 🤝 21. Joining (`JOIN`)

SQL:

```sql
SELECT *
FROM employees e
JOIN departments d ON e.id = d.id;
```

Pandas:

```python
pd.merge(employees, departments, on="id", how="inner")
```

```
┌─────────────────┐     ┌─────────────────┐
│ employees       │     │ departments     │
│ ─────────────   │     │ ─────────────   │
│ id   name       │     │ id   dept       │
│ 1    Gowtham    │  ⋈  │ 1    IT         │
│ 2    Arun       │     │ 2    HR         │
│ 3    Ravi       │     │ 4    Sales      │
└─────────────────┘     └─────────────────┘
                     │
                     ▼
    ┌────────────────────────────────┐
    │ merge(on="id", how="inner")    │
    │ ───────────────────────────    │
    │ id   name       dept           │
    │ 1    Gowtham    IT             │
    │ 2    Arun       HR             │
    │ (id 3 and 4 dropped)           │
    └────────────────────────────────┘
```

### The `how` Parameter

| SQL                | Pandas            | Keeps                        |
| ------------------ | ----------------- | ---------------------------- |
| `INNER JOIN`       | `how="inner"`     | Only matching keys (default) |
| `LEFT JOIN`        | `how="left"`      | All left rows                |
| `RIGHT JOIN`       | `how="right"`     | All right rows               |
| `FULL OUTER JOIN`  | `how="outer"`     | Everything from both sides   |
| `CROSS JOIN`       | `how="cross"`     | Every combination            |

If the key columns are named differently:

```python
pd.merge(
    employees, departments,
    left_on="dept_id",
    right_on="id",
    how="left",
)
```

### `UNION ALL` → `concat()`

`merge()` joins **side by side** (adds columns). `concat()` stacks **on top**
(adds rows):

```python
pd.concat([df_jan, df_feb], ignore_index=True)     # → UNION ALL
```

> [!TIP]
> Pass `indicator=True` to `merge()` and Pandas adds a `_merge` column telling
> you whether each row came from `left_only`, `right_only`, or `both`. It is the
> fastest way to debug a join that returned the wrong number of rows.

---

## ⚡ 22. Vectorisation vs `apply()`

This is the performance concept that separates beginners from everyone else.

```python
# ✅ Vectorised — runs in compiled C over the whole column at once
df["bonus"] = df["salary"] * 0.10

# ❌ apply — calls a Python function once per row (10–100× slower)
df["bonus"] = df["salary"].apply(lambda s: s * 0.10)

# ❌❌ iterrows — the slowest option available; avoid it
for i, row in df.iterrows():
    df.loc[i, "bonus"] = row["salary"] * 0.10
```

All three give the same answer. On a million rows, the first finishes in
milliseconds and the last takes minutes.

> [!IMPORTANT]
> **Rule of thumb:** if you are writing a `for` loop over a DataFrame, there is
> almost always a vectorised method that does it faster. Reach for `apply()` only
> when the logic genuinely cannot be expressed with column operations.

---

## 🧭 23. Working With the Index

```python
df = df.set_index("id")          # make a column the index
df = df.reset_index()            # push the index back into a column
df = df.reset_index(drop=True)   # discard the old index entirely
df = df.sort_index()             # → ORDER BY the index
```

Setting a meaningful index makes `loc` lookups much faster and lets Pandas
**align** two objects automatically when you combine them.

---

## 💾 24. Writing Data Back Out

```python
df.to_csv("out.csv", index=False)
df.to_json("out.json", orient="records", indent=2)
df.to_parquet("out.parquet")
df.to_sql("employees", connection, if_exists="replace", index=False)
```

> [!NOTE]
> `index=False` is almost always what you want for CSV. Without it, Pandas writes
> the index as an extra unnamed first column, and re-reading the file gives you a
> junk `Unnamed: 0` column.

---

## 📋 25. SQL → Pandas Cheat Sheet

| SQL                                | Pandas                                          |
| ---------------------------------- | ----------------------------------------------- |
| `SELECT *`                         | `df`                                            |
| `SELECT name`                      | `df["name"]`                                    |
| `SELECT name, salary`              | `df[["name", "salary"]]`                        |
| `SELECT COUNT(*)`                  | `len(df)`                                       |
| `SELECT DISTINCT dept`             | `df["dept"].unique()`                           |
| `WHERE age > 25`                   | `df[df["age"] > 25]`                            |
| `WHERE a AND b`                    | `df[(cond_a) & (cond_b)]`                       |
| `WHERE a OR b`                     | `df[(cond_a) \| (cond_b)]`                      |
| `WHERE NOT a`                      | `df[~(cond_a)]`                                 |
| `WHERE dept IN (...)`              | `df[df["dept"].isin([...])]`                    |
| `WHERE x IS NULL`                  | `df[df["x"].isna()]`                            |
| `ORDER BY salary`                  | `df.sort_values("salary")`                      |
| `ORDER BY salary DESC`             | `df.sort_values("salary", ascending=False)`     |
| `LIMIT 5`                          | `df.head(5)`                                    |
| `GROUP BY dept`                    | `df.groupby("dept")`                            |
| `GROUP BY dept` + `AVG(x)`         | `df.groupby("dept")["x"].mean()`                |
| `HAVING avg > n`                   | filter the grouped result                       |
| `JOIN ... ON`                      | `pd.merge(a, b, on="key", how="inner")`         |
| `LEFT JOIN`                        | `pd.merge(a, b, on="key", how="left")`          |
| `UNION ALL`                        | `pd.concat([a, b])`                             |
| `UPDATE ... SET ... WHERE ...`     | `df.loc[condition, column] = value`             |
| `ALTER TABLE ADD COLUMN`           | `df["new"] = ...`                               |
| `DELETE FROM ... WHERE ...`        | `df = df[~condition]`                           |

---

## 🚨 26. Gotchas Checklist

Keep this list next to you for the first few weeks:

- ✅ Use `&`, `|`, `~` — **never** `and`, `or`, `not`.
- ✅ Wrap every condition in parentheses: `(a) & (b)`.
- ✅ Never chain assignment — use one `df.loc[rows, cols] = value`.
- ✅ `df["x"]` gives a Series; `df[["x"]]` gives a DataFrame.
- ✅ `loc` slices are **inclusive** at both ends; `iloc` slices are not.
- ✅ `NaN != NaN` — always test with `.isna()`.
- ✅ An `int64` column becomes `float64` the moment it gains a null.
- ✅ Most methods return a new object — assign the result back.
- ✅ Avoid `iterrows()`; prefer vectorised column operations.
- ✅ Write CSVs with `index=False`.

---

> [!NOTE]
> **The one-sentence summary:** Pandas is SQL that lives in RAM, where the table
> is a `DataFrame`, the column is a `Series`, the `WHERE` clause is a boolean
> mask, and the index is a label — not a primary key.
