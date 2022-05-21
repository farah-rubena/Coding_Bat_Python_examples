#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


def reverse3_func(array):

    return array[::-1]

x = reverse3_func([1,2,3])
y = reverse3_func([5,11,9])
z = reverse3_func([7,0,0])

print(x, y, z)