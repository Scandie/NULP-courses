from functools import wraps

# === Task 1 ===
"""
Write a decorator which wraps functions to log function arguments and the return value on each call. Provide support for
both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both):

#>>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6 6
"""


def log(func):

    @wraps(func)
    def log_wrapper(*args, **kwargs):
        if kwargs:
            return 'you called: {}({}) \nit returned: {}'.format(func.__name__, str(kwargs)[1:-1], func(**kwargs))
        else:
            return 'you called: {} \nit returned: {}'.format(func.__name__ + str(args), func(*args))

    return log_wrapper


@log
def multiply(x, y):
    return x*y

print multiply(2, 3)
print multiply(y=5, x=2)
