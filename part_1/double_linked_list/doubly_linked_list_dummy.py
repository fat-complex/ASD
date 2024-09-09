from cgitb import reset

from doubly_linked_list import *

class Dummy(Node):
    def __init__(self):
        super().__init__(None)

class LinkedListWithDummy:
    def __init__(self):
        self.head = Dummy()
        self.tail = Dummy()

        self.reset()

    def insert(self, at_before_node: Node, node: Node | None):
        if node is None:
            return
        node.next = at_before_node
        node.prev = at_before_node.prev
        node.prev.next = node
        node.next.prev = node

    def add_in_tail(self, node: Node | None):
        self.insert(self.end(), node)

    def add_in_head(self, node: Node | None):
        self.insert(self.begin(), node)

    def delete(self, val, all=False):
        nodes: [Node] = self.find_all(val)
        for node in nodes:
            node.prev.next = node.next
            node.next.prev = node.prev

            if all is False:
                break

    def begin(self):
        return self.head.next

    def end(self):
        return self.tail

    def len(self):
        return len([i for i in self])

    def find(self, val):
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def clean(self):
        self.reset()

    def reset(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def __iter__(self):
        cursor: Node = self.head.next
        while type(cursor) != Dummy:
            yield cursor
            cursor = cursor.next

    @staticmethod
    def make(*args):
        linked_list: LinkedListWithDummy = LinkedListWithDummy()
        for arg in args:
            linked_list.add_in_tail(Node(arg))
        return linked_list

#=============================================================================

class CircularLinkedList:
    def __init__(self):
        self.dummy: Node = Dummy()
        self.reset()

    def find(self, val):
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def len(self):
        return len([i for i in self])

    def add_in_tail(self, node: Node):
        node.prev = self.dummy.prev
        node.prev.next = node
        node.next = self.dummy
        self.dummy.prev = node


    def delete(self, val, all=False):
        nodes: [Node] = self.find_all(val)
        for node in nodes:
            node.prev.next = node.next
            node.next.prev = node.prev

            if all is False:
                break

    def clean(self):
        self.reset()

    def insert(self, afterNode, newNode):
        if self.dummy.next is None:
            self.add_in_head(newNode)
            return

        if afterNode is None or afterNode == self.dummy.prev:
            self.add_in_tail(newNode)
            return

        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next = newNode

    def add_in_head(self, node: Node):
        node.next = self.dummy.next
        self.dummy.next.prev = node
        self.dummy.next = node
        node.prev = self.dummy

    def reset(self):
        self.dummy.next = None
        self.dummy.prev = None

        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

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


