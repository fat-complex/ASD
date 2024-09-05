class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

    def __repr__(self):
        return "{}".format(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def delete(self, val, all=False):
        (prev, found) = self.find_prev(val)
        while found is not None:
            if prev:
                prev.next = found.next
            else:
                self.head = found.next
            self.tail = prev if found == self.tail else self.tail
            if not all:
                break
            (prev, found) = self.find_prev(val)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return len([i for i in self])

    def insert(self, afterNode, newNode):
        if newNode is None:
            return
        if self.head is None and self.tail is None:
            self.add_in_tail(newNode)
            return
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode

    @staticmethod
    def from_args(*args):
        linked_list: LinkedList = LinkedList()
        for arg in args:
            node: Node = Node(arg)
            linked_list.add_in_tail(node)
        return linked_list

    def __iter__(self):
        node: Node | None = self.head
        while node is not None:
            yield node
            node = node.next

    def find_prev(self, val):
        if self.head is not None and self.head.value == val:
            return None, self.head
        node = self.head
        while node is not None and node.next is not None:
            if node.next.value == val:
                return node, node.next
            node = node.next

        return None, None

def symmetric_sum(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result = LinkedList()
    if list1.len() == list2.len():
        for node1, node2 in zip(list1, list2):
            result.add_in_tail(Node(node1.value + node2.value))

    return result
