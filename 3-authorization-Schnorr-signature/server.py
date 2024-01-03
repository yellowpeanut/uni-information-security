import random


class Server:

    def __init__(self):
        self.t = 10

    def authenticate(self, user, r):
        e = random.randint(0, 2 ** self.t - 1)
        s = user.get_s(e)
        if r == ((user.g**s * user.y**e) % user.p):
            return True
        return False
