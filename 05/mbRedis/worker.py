import sys

from redis import Redis


client = Redis()


def watch_links_data(name):
    print(f"Worker {name} started")
    while True:
        link = client.blpop('links')  # b = block
        print(link)

    print(f"Worker {name} ended")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise KeyError("Worker name is required")
    watch_links_data(sys.argv[1])
