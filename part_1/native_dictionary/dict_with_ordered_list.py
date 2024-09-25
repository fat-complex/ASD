from part_1.ordered_list.ordered_list import OrderedList, Node

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return "({}: {})".format(self.key, self.value)


class OrderedListDict:
    def __init__(self):
        self.ordered_list = OrderedList(True)

    def put(self, key, value):
        found: Node | None = self.ordered_list.find(Entry(key, None))
        if found is not None:
            entry: Entry  = self.__unpack(found)
            entry.value = value
            return
        self.ordered_list.add(Entry(key, value))


    def remove(self, key):
        found: Node | None = self.ordered_list.find(Entry(key, None))
        if found is not None:
            self.ordered_list.delete(Entry(key, None))

    def is_key(self, key):
        return self.ordered_list.find(Entry(key, None)) is not None

    def get(self, key):
        found: Node | None = self.ordered_list.find(Entry(key, None))
        return self.__unpack(found).value if found is not None else None

    def __len__(self):
        return self.ordered_list.size

    def __unpack(self, node: Node) -> Entry:
        return node.value.elem


#Поиск и удаление работаю за O(LogN), вставка из-за пересчета индексов в случаях если вставляемый элемент
# находится не на концах списка просходит за О(N)