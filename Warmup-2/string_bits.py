#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits_func(string):

    res = ""

    for char in string:
        res = string[0::2]

    return res

x = string_bits_func("Hello")
y = string_bits_func("Hi")
z = string_bits_func("Heeololeo")

print(x,y,z)

#OR


def string_bits_fun(strg):

    result = ""

    for char in range(len(strg)):
        if char % 2 == 0:
            result += strg[char]

    return result

x = string_bits_fun("Hello")
y = string_bits_fun("Hi")
z = string_bits_fun("Heeololeo")

print(x,y,z)
