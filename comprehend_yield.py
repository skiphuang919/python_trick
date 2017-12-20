def gen():
    print('start')
    yield 'A'
    print('continue1')
    yield 'B'
    print('continue2')
    yield 'C'
    print('end')

g = gen()
print(g)
print(next(g))
print(next(g))
print(next(g))

for c in gen():
    print('-->', c)

# start
# --> A
# continue1
# --> B
# continue2
# --> C
# end
# <generator object gen at 0x7fd61a0b3e60>
# start
# A
# continue1
# B
# continue2
# C
