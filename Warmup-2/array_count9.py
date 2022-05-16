#Given an array of ints, return the number of 9's in the array.

def array_count9_func(lst):

    count = 0
    for item in lst:
        if item == 9:
            count += 1

    return count

x = array_count9_func([1,2,9])
y = array_count9_func([1,9,9])
z = array_count9_func([1,9,9,3,9])

print(x,y,z)