# Regular — returns the whole list
def evens_list(n):
    return [i for i in range(n) if i % 2 == 0]

# Iterator class — manual, verbose
class Evens:
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

# Generator — same behavior as Iterator, much shorter
def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i