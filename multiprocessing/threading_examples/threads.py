import threading
import time

from multiprocessing.pool import ThreadPool


def print_with_delay(delay, name=None):
    name = str(delay) if name is None else name
    i = 0
    while i <= 20:
        time.sleep(delay)
        i += 1
        print(f"My name is {name}; My delay is {delay}; This is my {i} iteration")


if __name__ == "__main__":
    start_time = time.time()
    t1 = threading.Thread(target=print_with_delay, args=(1,))
    t2 = threading.Thread(target=print_with_delay, args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Done! its take {time.time() - start_time}")
