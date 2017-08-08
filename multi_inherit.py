class A:

    def bar(self):
        print('A.bar')

    def foo(self):
        print('A.foo')


class B(A):

    def bar(self):
        print('B.bar')


class C(A):

    def bar(self):
        print('C.bar')

    def foo(self):
        print('C.foo')


class D(B, C):
    pass


class NewBase(object):

    def bar(self):
        print('Base.bar')

    def foo(self):
        print('Base.foo')


class New1(NewBase):

    def bar(self):
        print('New1.bar')


class New2(NewBase):

    def bar(self):
        print('New2.bar')

    def foo(self):
        print('New2.foo')


class New3(New1, New2):
    pass


if __name__ == '__main__':
    print('old class:')
    # DFS
    # search order: D -> B -> A -> C
    d = D()
    d.bar()
    d.foo()
    print('new class:')
    # BFS
    # search order New3 -> New1 -> New2 -> BaseNew
    n = New3()
    n.bar()
    n.foo()

