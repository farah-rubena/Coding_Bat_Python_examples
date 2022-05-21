#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way_func(a, b):

    new_array = []

    mid_point_a = len(a) // 2
    mid_point_b = len(b) // 2

    new_array.append(a[mid_point_a])
    new_array.append(b[mid_point_b])

    return new_array

x = middle_way_func([1,2,3], [4,5,6])
y = middle_way_func([7,7,7], [3,8,0])
z = middle_way_func([5,2,9], [1,4,5])
print(x,y,z)