1. Iterators
An Iterator is an object that remembers its state (where it is during a loop) and returns the next element when you ask for it.

To understand iterators, you first need to know the difference between an Iterable and an Iterator:

Iterable: Any object you can loop over (like a List, Set, or Dictionary). It has an __iter__() method that spawns an iterator.

Iterator: The actual engine behind the scenes that fetches items one by one. It implements the Iterator Protocol, which requires two methods:

__iter__(): Returns the iterator object itself.

__next__(): Returns the next value. When there are no items left, it raises a StopIteration exception.


The iteration protocol
In Python, anything you can loop over with for x in something is called an iterable. Under the hood, the for loop does two things:

Calls iter(something) to get an iterator — an object that knows how to produce values one at a time.
Repeatedly calls next(iterator) until the iterator raises StopIteration.

Lists, tuples, strings, dicts, and files are all iterables. You can build your own too — and there are two ways to do it: writing an iterator class, or writing a generator function.
Iterators — the manual way
An iterator is any object that defines two methods:

__iter__(self) — returns the iterator itself (so for loops can call iter() on it).
__next__(self) — returns the next value, or raises StopIteration when there's nothing left.