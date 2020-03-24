from functools import reduce


def main():
    from Word import word_list

    print(reduce(lambda x, y: x + " " + y, word_list))
