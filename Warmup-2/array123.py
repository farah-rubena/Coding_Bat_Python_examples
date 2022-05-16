#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123_func(lst):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for item in range(len(lst)-2):

        if lst[item] == 1 and lst[item + 1] == 2 and lst[item + 2] == 3:
            return True
    else:
        return False

x = array123_func([1,1,2,3,1])
y = array123_func([1,1,2,4,1])
z = array123_func([1,1,2,1,2,3])

print(x, y, z)