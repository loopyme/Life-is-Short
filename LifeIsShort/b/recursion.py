def main():
    from Word import word_list

    def print_a_word(word_list):
        if not word_list:
            return
        else:
            print(word_list.pop(), end=" ")
            print_a_word(word_list)

    print_a_word(word_list[::-1])
