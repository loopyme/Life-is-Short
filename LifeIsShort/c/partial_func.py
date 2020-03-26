from functools import partial

word_list = ["Life", "is", "short"]

print_word = partial(print, end=" ")
for w in word_list:
    print_word(w)
