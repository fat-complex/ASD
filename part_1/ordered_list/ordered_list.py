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
        for node in self:
            if  self.compare(node.value, val) == 0:
                return node
        return None

    def delete(self, val):
        found = self.find(val)
        if found is not None:
            if found.prev is not None:
                found.prev.next = found.next
            else:
                self.head = found.next
            if found.next is not None:
                found.next.prev = found.prev

            self.tail = found.prev if found == self.tail else self.tail
            self.size -= 1

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

    def end(self):
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
        return self.end()

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