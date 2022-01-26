class A:
    pass
    # def greeting(self):
        # print('Hello from A')

class B():
    def greeting(self):
        print('Hello from B')

class C(A):
    def greeting(self):
        print('Hello from C')

class D(A, B):
    pass


class E(D, C):
    pass


def search(name, age=None, mobile=None, greate=None):
    pass

# polymorphism
search(name='Nima')
search(age=23)
search(mobile=+989112222)
search(mobile=+98914569, name='farhad')
search()