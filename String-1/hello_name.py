#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name_func(name):

    return f'Hello {name}'

n = input("Enter a name: ")
x = hello_name_func(name=n)
print(x)