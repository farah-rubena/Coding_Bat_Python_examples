#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


def first_half_func(string):

    mid_len = len(string) // 2

    return string[0:mid_len]


x = first_half_func("WooHoo")
y = first_half_func("HelloThere")
z = first_half_func("abcdef")

print(x, y, z)