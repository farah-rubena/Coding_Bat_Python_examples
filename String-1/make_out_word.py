#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


def make_out_word_func(out_string, word):

    mid_str = len(out_string)//2

    return f"{out_string[:mid_str]} {word} {out_string[mid_str:]}"

x = make_out_word_func('<<<>>>', 'farah')
print(x)