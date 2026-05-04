

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            raise ValueError
        else:
            self.cookies += n

    def withdraw(self, n):
         if n > self.cookies:
            raise ValueError
         else:
            self.cookies -= n


    @property
    def capacity(self):
        return self._capacity

    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError


    @property
    def size(self):
        return self.cookies
