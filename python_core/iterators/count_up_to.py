"""A hand-built iterator class that counts up from 1 to a given limit."""


class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        """Required by the Iterator Protocol: returns the iterator itself."""
        return self

    def __next__(self):
        """Required by the Iterator Protocol: returns the next value or raises StopIteration."""
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current


counter = CountUpTo(4)
for n in counter:
    print(n)  # Output: 1 2 3 4, one per line
