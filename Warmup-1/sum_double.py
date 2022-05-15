#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double_func(x, y):

    if x == y:
        return (x+y) * 2
    else:
        return x + y


x = sum_double_func(1,2)
y = sum_double_func(3,2)
z = sum_double_func(2,2)

print(x,y,z)