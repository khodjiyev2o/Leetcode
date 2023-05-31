a = 1

def inc_a():
    global a
    a += 2


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


s = make_counter()
print(s())

print(s())
