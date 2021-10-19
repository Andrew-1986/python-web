from time import time
from multiprocessing import Process


def factorize (*number):
    for num in number:
        result = []
        for i in range(1, num + 1):
            if num%i == 0:
                result.append(i)
        
        print(result)


if __name__ == "__main__":
    time_start = time()
    factorize(128, 255, 99999, 10651060)
    time_end = time()
    print(time_end - time_start)

    time_start_process = time()
    process_1 = Process(target=factorize, args=(128, ))
    process_2 = Process(target=factorize, args=(255, ))
    process_3 = Process(target=factorize, args=(99999, ))
    process_4 = Process(target=factorize, args=(10651060, ))

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()

    time_end_process = time()
    print(time_end_process - time_start_process)
