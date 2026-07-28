"""
Shows a side effect of plain decorators: wrapping greet() replaces it with
wrapper(), so greet.__name__ and greet.__doc__ now describe wrapper, not
the original function. See functools_wrap/ in this repo for the fix
(@functools.wraps), which restores the original metadata.
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")


print(greet.__name__)  # Output: wrapper
print(greet.__doc__)   # Output: None
