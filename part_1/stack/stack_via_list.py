from part_1.double_linked_list.doubly_linked_list_dummy import Node, CircularLinkedList

# 1, 2
class StackList:
    def __init__(self):
        self.list = CircularLinkedList.make()
        self.min_list = CircularLinkedList.make()
        self.total_sum = 0

    def size(self):
        return self.list.len()

    def push(self, value):
        self.list.add_in_head(Node(value))
        # min support
        self.__push_min(value)
        self.total_sum += value

    def __push_min(self, value):
        if self.min_list.len() == 0:
            self.min_list.add_in_head(Node(value))
        else:
            self.min_list.add_in_head(Node(min(value, self.min_list.top_value())))

    def pop(self):
        if self.size() > 0:
            top = self.list.top_value()
            self.list.pop_front()
            self.__pop_min(top)
            self.total_sum -= top
            return top
        return None

    def __pop_min(self, value):
        found = self.min_list.find(value)
        if found is not None:
            self.min_list.remove(found)

    def peek(self):
        if self.size() > 0:
            return self.list.top_value()
        return None

    def get_min_value(self):
        if self.min_list.len() > 0:
            return self.min_list.top_value()
        return None

    def get_average(self):
        if self.size() > 0:
            return self.total_sum // self.size()
        return None

# 3 while stack.size() > 0:
#     print(stack.pop())
#     print(stack.pop())
# Если число элементов на момент входа в цикл четное,  то всегда будут выведены верхние два вытолкнутых элемента,
# в противном случае на последней итерации  будут выведены сначала значение, а потом None

# Complexity: push - O(1), pop - O(1), peek - O(1)

