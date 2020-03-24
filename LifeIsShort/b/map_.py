def main():
    from Word import words
    upper_word_list = ["LIFE", 'IS', 'SHORT', 'USE', 'PYTHON']
    word_list = filter(lambda x: x.lower() in words.lower(), upper_word_list)
    word_list = map(lambda x: x.lower(), word_list)

    for w in word_list:
        print(w, end=" ")
