#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9_func(lst):

    range_count = lst[:4]
    for item in range(len(range_count)):
        if range_count[item]  == 9:
            return True
    return False


x = array_front9_func([1,2,9,3,4,])
y = array_front9_func([1,2,3,4,9])
z = array_front9_func([1,2,3,4,5])

print(x, y, z)