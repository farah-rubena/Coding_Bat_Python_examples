#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char_def(string, n):

    strng = list(string)
    x = strng.pop(n)
    return "".join(strng)


x = missing_char_def("kitten", 1)
y = missing_char_def("kitten", 0)
z = missing_char_def("kitten", 4)

print(x, y, z)
