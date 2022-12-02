import time


def time_func(func):
    def wrap_func(*args, **kwargs):
        for i in range(2):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func