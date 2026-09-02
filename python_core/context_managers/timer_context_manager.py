"""
Contrasts manual try/finally timing with a custom class-based context
manager (Timer) that measures elapsed time via __enter__/__exit__.
"""

import time

# --- Without a context manager ---
start = time.time()

try:
    print("Working...")
finally:
    print(time.time() - start)


# --- With a context manager ---
class Timer:
    """Times how long the code inside its `with` block takes to run."""

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print("Time:", time.time() - self.start)


with Timer():
    print("Working...")
