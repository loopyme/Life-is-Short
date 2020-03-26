import asyncio

word_list = ["Life", "is", "short"]


async def print_task():
    for w in word_list:
        await asyncio.sleep(0.1)
        print(w, end=" ")


def run():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(print_task())
    loop.close()


main = run
