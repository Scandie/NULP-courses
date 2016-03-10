from functools import wraps
import time
from collections import Hashable

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


def memo(func):   # not sure about proper work of this wrapper

    func_memo = {}

    # @wraps(func)
    def memo_wrapper(*args, **kwargs):

        def args_hashable(arguments):

            ishash = True
            for arg in arguments:
                if not isinstance(arg, Hashable):
                    ishash = False
                    break
            if ishash:
                # print str(arguments) + ' are hashable'
                return True
            else:
                return False

        if kwargs and not args:
            my_args = tuple([value for key, value in (sorted(kwargs.items()))])  # to simplify
            if args_hashable(my_args):

                if my_args not in func_memo:               # actual wrapping work part
                    func_memo[my_args] = func(**kwargs)
                    # print func_memo
                return func_memo[my_args]

            else:
                # print str(my_args) + " aren't hashable"
                return func(**kwargs)

        elif args and not kwargs:
            my_args = args

            if args_hashable(my_args):

                if my_args not in func_memo:               # actual wrapping work part
                    func_memo[my_args] = func(*args)
                    # print func_memo
                return func_memo[my_args]

            else:
                # print str(my_args) + " aren't hashable"
                return func(*args)

    return memo_wrapper


def timer(func):

    @wraps(func)
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


print fib(n=6)
print fib(4)
print '\n'*3

#
# Next peace of code for testing memo decorator with another function
#


@timer
@memo
def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k-1)     # change 'k' to 'k=k' for kwargs-type filling func_memo


print factorial(k=8)
print factorial(6)
