import multiprocessing
import os


def square(n):
    print(f"Worker process id for {n}: {os.getpid()}")
    return n * n


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    p = multiprocessing.Pool(4)

    result = p.map(square, my_list)

    print(result)
