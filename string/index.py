# def plus_one(number):
#     return number + 1

# add_one = plus_one
# add_one(5)




# def plus_one(number):
#     def add_one(number):
#         return number + 1


#     result = add_one(number)
#     return result
# plus_one(4)



# def plus_one(number):
#     return number + 1

# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)

# print(function_call(plus_one))


# def say_hello():
#     def function_hi():
#         return 'hello'
#     return function_hi
# print(say_hello())


# def print_message(message):
#     "Enclosong Function"
#     def message_sender():
#         "Nested Function"
#         return message

#     return  message_sender
# message = print_message("Some random message")
# print(message())

# def uppercase_decorator(function):
#     def wrapper(arg1):
#         func = function(arg1)
#         uppercase = func.upper()
#         return uppercase
#     return wrapper


# def split_sentence(function):
#     def wrapper(arg1):
#         func = function(arg1)
#         splitted = func.split()
#         return splitted
#     return wrapper

# @split_sentence
# @uppercase_decorator
# def say_goodbye(message):
#     return message

# print(say_goodbye('hello'))



# def getting_arbitrary_arguments(function):
#     def wrapper(*args, **kwargs):
#         print(f'args are {args}, kwargs are {kwargs}')
#         return function
#     return wrapper

# def simple(*args, **kwargs):
#     return f'function simple  is called with args {args} and kwargs {kwargs}'

# s1 = getting_arbitrary_arguments(simple('goodbye','goodbye',key='hello'))
# s2 = getting_arbitrary_arguments(simple('goodbye','goodbye',key='hello'))
# print(s1())
# print(s2('goodbye','goodbye',key='hello'))

# def double_sum(function):
#     def wrapper(*args, **kwargs):
#         kwargs['numbers'] = [x*x for x in kwargs['numbers']]
#         return function(*args, **kwargs) 
#     return wrapper

# @double_sum
# def sum_all(numbers: list[int]) -> int:
#     print("calling sum function inside original function")
#     return sum(numbers)

# print(sum_all(numbers=[1,2,3,4]))

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")