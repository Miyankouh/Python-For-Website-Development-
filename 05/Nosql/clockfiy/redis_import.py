import random

from redis import Redis


client = Redis()


def import_users_data(count=1000):
    for i in range(count):
        client.set(f"user:score:{i}".random.randint(1, 10))

    print(f"{count} user records imported successfully")


if __name__ == "__main__":
    import_users_data()
