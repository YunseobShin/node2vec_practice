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

import multiprocessing
from functools import partial
from contextlib import contextmanager
import numpy as np
from numpy import array as ar
from scipy.spatial.distance import euclidean as dis

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()


def check_link(v, s, threshold):
    print('v shape: ', v.shape)
    print('s shape: ', s.shape)
    res = dis(v, s) < threshold
    if res.all():
        return True
    else:
        return False

def parallel_check_link(a, b, c, d):
    print(a)
    print(b)
    g = open('new_graph', 'a')
    for i in range(b.shape[0]):
        if np.array_equal(a, b[i]):
            continue
        if check_link(a, b[i], c):
            g.write(str(d+1)+' '+ str(i+1)+'\n')
    g.close()

    # return '{} & {} & {}'.format(a, b, c)



if __name__ == '__main__':
    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    nums = ar([ ar([1,2,3,4,5,6]), ar([2,3,4,5,6,7]),
                ar([3,2,5,4,5,80]), ar([4,5,5,1,5,92]) ])
    chunks = [nums[0:2], nums[2:4]]

    for i in range(nums.shape[0]):
        v = nums[i]
        print(v.shape)
        with poolcontext(processes=10) as pool:
            pool.map(partial(parallel_check_link, b=v, c=2, d=i), chunks)
        # print(results)

# Output: ['Brown & Sons', 'Wilson & Sons', 'Bartlett & Sons', ...


##################################################################################
#starmap

#!/usr/bin/env python3
# from functools import partial
# from itertools import repeat
# from multiprocessing import Pool, freeze_support
#
# def func(a, b):
#     print('a:', a)
#     print('b:', b)
#     print('a+b: ', a+b)
#     return a + b
#
# def main():
#     a_args = [1,2,3]
#     second_arg = 1
#     with Pool() as pool:
#         L = pool.starmap(func, [(1, 1), (2, 1), (3, 1)])
#         M = pool.starmap(func, zip(a_args, repeat(second_arg)))
#         N = pool.map(partial(func, b=second_arg), a_args)
#         assert L == M == N
#
# if __name__=="__main__":
#     freeze_support()
#     main()














####################################################
