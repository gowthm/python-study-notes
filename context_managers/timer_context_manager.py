# Without Context Manager

import time

start = time.time()

try:
    print("Working...")
finally:
    print(time.time() - start)


# With Context Manager

class Timer:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print("Time:", time.time() - self.start)


with Timer():
    print("Working...")
