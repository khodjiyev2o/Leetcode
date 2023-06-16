import datetime


# decorator expects another function as argument


def logger(func_to_dec):
    # A wrapper function is defined on the fly
    def func_wrapper():
        # add any pre original function execution functionality
        print("Calling function: {} at {}".format(func_to_dec.__name__, datetime.datetime.now()))
        func_to_dec()

        # add any post original function execution functionality
        print("Finished calling : {}".format(func_to_dec.__name__))
        # over the func_to_decorate has been created.

    return func_wrapper


@logger
def print_full_name():
    print("My name is John Doe")


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
            return instances[cls]

    return get_instance


@singleton
class Test(object):
    pass


class Foo(object):
    pass

print(type(Foo))


if __name__ == "__main__":
    print("running decorator.py files")