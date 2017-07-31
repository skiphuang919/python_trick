import time
from functools import wraps


def log_wrap(level='info'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print '[{level}] params: {param}'.format(level=level, param=args)
            t1 = time.time()
            res = func(*args, **kwargs)
            t2 = time.time()
            print '[{level}] costs: {time}'.format(level=level, time=t2-t1)
            return res
        return wrapper
    return decorator


@log_wrap()
def add_f(a, b):
    s = a + b
    return s


@log_wrap(level='warning')
def min_f(a, b):
    r = a - b
    return r

if __name__ == '__main__':
    r1 = add_f(1, 3)
    print r1
    r2 = min_f(8, 2)
    print r2
