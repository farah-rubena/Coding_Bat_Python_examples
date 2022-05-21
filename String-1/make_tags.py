#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags_func(tag, word):

    return f"<{tag}>{word}<{tag}>"


t = input("Enter the tag: ")
w = input("Enter the word: ")

x = make_tags_func(tag=t, word=w)
print(x)