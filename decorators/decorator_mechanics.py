def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper

@decorator
def hello():
    print("Hello")

"""
 Python automatically converts this to:
 def hello():
    print("Hello")

hello = decorator(hello)

Now let's see what happens.

decorator(hello) is called.

Inside decorator:

def decorator(func):
    # func points to original hello

    def wrapper(*args, **kwargs):
        ...

    return wrapper

Notice:

wrapper() is not called
It is returned

So after this line:

hello = decorator(hello)

hello is no longer the original function.

It is now:

hello = wrapper


Original hello
      │
      ▼
decorator(original hello)
      │
      ▼
returns wrapper
      │
      ▼
hello now points to wrapper


# Visual memory

## Without decorator:

hello()
   │
   ▼
Hello

## With decorator:

hello()
   │
   ▼
wrapper()
   │
   ├── Before
   ├── func()  ---> original hello()
   └── After

"""

def decorator(func):
    print("Decorator called")

    def wrapper():
        print("Wrapper called")
        func()

    return wrapper

def hello():
    print("Hello")

hello = decorator(hello)

print("Done")

hello()