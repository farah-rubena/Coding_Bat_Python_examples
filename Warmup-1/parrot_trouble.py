#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


def parrot_trouble_func(talking, hour):

    if (hour < 7 or hour > 20) and talking:
        return True
    return False


x = parrot_trouble_func(True, 6)
y = parrot_trouble_func(True, 7)
z = parrot_trouble_func(False, 6)

print(x,y,z)