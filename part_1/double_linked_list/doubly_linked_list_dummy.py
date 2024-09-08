class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __repr__(self):
        return "{}".format(self.value)


class LinkedListDummy:
    def __init__(self):
        self.dummy: Node = Node(None)
        self.reset()

    def add_in_tail(self, node: Node):
        node.prev = self.dummy.prev
        node.prev.next = node
        node.next = self.dummy
        self.dummy.prev = node


    def find(self, val):
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val) -> [Node]:
        return [node for node in self if node.value == val]

    def delete(self, val, all=False):
        nodes: [Node] = self.find_all(val)
        for node in nodes:
            node.prev.next = node.next
            node.next.prev = node.prev

            if all is False:
                break

    def clean(self):
        self.reset()

    def len(self):
        return len([i for i in self])

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
        linked_list: LinkedListDummy = LinkedListDummy()
        for arg in args:
            linked_list.add_in_tail(Node(arg))
        return linked_list

    def __iter__(self):
        cursor: Node = self.dummy.next
        while cursor != self.dummy:
            yield cursor
            cursor = cursor.next

    def __repr__(self):
        return str([node for node in self])


