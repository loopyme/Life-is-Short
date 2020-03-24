from functools import partial


def main():
    from Word import word_list

    print_word = partial(print, end=" ")
    for w in word_list:
        print_word(w)
