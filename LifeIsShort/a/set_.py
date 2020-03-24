def main():
    stammer_word_list = ['Life', 'Life', 'Life', 'is', 'is', 'is', 'is', 'is', 'short', 'short', 'short', 'short']

    (res_words := list(set(stammer_word_list))).sort(key=stammer_word_list.index)

    print(" ".join(res_words))
