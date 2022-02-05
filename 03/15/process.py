import multiprocessing
import time
from multiprocessing import Pool
from utils import is_prime, DEFAULT_NUMBERS


def multi_process():

    pool = Pool(2)
    while pool:
        pool.map(is_prime, DEFAULT_NUMBERS)
    print("all processes finished")


