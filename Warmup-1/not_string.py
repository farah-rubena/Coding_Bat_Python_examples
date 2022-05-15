#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string_func(string):

    if string[:3] == "not":
        return string
    else:
        return "not" + string


x = not_string_func("candy")
y = not_string_func("x")
z = not_string_func("not bad")

print(x, y, z)