from functools import reduce


def cube(x):
    return x * x * x


def filters(a):
    return a > 4


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# map
newl = list(map(lambda x:x * x * x, l1))
print(newl)

# filter
newf = list(filter(lambda x:x > 4, l1))
print(newf)

# reduce
newr = reduce(lambda x, y:x + y, l1)
print(newr)
