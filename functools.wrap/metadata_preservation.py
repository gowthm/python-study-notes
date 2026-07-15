# without functools.wrap

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")

print(greet.__name__)  # Outputs: wrapper
print(greet.__doc__)   # Outputs: None

# with functools.wraps

from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")

print(greet.__name__)  # Outputs: greet
print(greet.__doc__)   # Outputs: This function greets the user.



