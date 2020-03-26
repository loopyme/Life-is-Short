word_list = ["Life", "is", "short"]


def print_a_word(word_list):
    if not word_list:
        return
    else:
        print(word_list.pop(), end=" ")
        print_a_word(word_list)


print_a_word(word_list[::-1])
