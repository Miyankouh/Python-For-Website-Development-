from time import sleep

class LazyLoader:
    def __init__(self,cls):
        self.cls = cls
        self.object = None

    def __getattr__(self,item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)
        
class MySqlHandler():
    def __init__(self):
        sleep(1)

    def connect(self):
        return "Connect to the  mysql stablished"

class MongoHandler():
    def __init__(self):
        sleep(100)

    def show(self):
        return "Hello from mongo"


class NotificationCenterHandler():
    def __init__(self):
        sleep(3)

    def get(self):
        return "Hello from notif"


if __name__ == "__main__":
    mysql = LazyLoader(MySqlHandler)
    mongo = LazyLoader(MongoHandler)
    notif = LazyLoader(NotificationCenterHandler)

    print(mysql.connect())
    print(notif.get())
    # print(mongo.show())

    print(mysql.connect())
    print(notif.get())

    print(mysql.connect())
    print(notif.get())

    print(mysql.connect())
    print(notif.get())