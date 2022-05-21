#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start_func(a, b):

    return a[1:] + b[1:]

x = non_start_func("Hello", "There")
y = non_start_func("java", "code")
z = non_start_func("shotl", "java")

print(x, y, z)
