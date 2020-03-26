words = "Life is short"


class Duck:
    def __init__(self):
        pass

    def __str__(self):
        return words


def main():
    d = Duck()
    print(d)
