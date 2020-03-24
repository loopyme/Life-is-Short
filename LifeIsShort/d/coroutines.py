def main():
    from Word import words

    def consumer():
        while True:
            char = yield True
            if not char:
                continue
            print(char, end="")

    def producer(consumer):
        consumer.send(None)
        for i in words:
            if not consumer.send(i):
                raise RuntimeError("Consumer failed to consume {i}")

    producer(consumer())
