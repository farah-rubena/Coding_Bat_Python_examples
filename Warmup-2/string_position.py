#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_position_func(string):

    res = ""

    for char in range(len(string)):
        res += string[:char+1]

    return res

x = string_position_func("Code")
y = string_position_func("abc")
z = string_position_func("ab")

print(x,y,z)



