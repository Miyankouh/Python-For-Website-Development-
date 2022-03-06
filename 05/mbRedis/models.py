class User:
    def __init__(self, id):
        self.id = id


class Alert:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id


class Adv:
    def __init__(self, id):
        self.id = id
