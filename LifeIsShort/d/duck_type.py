def main():
    from Word import words

    class Duck:
        def __init__(self):
            pass

        def __str__(self):
            return words

    d = Duck()
    print(d)
