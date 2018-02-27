def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class MyClass(object):
    pass


class SingletonClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass2(SingletonClass):
    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass3(metaclass=Singleton):
    pass


if __name__ == '__main__':
    c1 = MyClass()
    c2 = MyClass()
    print('c1 is c2: {}'.format(c1 is c2))

    c1 = MyClass2()
    c2 = MyClass2()
    print('c1 is c2: {}'.format(c1 is c2))

    c1 = MyClass3()
    c2 = MyClass3()
    print('c1 is c2: {}'.format(c1 is c2))


