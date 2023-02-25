def even_numbers():
    current = 0
    while current <= 20:
        yield current
        current += 2

gen = even_numbers()


for num in even_numbers():
    print(num)


assert next(gen) == 0
assert next(gen) == 2
assert next(gen) == 4
assert next(gen) == 6 
assert next(gen) == 8


''''

The main difference between an iterator and a generator is the way they are implemented.

An iterator is a class that implements the __iter__() and __next__() methods. The __iter__() method returns the iterator object itself, while the __next__() method returns the next item in the sequence. An iterator can be used to iterate over a finite sequence of values, but once it has been exhausted, it cannot be used again.

A generator, on the other hand, is a function that uses the yield keyword to return a generator object. When the generator function is called, it returns the generator object, which can be used to iterate over a sequence of values. The values are generated one at a time as needed, so generators are useful for working with large or infinite sequences of data.

Here are some key differences between iterators and generators:

Syntax: Iterators are implemented using a class, while generators are implemented using a function.

State: Iterators have an internal state that keeps track of the current item in the sequence, while generators maintain their state automatically between calls to the generator function.

Memory usage: Iterators can be used to iterate over large sequences of data, but they store all the data in memory at once. Generators, on the other hand, generate values on-the-fly as they are needed, so they are more memory-efficient.

Reusability: Iterators can only be used once to iterate over a sequence of values, while generators can be used multiple times to generate a new sequence of values each time they are called.

In summary, while iterators and generators are both used to iterate over a sequence of values, they differ in how they are implemented, their state management, memory usage, and reusability.
'''