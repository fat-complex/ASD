class Deque:
    def __init__(self):
        self.capacity = 4
        self.storage = [None] * self.capacity
        self.count = 0
        self.head = 0
        self.tail = 0

    def addFront(self, item):
        if self.size() == self.capacity:
            self.__reallocate()
        self.head = (self.head - 1) % self.capacity
        self.storage[self.head] = item
        self.count += 1

    def addTail(self, item):
        if self.size() == self.capacity:
            self.__reallocate()
        self.storage[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def removeFront(self):
        if not self.is_empty():
            top = self.top_value()
            self.head = (self.head + 1) % self.capacity
            self.count -= 1
            return top
        return None

    def removeTail(self):
        if not self.is_empty():
            back = self.back_value()
            self.tail = (self.tail - 1) % self.capacity
            self.count -= 1
            return back
        return None

    def __reallocate(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(0, self.size()):
            new_storage[i] = self.storage[(self.head + i) % self.size()]
        self.storage = new_storage
        self.head = 0
        self.tail = self.size()

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def top_value(self):
        if not self.is_empty():
            return self.storage[self.head]
        return None

    def back_value(self):
        if not self.is_empty():
            return self.storage[(self.tail - 1) % self.capacity]
        return None