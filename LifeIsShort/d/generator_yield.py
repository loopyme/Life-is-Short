word_list = ['Life', 'is', 'short']


def get_word():
    for w in word_list:
        yield w


def main():
    for w in get_word():
        print(w, end=" ")
