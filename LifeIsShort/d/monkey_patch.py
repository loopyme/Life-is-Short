word_list = ["Life", "is", "short"]


def main():
    global print
    buildin_print, print = print, lambda value: buildin_print(value, end=" ")

    for w in word_list:
        print(w)

    print = buildin_print


# See ..test.run_test.get_StringIO
