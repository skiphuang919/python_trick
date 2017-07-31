import time
from functools import wraps


def log_wrap1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'params: {param}'.format(param=args)
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print 'costs: {time}'.format(time=t2-t1)
        return res
    return wrapper


def log_wrap2(level='info'):
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


@log_wrap1
def add_f1(a, b):
    s = a + b
    return s


@log_wrap1
def min_f1(a, b):
    r = a - b
    return r


@log_wrap2()
def add_f2(a, b):
    s = a + b
    return s


@log_wrap2(level='warning')
def min_f2(a, b):
    r = a - b
    return r

if __name__ == '__main__':
    r1 = add_f1(1, 3)
    print r1
    r2 = min_f1(8, 2)
    print r2
    r3 = add_f2(1, 3)
    print r3
    r4 = min_f2(8, 2)
    print r4
