words = 'Life is short'


def lazy_print(text):
    return lambda: print(text)


task = lazy_print(words)
task()
