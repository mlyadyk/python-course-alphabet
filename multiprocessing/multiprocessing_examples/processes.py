import time
from multiprocessing import Process


def print_with_delay(delay, name=None):
    name = str(delay) if name is None else name
    it = 0
    while it <= 10:
        time.sleep(delay)
        it += 1
        print(f"My name is {name}; My delay is {delay}; This is my {it} iteration")


if __name__ == "__main__":
    processes = []
    for i in range(1, 5):
        p = Process(target=print_with_delay, args=(i, ))
        p.start()
        print(f"Start new process with pid {p.pid}; Parent pid {p._parent_pid}")
        processes.append(p)

    for p in processes:
        p.join()
        print("Join process")
        print(dir(p))
