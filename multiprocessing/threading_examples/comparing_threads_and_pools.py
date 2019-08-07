import multiprocessing
import threading
import time
import os

from multiprocessing.pool import ThreadPool


def square(n):
    # print(f"Worker process id for {n}: {os.getpid()}")
    return n * n


def run_process(data, method):

    p = multiprocessing.Pool(4)

    result = p.map(method, data)
    print(result)


def run_threading(data,  method):
    t = ThreadPool()
    result = t.map(method, data)
    print(result)


if __name__ == "__main__":

    processes_start_time = time.time()

    run_process(list(range(1, 10000)), square)

    print(f"Processes takes {time.time() - processes_start_time}")

    threads_start_time = time.time()

    run_threading(list(range(1, 10000)), square)

    print(f"Threads takes {time.time() - threads_start_time}")
