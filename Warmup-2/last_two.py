#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


def last_two_func(string):

    if len(string) < 2:
        return string

    last2 = string[len(string)-2:]
    count = 0

    for i in range(len(string)-2):
        sub = string[i:i+2]
        if sub == last2:
            count += 1

    return count

x = last_two_func("hixxhi")
y = last_two_func("xaxaxaxx")
z = last_two_func("axxxaaxx")

print(x,y,z)

