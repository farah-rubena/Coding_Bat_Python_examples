#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end_func(string):

    return string[-2:] * 3

x = extra_end_func("Hello")
print(x)