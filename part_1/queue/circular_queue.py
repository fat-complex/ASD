class CircularQueue:
    def __init__(self, queue_size: int):
        self.buffer = [None] * queue_size
        self.capacity= queue_size
        self.head = 0
        self.tail = -1
        self.queue_size = 0

    def enqueue(self, item):
        if not self.is_full():
            self.tail = (self.tail + 1) % self.capacity
            self.buffer[self.tail] = item
            self.queue_size += 1

    def dequeue(self):
        if not self.is_empty():
            top = self.buffer[self.head]
            self.head = (self.head + 1) % self.capacity
            self.queue_size -= 1
            return top
        return None

    def size(self) -> int:
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def front(self):
        if not self.is_empty():
            return self.buffer[self.head]
        return None

    def back(self):
        if not self.is_empty():
            return self.buffer[self.tail]
        return None
