words = "Life is short"


class TaskRunner:
    @staticmethod
    def run(func, *args, **kwargs):
        func(*args, **kwargs)


runner = TaskRunner()
runner.run(lambda x: print(x), words)
