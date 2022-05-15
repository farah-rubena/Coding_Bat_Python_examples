#Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.


def makes10_func(a, b):

    if (a + b) == 10 or (a == 10) or (b ==10):
        return True
    return False


x = makes10_func(9, 10)
y = makes10_func(9, 9)
z = makes10_func(1, 9)

print(x,y,z)