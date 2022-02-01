from abc import ABC, abstractmethod 


class Message:
    def __init__(self,subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]
    
    def send(self, to_user):
        if to_user.__class__  not in self.current.allowed:
            print(f"{self.current.__class__} is not allowed to send email to {to_user.__class__}")
        else:
            self.flow.append(to_user)
            print("message sent to {to_user.__class__}")

class AbstractUser(ABC):
    pass


class ManagerDirector(AbstractUser):
    @property
    @abstractmethod
    def allowed(self):
        pass


class InternalManeger(AbstractUser):
    allowed = []


class Supervisor(AbstractUser):
    allowed = [ManagerDirector]


class Operator(AbstractUser):
    allowed = [InternalManeger]


class Client(AbstractUser):
    allowed = [Operator]


if __name__ == '__main__':
    opt = Operator()
    spr = Supervisor()
    inm = InternalManeger()
    mnd = ManagerDirector

    client = Client()
    message = Message("Issue #123456", "issue description", client)

    message.send(opt)
    message.send(spr)
    message.send(inm)
    message.send(mnd)
