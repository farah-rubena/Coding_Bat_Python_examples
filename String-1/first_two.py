#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string ""

def first_two(string):

    if len(string) <=2:
        return string
    return string[:2]


x = first_two("Hello")
y = first_two("abcdefg")
z = first_two("ab")

print(x, y, z)

