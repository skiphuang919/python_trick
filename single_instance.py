def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class MyClass(object):
    def __init__(self, x):
        self.x = x

if __name__ == '__main__':
    c1 = MyClass(1)
    c2 = MyClass(2)
    print 'c1 is c2: {}'.format(c1 is c2)
