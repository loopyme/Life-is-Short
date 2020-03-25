word_list = ['Life', 'is', 'short']


class foo:
    def __init__(self):
        print(word_list[0], end=" ")

    def __enter__(self):
        print(word_list[1], end=" ")

    def __exit__(self, *args):
        print(word_list[2], end=" ")


def main():
    with foo() as _:
        pass
