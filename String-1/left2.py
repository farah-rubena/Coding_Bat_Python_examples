#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2_func(string):

    if len(string)<=2:
        return string
    return string[2:]+string[:2]

x = left2_func("hello")
y = left2_func("java")
z = left2_func("Hi")

print(x, y, z)