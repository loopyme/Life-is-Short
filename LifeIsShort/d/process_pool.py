from multiprocessing import Pool, Manager


def get_word(que):
    word_list = ['Life', 'is', 'short']
    for word in word_list:
        que.put(word)


def print_word(que):
    for i in range(3):
        print(que.get(), end=" ")


def main():
    process_pool = Pool(2)
    word_que = Manager().Queue()

    process_pool.apply_async(print_word, args=(word_que,))
    process_pool.apply_async(get_word, args=(word_que,))

    process_pool.close()
    process_pool.join()
