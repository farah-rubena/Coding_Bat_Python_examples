#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6_func(list_1):

    if list_1[0] == 6 or list_1[-1] == 6:
        return True
    return False


x = first_last6_func([1,2,6])
y = first_last6_func([6, 1,2,3])
z = first_last6_func([13, 6, 1, 2, 3])

print(x, y, z)