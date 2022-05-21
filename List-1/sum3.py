#Given an array of ints length 3, return the sum of all the elements.

def sum3_func(array):

    sum = 0

    for _ in array:
        sum += _
    return sum

x = sum3_func([1,2,3])
y = sum3_func([5, 11, 2])
z = sum3_func([7, 0, 0])

print(x, y, z)