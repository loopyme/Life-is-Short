def main():
    from Word import word_list

    def get_word():
        for w in word_list:
            yield w

    for w in get_word():
        print(w, end=" ")
