from part_1.deque.deque import Deque
from part_1.double_linked_list.doubly_linked_list_dummy import CircularLinkedList, Node


class DequeWithMinSupport(Deque):
    def __init__(self):
        super().__init__()
        self.list_as_stack = CircularLinkedList()

    def addFront(self, item):
        super().addFront(item)
        self.__push_min(item)

    def addTail(self, item):
        self.list.add_in_tail(Node(item))
        self.__push_min(item)

    def removeFront(self):
        if not self.list.is_empty():
            top = self.list.top_value()
            self.list.pop_front()
            self.__pop_min(top)
            return  top
        return None

    def removeTail(self):
        if not self.list.is_empty():
            back = self.list.back_value()
            self.list.pop_back()
            self.__pop_min(back)
            return back
        return None

    def get_min(self):
        return self.list_as_stack.top_value()

    def __push_min(self, value):
        if self.list_as_stack.len() == 0:
            self.list_as_stack.add_in_head(Node(value))
        else:
            self.list_as_stack.add_in_head(Node(min(value, self.list_as_stack.top_value())))

    def __pop_min(self, value):
        found = self.list_as_stack.find(value)
        if found is not None:
            self.list_as_stack.remove(found)