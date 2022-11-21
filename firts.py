from multiprocessing import Process


def lag():
    ans = 0
    for i in range(1, 100000):
        ans += i ** i


def lag_machine():
    processes = []
    for _ in range(4):
        proc = Process(target=lag_machine)
        proc.start()
        processes.append(proc)
    proc = Process(target=lag)
    proc.start()
    processes.append(proc)
    for proc in processes:
        proc.join()


if __name__ == '__main__':
    print('My first git-repo')
    lag_machine()
