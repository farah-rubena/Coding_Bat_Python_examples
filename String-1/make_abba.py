#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba_func(a, b):

    return a + b + b + a


a = input("Enter the first word: ")
b = input("Enter the second word: ")

x = make_abba_func(a, b)

print(x)