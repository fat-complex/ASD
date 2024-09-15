from part_1.stack.stack import Stack

class Queue:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def enqueue(self, item):
        self.input_stack.push(item)

    def dequeue(self):
        if self.output_stack.size() == 0:
            while self.input_stack.size() > 0:
                self.output_stack.push( self.input_stack.pop())
        return self.output_stack.pop()

    def front(self):
        return self.output_stack.peek() if self.input_stack.size() == 0 else self.input_stack.bottom()

    def back(self):
        return self.output_stack.bottom() if self.input_stack.size() == 0 else self.input_stack.peek()


    def size(self):
        return self.input_stack.size() + self.output_stack.size()