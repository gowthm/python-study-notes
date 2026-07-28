"""
Three ways to produce the even numbers below n, from most to least verbose:
a regular function (builds the whole list upfront), a hand-written iterator
class (manual state management), and a generator function (same behavior,
far less code).
"""


def evens_list(n):
    """Regular function — returns the whole list at once."""
    return [i for i in range(n) if i % 2 == 0]


class Evens:
    """Iterator class — manual, verbose. You track state (self.i) yourself."""

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.n:
            val = self.i
            self.i += 1
            if val % 2 == 0:
                return val
        raise StopIteration


def evens(n):
    """Generator — same behavior as Evens, much shorter."""
    for i in range(n):
        if i % 2 == 0:
            yield i
