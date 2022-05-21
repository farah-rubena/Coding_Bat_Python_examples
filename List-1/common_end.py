#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


def common_end_func(a, b):

    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    return False

x = common_end_func([1,2,3], [7,3])
y = common_end_func([1,2,3], [7,3, 2])
z = common_end_func([1,2,3], [1,3])

print(x, y, z)