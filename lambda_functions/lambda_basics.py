# map()

#without lambda


def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)

# with lambda

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * x, numbers))

print(result)


# filter

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# sorted

students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 30}
]

students.sort(key=lambda student: student["age"])

print(students)