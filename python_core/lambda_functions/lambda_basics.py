"""Lambda functions used with map(), filter(), and sorted()/.sort()."""

# map() — without lambda
def square(x):
    return x * x


numbers = [1, 2, 3, 4]
result = list(map(square, numbers))
print(result)  # Output: [1, 4, 9, 16]

# map() — with lambda
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * x, numbers))
print(result)  # Output: [1, 4, 9, 16]

# filter() — keep only even numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)  # Output: [2, 4, 6]

# sorted()/.sort() — sort by a custom key
students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 30}
]

students.sort(key=lambda student: student["age"])
print(students)  # Output: sorted by age -> Alice(20), John(25), Bob(30)
