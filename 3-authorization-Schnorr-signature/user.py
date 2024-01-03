import random
import pickle
import os

class User:

    def __init__(self, username):
        self.username = username
        self.k = 0
        self.p, self.q = self.__get_pq()
        self.x = random.randint(1, self.q - 1)
        self.g = self.__generate_g(self.p, self.q)
        self.y = self.__generate_y(self.p, self.x, self.g)

        with open(os.path.dirname(__file__) + "/pkl" + f'/{self.username}.pkl', 'wb') as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)
        with open(os.path.dirname(__file__) + "/pkl" + f'/{self.y}{self.x}.pkl', 'wb') as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)

    def start_authentication(self):
        self.k = random.randint(1, self.q - 1)
        r = self.g**self.k % self.p
        return r

    def __get_pq(self):
        p = self.__generate_p()
        q = random.randint(2, 5)*p + 1
        return p, q

    def __generate_p(self, mx=500):
        nums = []
        for x in range(1, mx):
            for y in range(2, x):
                if x % y == 0:
                    break
                else:
                    nums.append(x)
        p = nums[random.randint(5, len(nums)-1)]
        return p

    def __generate_g(self, p, q):
        g = 2
        while g**q % p != 1:
            g += 1
        return g

    def __generate_y(self, p, x, g):
        y = 2
        while (g**x * y) % p != 1:
            y += 1
        return y

    def get_s(self, e):
        return (self.k + self.x*e) % self.p
