import random

from pymongo import MongoClient


client = MongoClient()
db = client.clockify_denormalized

users_records_collection = db.users


def import_users_data(count=1000):
    for i in range(count):
        users_records_collection.insert_one(
            {f"user_{i}": random.randint(1, 10)}
        )

    print(f"{count} user records imported successfully")
