word_list = ["Life", "is", "short"]


def get_word():
    for w in word_list:
        print(w, end=" ")
        yield w


def main():
    for _ in get_word():
        pass
