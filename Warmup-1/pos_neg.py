#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(x, y, negative):

    if negative:
        return x < 0 and y < 0
    else:
        return (x < 0 or x > 0) and (y < 0 or y > 0)


x = pos_neg(1, -1, False)
y = pos_neg(-1, 1, False)
z = pos_neg(-4, -5, True)

print(x, y, z)