word_list = ['Life', 'is', 'short']

it = iter(word_list)
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
