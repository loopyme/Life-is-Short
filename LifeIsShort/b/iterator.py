def main():
    from Word import word_list

    it = iter(word_list)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            break
