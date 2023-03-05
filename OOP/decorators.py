

def double(func):
    def wrapper(*args, **kwargs):
        age = func(*args,**kwargs)
        age += 1
        return age
    return wrapper


def sum1(age: int = 1) -> int:
    return age + 1

funct = double(sum1)
print(funct())
