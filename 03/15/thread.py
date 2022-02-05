import time
import threading
import queue
import requests
from utils import is_prime, DEFAULT_NUMBERS


q = queue.Queue()


def worker(number):
    start = time.time()
    time.sleep(2)
    print(f'worker {number}, started {start}, finished {time.time()}')


def get_page(number):
    # while q.empty():  #  race condition
    while True:
        url = q.get()

        # print(f'Thread start {url}')
        try:
            response = requests.get(url)
        except:
            print(f"Error occurred {url}")
        print(f"get {number}\t completed {url}\t queue size {q.qsize()}")
        q.task_done()
        if q.empty():
            break

def show_is_prime():
        while True:
            number = q.get()
            is_prime ={number}
            q.task_done()
            if q.empty():
                break


def multi_thread():
    # for i in range(5):
        # print(worker(i))

    # for i in range(50):
    # t = threading.Thread(target=worker, args=(i, ))
    # t.start()

    # links = [
        # "htpp://7learn.com",
        # "https://googel.com",
    # ] * 30    


    # for link in links:
        # q.put(link)


    # threads = list()
    # for i in range(4):
        # t = threading.Thread(target=get_page, args=(i, ))
        # threads.append(t)
        # t.setDaemon(True)
        # t.start()

    # print("thread not join yet")
    # q.join()
    # for tr in threads:
        # tr.join()

    # print("ALL finish ")

    for num in DEFAULT_NUMBERS:
        q.put(num)
 
    threads = list()
    for i in range(4):
        t = threading.Thread(target=show_is_prime, args=(i, ))
        threads.append(t)
        t.setDaemon(True)
        t.start()
    
    print("thread not join yet")
    q.join()
    print("thread finished")



class CustomThread(threading.Thread):

    def __init__(self, limit, queue, *args, **kwargs):
        self.limit = limit
        self.queue = queue
        super().__init__(*args, **kwargs)


    def run(self):
        counter = 0
        while counter < self.limit:
            print(f"{self.name} Qsize: {self.queue.qsize()}")    
            number = self.queue.get()
            is_prime(number)
            counter += 1 
        print(f"Thread reached limitation")    

            # for _ in range(self.limit):
                    # number = self.queue.get()
                    # show_is_prime(number)
                    


if __name__ == '__main__':
    for i in DEFAULT_NUMBERS:
        q.put(i)

    c1 = CustomThread(100, q)
    c2 = CustomThread(50, q)

    c1.start()
    c2.start()

    c1.join()
    c2.join()