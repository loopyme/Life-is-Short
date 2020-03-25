words = 'Life is short'


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


def main():
    producer(consumer())
