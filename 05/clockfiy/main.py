from datetime import datetime
from pymongo import MongoClient
from data import users, projects
from bson.objectid import ObjectId


client = MongoClient()
db = client.clockify_denormalized

users_collection = db.users
projects_collection = db.projects
reports_collection = db.reports


def store_once():
    """" just run at the first run of the script """
    users_collection.insert_many(users)
    projects_collection.insert_many(projects)


def save_record():
    moo = users_collection.find_one({"username": "moo"})
    shop = projects_collection.find_one({"name": "Onlin Shop"})

    report = reports_collection.insert_one({
        "user": moo,
        "project": shop,
        "start_time": datetime.now(),

    })
    return report['_id']


def set_end_time(object_id):
    query = {"id": ObjectId(object_id)}
    update = {"$set": {'end_time': datetime.now()}}
    reports_collection.update_one(query, update)


def show_reports():
    for report in reports_collection.find():
        duration = report['end_time'] - report['start_time']
        print(f"{report['user']['username']}\t {report['project']['name']}\t {duration.seconds}")


if __name__ == '__main__':
    # save_record()
    # set_end_time("6219db786f94ec82ab9b8d4b")
    show_reports()
