from functools import wraps


# def welcome(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("Welcome")
#         result = fn(*args, **kwargs)
#         return result
#
#     return wrapper

def welcome(name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Welcome {name}")
            result = fn(*args, **kwargs)
            return result

        return wrapper
    return decorator


@welcome("Tom")
def my_fun(message: str):
    print(f"Hello {message}")


@welcome("Mary")
def my_fun_2():
    print("my fun 2")


# f1 = welcome(my_fun)
# f1("Jack")

my_fun("Jack")

print(my_fun.__name__)
