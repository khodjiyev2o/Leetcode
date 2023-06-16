from Intermediatery_Python.decorator import *

print_full_name()

def first():
    sequence = []
    for i in range(1000000):
        sequence.append(i)
    return sequence


def first_generator():
    for i in range(100000000):
        yield i


sequence_list = first_generator()
sequence_generator = first()
# Print the memory usage of the two approaches
import sys


print(f"Memory usage (List): {sys.getsizeof(sequence_list)} bytes")
print(f"Memory usage (Generator): {sys.getsizeof(sequence_generator)} bytes")


