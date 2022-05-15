#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff_21(n):

    if n > 21:
        return abs(n-21)*2
    else:
        return abs(n-21)


x = diff_21(19)
y = diff_21(10)
z = diff_21(21)

print(x,y,z)