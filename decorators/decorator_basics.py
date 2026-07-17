def wrapper(func):
    def myinnerwrapper():
        func()
        print("This is main block from wrapper")
        
    return myinnerwrapper

@wrapper
def myfunc():
    print("This is from myfunc")

myfunc()