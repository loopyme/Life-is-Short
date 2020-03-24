def main():
    from Word import words

    def print_before(func):
        print(words)

        def wrapper(*args, **kw):
            return func(*args, **kw)

        return wrapper

    @print_before
    def foo():
        pass

    foo()
