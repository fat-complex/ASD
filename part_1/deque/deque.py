class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Dummy(Node):
    def __init__(self):
        super().__init__(None)

class CircularLinkedList:
    def __init__(self):
        self.dummy: Node = Dummy()
        self.reset()
        self.size = 0

    def find(self, val):
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def len(self):
        return self.size

    def add_in_tail(self, node: Node):
        self.insert(self.end(), node)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def delete(self, val, all=False):
        nodes: [Node] = self.find_all(val)
        for node in nodes:
            self.remove(node)
            if all is False:
                break

    def clean(self):
        self.reset()

    def insert(self, at_before_node: Node, node: Node):
        node.next = at_before_node
        node.prev = at_before_node.prev
        node.prev.next = node
        node.next.prev = node
        self.size += 1

    def begin(self):
        return self.dummy.next

    def end(self):
        return self.dummy

    def add_in_head(self, node: Node):
        self.insert(self.begin(), node)

    def reset(self):
        self.dummy.next = None
        self.dummy.prev = None

        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        return self.size == 0

    def top_value(self):
        if self.len() > 0:
            return self.dummy.next.value
        return None

    def back_value(self):
        if self.len() > 0:
            return self.dummy.prev.value
        return None

    def pop_front(self):
        head = self.dummy.next
        if head is not None:
            self.remove(head)

    def pop_back(self):
        tail = self.dummy.prev
        if tail is not None:
            self.remove(tail)

    @staticmethod
    def make(*args):
        linked_list: CircularLinkedList = CircularLinkedList()
        for arg in args:
            linked_list.add_in_tail(Node(arg))
        return linked_list

    def __iter__(self):
        cursor: Node = self.dummy.next
        while type(cursor) != Dummy:
            yield cursor
            cursor = cursor.next

class Deque:
    def __init__(self):
        self.list = CircularLinkedList()

    def addFront(self, item):
        self.list.add_in_head(Node(item))

    def addTail(self, item):
        self.list.add_in_tail(Node(item))

    def removeFront(self):
        if not self.list.is_empty():
            top = self.list.top_value()
            self.list.pop_front()
            return  top
        return None

    def removeTail(self):
        if not self.list.is_empty():
            back = self.list.back_value()
            self.list.pop_back()
            return back
        return None

    def top_value(self):
        return self.list.top_value()

    def back_value(self):
        return self.list.back_value()

    def size(self):
        return self.list.size

    def is_empty(self):
        return self.list.is_empty()

# 7.1 В данном решении мера сложности удаления и вставки с обоих концов равна О(1),
#     так как в реализации Deque был выбран связной список.