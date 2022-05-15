#Given a string, return a new string where the first and last chars have been exchanged.


def front_back_func(string):

    if len(string) <=1:
        return string

    first_char = string[0]
    last_char = string[-1]
    return last_char + string[1:-1] + first_char 


x = front_back_func('code')
y = front_back_func('a')
z = front_back_func('ab')

print(x,y,z)
