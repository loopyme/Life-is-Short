words = "Life is short"

upper_word_list = ["LIFE", "IS", "SHORT", "USE", "PYTHON"]
word_generator = (
    lower_w for w in upper_word_list if (lower_w := w.lower()) in words.lower()
)

for w in word_generator:
    print(w, end=" ")
# word_generator is StopIteration now
