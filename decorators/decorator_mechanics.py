"""
Under-the-hood mechanics of `@decorator` syntax.

Python compiles:
    @decorator
    def hello(): ...

into:
    def hello(): ...
    hello = decorator(hello)

`decorator(hello)` runs immediately and returns `wrapper` (not called, just
returned), so the name `hello` gets rebound to `wrapper`. From then on,
hello() actually calls wrapper(), which calls the original hello via `func`.

For the full step-by-step execution trace (with *args/**kwargs), see
decorator_arguments_flow.md in this folder.
"""


def decorator(func):
    print("Decorator called")

    def wrapper():
        print("Wrapper called")
        func()  # calls the original hello(), captured via closure

    return wrapper


def hello():
    print("Hello")


hello = decorator(hello)  # hello now points to wrapper, not the original function

print("Done")

hello()  # Output: Wrapper called \n Hello
