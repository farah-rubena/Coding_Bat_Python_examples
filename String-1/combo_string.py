#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

def combo_string_func(a, b):

    if len(a) < len(b):
        return f"{a}{b}{a}"
    return f"{b}{a}{b}"

x = combo_string_func("Hello", "Hi")
y = combo_string_func("Hi", "Hello")
z = combo_string_func("aaa", "b")

print(x, y, z)