#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front_3(string):

    front = string[:3]
    if len(string) <= 3:
        return string
    else:
        return front*3

x = front_3("Java")
y = front_3("Chocolate")
z = front_3("abc")

print(x, y, z)


