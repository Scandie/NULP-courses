from functools import wraps
import time

# === Task 1 ===
"""
Write a decorator which wraps functions to log function arguments and the return value on each call. Provide support for
both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both):

#>>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6 6
"""
print """     === Task 1 ===      \n"""  # to separate results in console


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
print multiply(y=5, x=2), '\n'*3

# === Task 2 ===
"""

Write a decorator to memoize functions with an arbitrary set of arguments.
Memoization is only possible if the arguments are hashable. Example function - Fibonacci.

Memoization - if function was already called with this arguments, then get result from cache. if not - execute function,
 store result in cache, and return result.

If the wrapper is called with arguments which are not hashable, then the wrapped function should just be called without
caching.

Note: To use args and kwargs as dictionary keys, they must be hashable, which basically means that they must be
immutable. args is already a tuple, which is fine, but kwargs have to be converted.
One way is tuple(sorted(kwargs.items())).

Such functions could be used to reduce cost of computation of some functions.
"""
print """     === Task 2 ===      \n"""  # to separate results in console
func_memo = {}


def memo(func):   # not sure about proper work of this wrapper

    @wraps(func)
    def memo_wrapper(*args, **kwargs):
        if kwargs and not args:

            n = (sorted(kwargs.items())[0][1])  # to simplify

            if n not in func_memo:               # actual wrapping work part
                func_memo[n] = func(**kwargs)
                return func(**kwargs)

            # print func_memo
            return func_memo[n]

        elif args and not kwargs:
            n = args[0]                         # to simplify

            if n not in func_memo:              # actual wrapping work part
                func_memo[n] = func(*args)
                return func(*args)

            # print func_memo
            return func_memo[n]

    return memo_wrapper


def timer(func):

    def time_wrapper(*args, **kwargs):
        t = time.time()                    # define timer start
        result = func(*args, **kwargs)
        print 'time wasted %f' % (time.time() - t)    # using timer to show the point of using memoize
        return result

    return time_wrapper


@timer
@memo
def fib(n):

    if n <= 1 or n == 2:
        return 1

    return int(fib(n=n-1) + fib(n-2))    # 'n=n' for kwargs filling and 'n' for args ones


print fib(n=12)
print func_memo
print fib(12)
print func_memo, '\n'*3

#
# Next peace of code for testing memo decorator with another function
#
func_memo = {}


@memo
def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k-1)     # change 'k' to 'k=k' for kwargs-type filling func_memo


print factorial(k=15)
print func_memo
print factorial(15)
print func_memo
