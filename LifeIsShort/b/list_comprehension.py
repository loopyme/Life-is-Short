words = 'Life is short'

upper_word_list = ["LIFE", 'IS', 'SHORT', 'USE', 'PYTHON']
lower_word_list = [lower_w for w in upper_word_list if (lower_w := w.lower()) in words.lower()]

print(" ".join(lower_word_list))
