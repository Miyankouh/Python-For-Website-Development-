class DatabaseHandler():  # Singelton
    inistance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inistance'):
            cls.inistance = super(*args, **kwargs)
        return cls.inistance



if __name__ == "__main__":
    s1 = DatabaseHandler()
    s2 = DatabaseHandler()
    s3 = DatabaseHandler()
    s4 = DatabaseHandler()

    print(id(s1))
    print(id(s2))
    print(id(s3))
    print(id(s4))

    print(id(s1) == id(s2) == id(s3) == id(s4))