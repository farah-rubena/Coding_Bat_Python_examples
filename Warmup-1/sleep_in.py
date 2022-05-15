#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in_func(weekday, vacation):

    if not weekday or vacation:
        return True
    else:
        return False


x = sleep_in_func(False, False)
y = sleep_in_func(True, False)
z = sleep_in_func(False, True)

print(x, y, z)