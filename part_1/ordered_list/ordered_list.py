from itertools import count
from os import pread


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __repr__(self):
        return "{}".format(self.value)

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.size = 0

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        return 1

    def add(self, value):
        place = self.__get_place(value)
        self.__insert(place, Node(value))

    def find(self, val):
        result, _ = self.__find_if(self.head, lambda x: self.compare(x, val) == 0)
        return result

    def delete(self, val):
        found = self.find(val)
        self.__delete(found)

    def clean(self, asc):
        self.__ascending = asc
        self.head = self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def empty(self):
        return self.len() == 0

    def remove_duplicates(self):
        node: Node = self.head
        while node is not None:
            next_node, _ = self.__find_if(node, lambda x: x != node.value)
            self.__delete_range(node.next, next_node)
            node = next_node

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

    def range_contains(self, lst: []) -> bool:
        if len(lst) == 0:
            return True
        start = self.find(lst[0])
        if start is None:
            return False

        start = start.next
        for val in lst[1:]:
            if start is None or start.value != val:
                return False
            start = start.next

        return True

    def most_common(self):
        result = self.head.value if self.head is not None else None
        count = 1
        node: Node = self.head
        while node is not None:
            next_node, distance = self.__find_if(node, lambda x: x != node.value)
            result = node.value if distance > count else result
            count = distance
            node = next_node
        return result

    def __end(self):
        return self.tail if self.tail is None else self.tail.next

    def __iter__(self):
        cursor: Node | None = self.head

        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def __insert(self, at_before: Node, node: Node):
        if self.empty() or at_before is None:
            self.__add_in_tail(node)
            return

        if at_before.prev is None:
            self.__add_in_head(node)
            return

        node.next = at_before
        node.prev = at_before.prev
        node.prev.next = node
        node.next.prev = node
        self.size += 1

    def __add_in_tail(self, node: Node):
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.size += 1

    def __add_in_head(self, newNode):
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        newNode.prev = None
        self.size += 1

    def __get_place(self, value):
        if self.__ascending:
            return self.__find_insert_place(value, lambda l, r: self.compare(l, r) == -1)
        return self.__find_insert_place(value, lambda l, r: self.compare(l, r) == +1)

    def __find_insert_place(self, value, comparator):
        for node in self:
            if comparator(value, node.value):
                return node
        return self.__end()

    def __delete(self, node: Node):
        if node is not None:
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev

            self.tail = node.prev if node == self.tail else self.tail
            self.size -= 1

    def __delete_range(self, first: Node, last: Node):
        while first != last:
            next_node = first.next
            self.__delete(first)
            first = next_node

    def __find_if(self, from_pos: Node, predicate):
        distance = 0
        node: Node = from_pos
        while node is not None:
            if predicate(node.value):
                return node, distance
            node = node.next
            distance += 1
        return self.__end(), distance

    @staticmethod
    def make(asc: bool, *args):
        ordered = OrderedList(asc)
        for arg in args:
            ordered.add(arg)
        return ordered

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        s1: str = v1.lstrip().rstrip()
        s2: str = v2.lstrip().rstrip()
        return super().compare(s1, s2)

    @staticmethod
    def make(asc: bool, *args):
        ordered = OrderedStringList(asc)
        for arg in args:
            ordered.add(arg)
        return ordered