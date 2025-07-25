class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Cookies went to negative numbers, whaatt?")

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Cookies can not extend capacity of jar")

    def __str__(self):
        return "🍪" * self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must not be a negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar(10)
    jar.deposit(5)
    print(jar)


main()
