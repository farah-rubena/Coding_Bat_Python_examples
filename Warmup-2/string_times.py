#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times_func(string, n):

    return string * n

x = string_times_func("Hi",2)
y = string_times_func("Hi",3)
z = string_times_func("Hi",1)

print(x,y,z)


#OR

def string_times_fun(str, n):

    res = ""
    for _ in range(n):
        res += str

    return res

x = string_times_fun("Hi", 3)
y = string_times_fun("Hi", 2)
z = string_times_fun("Hi", 4)

print(x, y, z)