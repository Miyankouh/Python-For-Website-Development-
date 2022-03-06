from utils.queue import Queue


def check_adv():
    q = Queue()
    for i in range(100):
        if i % 5 == 0:
            q.push('alert:1', i)
        if i % 7 == 0:
            q.push('alert:2', i)
        if i % 13 == 0:
            q.push('alert:3', i)
        if i % 23 == 0:
            q.push('alert:4', i)
    print('Done')


if __name__ == "__main__":
    check_adv()
