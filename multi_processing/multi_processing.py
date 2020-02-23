import multiprocessing


def processing_1():
    while True:
        print("进程1--------------")

def processing_2():
    while True:
        print('进程2--------------')

def main():
    p1 = multiprocessing.Process(target=processing_1)
    p2 = multiprocessing.Process(target=processing_2)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()