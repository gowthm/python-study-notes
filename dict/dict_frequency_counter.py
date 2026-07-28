"""Counts how many times each item appears in a list, using .get() to avoid KeyError."""

fruits = ["apple", "banana", "apple", 'cherry', 'apple']
count = {}

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1

print(count)  # Output: {'apple': 3, 'banana': 1, 'cherry': 1}
