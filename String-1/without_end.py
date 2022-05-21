#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end_func(string):

    return string[1:-1]

x = without_end_func("Hello")
y = without_end_func("Python")
z = without_end_func("coding")

print(x, y, z)