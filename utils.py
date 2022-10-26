import time


def verify_func(func, *pargs, **kargs):
    start = time.perf_counter()
    ret_val = func(*pargs, **kargs)
    stop = time.perf_counter()
    print("\tExecution time: {}".format(stop - start))
    return ret_val