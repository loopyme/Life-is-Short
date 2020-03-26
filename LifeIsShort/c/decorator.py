words = "Life is short"


def print_before(func):
    # it is almost a trap to print here, words will be printed while decorating instead of calling foo
    # Be aware that @ is just syntactic sugar, decorating is equivalent to `print_before(foo)`

    print(words)

    def wrapper(*args, **kw):
        return func(*args, **kw)

    return wrapper


@print_before
def foo():
    pass
