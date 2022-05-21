#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3_func(arr):

    return arr[::-1]

x = rotate_left3_func([1,2,3])
y = rotate_left3_func([5,11,9])
z = rotate_left3_func([7,0,0])

print(x, y, z)