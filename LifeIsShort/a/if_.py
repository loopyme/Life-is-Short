import random

word_list = ['Life', 'is', 'short']

last_word = ""
while True:
    word = random.choice(word_list)
    if (do_print := (word == "Life" and last_word == '') or
                    (word == "is" and last_word == 'Life') or
                    (word == "short" and last_word == 'is')):
        print(word, end=' ')
        last_word = word
    if word == 'short' and do_print:
        break
