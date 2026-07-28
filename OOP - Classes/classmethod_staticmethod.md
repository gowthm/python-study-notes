
@classmethod and @staticmethod are decorators that change how methods behave inside a class. The main difference is what gets passed automatically as the first argument.


| Method type     | First parameter | Can access class?                 | Can access instance?   |
| --------------- | --------------- | --------------------------------- | ---------------------- |
| Instance method | `self`          | Yes (through `self.__class__`)    | Yes                    |
| `@classmethod`  | `cls`           | Yes                               | No (unless passed one) |
| `@staticmethod` | Nothing         | No (unless referenced explicitly) | No                     |


instance method
class method
static method



instance method:

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name)

s = Student("Alice")
s.introduce()


class method
class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

Python secretly changes it to

Student.show_school(Student)

The class itself is passed automatically.


Static method

class Student:

    @staticmethod
    def add(a, b):
        return a + b

Student.add(3, 5)

What Python actually does

Nothing extra.

It simply runs

Student.add(3, 5)

No self.

No cls.

It's just a normal function stored inside the class.


Side-by-side example
class Demo:

    def instance(self):
        print("self =", self)

    @classmethod
    def class_method(cls):
        print("cls =", cls)

    @staticmethod
    def static_method():
        print("Nothing is passed")

Now:

d = Demo()

d.instance()
Demo.class_method()
Demo.static_method()

Output:

self = <Demo object>
cls = <class '__main__.Demo'>
Nothing is passed

Notice:

instance() gets the object.
class_method() gets the class.
static_method() gets nothing automatically.
Why use @classmethod?

Imagine every student belongs to the same school.

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Now:

Student.change_school("XYZ School")

print(Student.school)

Output:

XYZ School

Since the method changes a class variable, it makes sense for it to receive the class (cls).

Why use @staticmethod?

Suppose you need a helper function that doesn't depend on any student or school.

class Student:

    @staticmethod
    def is_adult(age):
        return age >= 18

Use it like this:

Student.is_adult(20)

Output:

True

The function doesn't need a student object or the class itself—it just checks an age. Keeping it inside Student groups related functionality together.

The easiest way to remember
self → one object ("this student")
cls → the whole class ("the Student class")
No self or cls → just a normal helper function (@staticmethod)

