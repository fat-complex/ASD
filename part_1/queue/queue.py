class Queue:
    def __init__(self):
        self.buffer = []

    def enqueue(self, item):
        self.buffer.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.buffer.pop(0)
        return None


    def front(self):
        if self.size() > 0:
            return self.buffer[0]
        return None

    def back(self):
        if self.size() > 0:
            return self.buffer[self.size() - 1]
        return None

    def size(self):
        return len(self.buffer)

# Complexity: 1) enqueue. O(1) if no reallocate buffer else O(N): amortized ~O(N)
#             2) dequeue. O(N)