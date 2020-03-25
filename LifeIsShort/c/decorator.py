words = 'Life is short'


def print_before(func):
    # it is thickly to print here, words will be printed while decorating instead of calling the function
    print(words)

    def wrapper(*args, **kw):
        return func(*args, **kw)

    return wrapper


@print_before
def foo():
    pass
