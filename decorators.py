import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        res = end - start
        print(f"The function was ended via {res} seconds")

        return result
    return wrapper
