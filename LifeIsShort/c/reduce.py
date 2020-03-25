from functools import reduce

word_list = ['Life', 'is', 'short']

print(reduce(lambda x, y: x + " " + y, word_list))
