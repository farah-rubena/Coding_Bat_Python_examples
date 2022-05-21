#Given an int array length 2, return True if it contains a 2 or a 3.


def has23_func(nums):

    for _ in nums:
        if _ == 2 or _ == 3:
            return True
    return False

x = has23_func([2,5])
y = has23_func([4,3])
z = has23_func([4,5])

print(x, y, z)