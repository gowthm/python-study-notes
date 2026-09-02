"""Basic generator: yields numbers one at a time instead of returning a full list."""


def count(limit):
    i = 0
    while i < limit:
        i += 1
        yield i


gen = count(6)

for x in gen:
    print(x)  # Output: 1 2 3 4 5 6, one per line
