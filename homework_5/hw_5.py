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
   '''sync factorize'''
    print("Start sync factorize")
    time_start = time()
    factorize(128, 255, 99999, 10651060)
    time_end = time()
    print(time_end - time_start)

    '''multiprocessing factorize'''
    print("Start multiprocessing factorize")
    time_start_process = time()

    with multiprocessing.Pool() as Pool:
        result = Pool.map(factorize, (128, 255, 99999, 10651060))

    time_end_process = time()
    print(time_end_process - time_start_process)
