# multiprocessing
# import os
#
# from multiprocessing import Process, current_process
#
#
# def doubler(number):
#     result = number * 2
#     proc_name = current_process().name
#     print('{0} doubled to {1} by process id: {2}'.format(number, result, proc_name))
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     procs = []
#     proc = Process(target=doubler, args=(5,))
#
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,))
#         procs.append(proc)
#         proc.start()
#
#     proc = Process(target=doubler, name='Test', args=(2,))
#     proc.start()
#     procs.append(proc)
#
#     for proc in procs:
#         proc.join()

########################################################
# lock
# from multiprocessing import Process, Lock
#
# def printer(item, lock):
#     lock.acquire()
#     try:
#         print(item)
#     finally:
#         lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'twice', 10]
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()
######################################################
#logging

# import logging
# import multiprocessing
# from multiprocessing import Process, Lock
#
# def printer(item, lock):
#     # Print out the item that was passed in
#     lock.acquire()
#     try:
#         print(item)
#     finally:
#         lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#     multiprocessing.log_to_stderr()
#     logger = multiprocessing.get_logger()
#     logger.setLevel(logging.INFO)
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()
#########################################################
# Pool

# from multiprocessing import Pool
#
# def doubler(n1, n2):
#     return n1 * n2
#
# if __name__ == '__main__':
#     numbers = [5, 10, 20]
#     pool = Pool(processes = 3)
#     print(pool.map(doubler, numbers))




####################################################
# Pool with multiple arguments using partial

# import multiprocessing
# from functools import partial
# from contextlib import contextmanager
#
# @contextmanager
# def poolcontext(*args, **kwargs):
#     pool = multiprocessing.Pool(*args, **kwargs)
#     yield pool
#     pool.terminate()
#
# def merge_names(a, b):
#     return '{} & {}'.format(a, b)
#
# if __name__ == '__main__':
#     names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
#     with poolcontext(processes=3) as pool:
#         results = pool.map(partial(merge_names, b='Sons'), names)
#     print(results)

# Output: ['Brown & Sons', 'Wilson & Sons', 'Bartlett & Sons', ...


##################################################################################
#starmap

#!/usr/bin/env python3
from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support

def func(a, b):
    print('a:', a)
    print('b:', b)
    print('a+b: ', a+b)
    return a + b

def main():
    a_args = [1,2,3]
    second_arg = 1
    with Pool() as pool:
        L = pool.starmap(func, [(1, 1), (2, 1), (3, 1)])
        M = pool.starmap(func, zip(a_args, repeat(second_arg)))
        N = pool.map(partial(func, b=second_arg), a_args)
        assert L == M == N

if __name__=="__main__":
    freeze_support()
    main()














####################################################
