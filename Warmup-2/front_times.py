#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


def front_times_func(string, n):

    if len(string) <3:
        return string
    return string[:3] * 3

x = front_times_func("Abc", 3)
y = front_times_func("to", 3)
z = front_times_func("Chocolate", 4)

print(x,y,z)