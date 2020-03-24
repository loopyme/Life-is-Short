from Word import word_list


def main():
    global print
    buildin_print, print = print, lambda value: buildin_print(value, end=' ')

    for w in word_list:
        print(w)


if __name__ == '__main__':
    main()
