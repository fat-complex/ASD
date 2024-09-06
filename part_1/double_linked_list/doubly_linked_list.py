class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __repr__(self):
        return "{}".format(self.value)

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def delete(self, val, all=False):
        founds = self.find_all(val)
        for node in founds:
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev

            self.tail = node.prev if node == self.tail else self.tail

            if all is False:
                break

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return len([i for i in self])

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.add_in_head(newNode)
            return
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        if afterNode == self.tail:
            self.add_in_tail(newNode)
            return
        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        newNode.prev = None

    def reverse(self):
        node: Node | None = self.head
        while node is not None:
            next_node = node.next
            node.next = node.prev
            node.prev = next_node
            node = next_node

        self.head, self.tail = self.tail, self.head

    def has_loop(self) -> bool:
        first: Node | None = self.head
        second: Node | None = self.head

        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next

            if first == second:
                return True
        return False

    def sort(self):
        cursor = self.head
        while cursor is not None:
            current_node = cursor
            after_cursor = cursor.next
            while current_node is not None and current_node != self.head:
                if current_node.value < current_node.prev.value:
                    self.swap(current_node, current_node.prev)
                else:
                    break
            cursor = after_cursor

    def swap(self, node1: Node | None, node2: Node | None):
        if node1 is None or node2 is None or node1.value == node2.value:
            return

        if node1 == self.head:
            self.head = node2
        elif node2 == self.head:
            self.head = node1

        if node1 == self.tail:
            self.tail = node2
        elif node2 == self.tail:
            self.tail = node1

        tmp = node1.next
        node1.next = node2.next
        node2.next = tmp

        if node1.next is not None:
            node1.next.prev = node1
        if node2.next is not None:
            node2.next.prev = node2

        tmp = node1.prev
        node1.prev = node2.prev
        node2.prev = tmp

        if node1.prev is not None:
            node1.prev.next = node1
        if node2.prev is not None:
            node2.prev.next = node2

    # * special task. See tests tests_doubly_linked_list
    def merge(self, other):
        if self.head == other.head:
            return

        if self.head is None:
            self.head = other.head
            self.tail = other.tail
            return
        if other.head is None:
            return

        node1 = self.head
        node2 = other.head

        head: Node | None
        tail: Node | None
        if node1.value < node2.value:
            head = tail = node1
            node1 = node1.next
        else:
            head = tail = node2
            node2 = node2.next

        while node1 is not None and node2 is not None:
            if node1.value < node2.value:
                tail.next = node1
                node1.prev = tail
                tail = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2.prev = tail
                tail = node2
                node2 = node2.next

        tail.next = node1 if node1 is not None else node2
        tail.next.prev = tail
        while tail.next:
            tail = tail.next
        self.head = head
        self.tail = tail

    def __iter__(self):
        cursor: Node | None = self.head

        while cursor is not None:
            yield cursor
            cursor = cursor.next

    @staticmethod
    def make(*args):
        linked_list: LinkedList2 = LinkedList2()
        for arg in args:
            linked_list.add_in_tail(Node(arg))
        return linked_list