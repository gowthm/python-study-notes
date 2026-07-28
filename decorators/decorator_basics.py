"""Minimal decorator: wraps myfunc() to run extra code after it."""


def wrapper(func):
    def myinnerwrapper():
        func()
        print("This is main block from wrapper")

    return myinnerwrapper


@wrapper
def myfunc():
    print("This is from myfunc")


myfunc()  # Output: This is from myfunc \n This is main block from wrapper
