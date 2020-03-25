words = 'Life is short'


def print_before(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(text)
            return func(*args, **kw)

        return wrapper

    return decorator


@print_before(words)
def foo():
    pass


foo()
