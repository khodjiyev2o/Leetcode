class EventNumbers:
    def __init__(self):
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 2
        if self.current > 20:
            raise StopIteration
        return self.current

events = EventNumbers()

for i in events:
    print(i)


my_list = [1, 2, 3]
my_iterator = iter(my_list)   # calls the iter() method

print(next(my_iterator))   # calls the next() method to get the first item
print(next(my_iterator))   # calls the next() method to get the second item
print(next(my_iterator))    # calls the next() method to get the third item
