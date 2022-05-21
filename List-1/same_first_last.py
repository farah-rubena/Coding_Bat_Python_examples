#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last_func(arr):

    equality = arr[0] == arr[-1]
    #print(equality)
    if len(arr) >= 1 and equality:
        return True
    return False

x = same_first_last_func([1,2,3])
y = same_first_last_func([1,2,3,1])
z = same_first_last_func([1,2,1])

print(x, y, z)