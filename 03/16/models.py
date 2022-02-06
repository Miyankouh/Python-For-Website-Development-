class Supervisor:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    
    @classmethod
    def sampel(cls):
        return cls("ali","123","0912451789")