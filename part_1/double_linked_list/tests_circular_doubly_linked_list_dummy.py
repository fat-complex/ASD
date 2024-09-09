import unittest
from doubly_linked_list_dummy import *

LinkedList = CircularLinkedList

def to_values(list_nodes: [Node | None]):
    return [node.value for node in list_nodes]

class TestCleanMethod(unittest.TestCase):
    def test_clean(self):
        ll1 = LinkedList.make()
        ll1.clean()
        self.assertEqual(to_values(ll1), [])

        ll2 = LinkedList.make(1, 2, 3, 4, 5)
        ll2.clean()
        self.assertEqual(to_values(ll2), [])


class TestLenMethod(unittest.TestCase):
    def test_len(self):
        ll1 = LinkedList.make()
        self.assertEqual(ll1.len(), 0)

        ll2 = LinkedList.make(1, 2, 3, 4, 5)
        self.assertEqual(ll2.len(), 5)

class TestFindMethod(unittest.TestCase):
    def test_find_in_empty_list(self):
        ll = LinkedList.make()
        not_found = ll.find(23)
        self.assertEqual(not_found, None)

    def test_not_found_in_list(self):
        ll = LinkedList.make(1, 2, 3, 4, 5)
        not_found = ll.find(23)
        self.assertEqual(not_found, None)

    def test_find_in_list(self):
        ll = LinkedList.make(1, 2, 3, 4, 5)
        found = ll.find(3)
        self.assertEqual(found.value, 3)


class TestFindAllMethod(unittest.TestCase):
    def test_find_in_empty_list(self):
        ll = LinkedList.make()
        not_found = ll.find_all(33)
        self.assertEqual(not_found, [])

    def test_not_found_in_list(self):
        ll = LinkedList.make(1, 2, 3, 4, 5)
        not_found = ll.find_all(33)
        self.assertEqual(not_found, [])

    def test_find_in_list(self):
        ll1 = LinkedList.make(1, 2, 3, 4, 5)
        found = ll1.find_all(3)
        self.assertEqual(to_values(found), [3])

        ll2 = LinkedList.make(3, 2, 3, 4, 5, 3)
        found = ll2.find_all(3)
        self.assertEqual(to_values(found), [3, 3, 3])

        ll3 = LinkedList.make(3)
        found = ll3.find_all(3)
        self.assertEqual(to_values(found), [3])

        ll3 = LinkedList.make(3, 3, 3, 3, 3)
        found = ll3.find_all(3)
        self.assertEqual(to_values(found), [3, 3, 3, 3, 3])


class TestDeleteMethod(unittest.TestCase):
    def test_delete_from_empty_list(self):
        ll = LinkedList.make()
        ll.delete(3)
        self.assertEqual(to_values(ll), [])

    def test_delete_from_non_empty_list(self):
        ll1 = LinkedList.make(1)
        ll1.delete(1)
        self.assertEqual(to_values(ll1), [])
        self.assertEqual(ll1.len(), 0)

        ll2 = LinkedList.make(1, 2, 3, 4, 5)
        ll2.delete(1)
        self.assertEqual(to_values(ll2), [2, 3, 4, 5])
        self.assertEqual(ll2.len(), 4)

        ll3 = LinkedList.make(1, 2, 3, 4, 5)
        ll3.delete(5)
        self.assertEqual(to_values(ll3), [1, 2, 3, 4])
        self.assertEqual(ll3.len(), 4)

        ll4 = LinkedList.make(1, 2, 3, 4, 5)
        ll4.delete(3)
        self.assertEqual(to_values(ll4), [1, 2, 4, 5])
        self.assertEqual(ll4.len(), 4)

        ll5 = LinkedList.make(3, 1, 2, 3, 4, 5, 3)
        ll5.delete(3)
        self.assertEqual(to_values(ll5), [1, 2, 3, 4, 5, 3])
        self.assertEqual(ll5.len(), 6)

        ll6 = LinkedList.make(1, 2, 3, 4, 5)
        ll6.delete(5)
        self.assertEqual(to_values(ll6), [1, 2, 3, 4])
        self.assertEqual(ll6.len(), 4)

        ll7 = LinkedList.make(1, 2, 3, 4, 5)
        ll7.delete(5, all=True)
        self.assertEqual(to_values(ll7), [1, 2, 3, 4])
        self.assertEqual(ll7.len(), 4)

        ll8 = LinkedList.make(1, 2, 3, 4, 5)
        ll8.delete(1, all=True)
        self.assertEqual(to_values(ll8), [2, 3, 4, 5])
        self.assertEqual(ll8.len(), 4)

        ll9 = LinkedList.make(1, 2, 3, 4, 5)
        ll9.delete(3, all=True)
        self.assertEqual(to_values(ll9), [1, 2, 4, 5])
        self.assertEqual(ll9.len(), 4)

        ll10 = LinkedList.make(3, 1, 2, 3, 4, 5, 3)
        ll10.delete(3, all=True)
        self.assertEqual(to_values(ll10), [1, 2, 4, 5])
        self.assertEqual(ll10.len(), 4)

        ll11 = LinkedList.make(3, 3, 3, 3, 3)
        ll11.delete(3, all=True)
        self.assertEqual(to_values(ll11), [])
        self.assertEqual(ll11.len(), 0)

        ll12 = LinkedList.make(1, 3, 3, 3, 3, 3, 1)
        ll12.delete(3, all=True)
        self.assertEqual(to_values(ll12), [1, 1])
        self.assertEqual(ll12.len(), 2)

        ll13 = LinkedList.make(3, 3, 3, 1, 1, 3, 3)
        ll13.delete(3, all=True)
        self.assertEqual(to_values(ll13), [1, 1])
        self.assertEqual(ll13.len(), 2)

        ll14 = LinkedList.make(1, 3, 3, 3, 3, 3, 3)
        ll14.delete(3, all=True)
        self.assertEqual(to_values(ll14), [1])
        self.assertEqual(ll14.len(), 1)

        ll15 = LinkedList.make(3, 3, 3, 3, 3, 3, 1)
        ll15.delete(3, all=True)
        self.assertEqual(to_values(ll15), [1])
        self.assertEqual(ll15.len(), 1)


class TestAddInHeadMethod(unittest.TestCase):
    def test_add_in_head(self):
        ll1 = LinkedList.make()
        ll1.add_in_head(Node(1))
        self.assertEqual(to_values(ll1), [1])

        ll2 = LinkedList.make(2, 3, 4, 5)
        ll2.add_in_head(Node(1))
        self.assertEqual(to_values(ll2), [1, 2, 3, 4, 5])

        ll3 = LinkedList.make()
        for val in [1, 2, 3, 4, 5]:
            ll3.add_in_head(Node(val))
        self.assertEqual(to_values(ll3), [5, 4, 3, 2, 1])


class TestInsertMethod(unittest.TestCase):
    def test_insert(self):
        ll1 = LinkedList.make()
        ll1.insert(None, Node(1))
        self.assertEqual(to_values(ll1), [1])
        self.assertEqual(ll1.len(), 1)

        ll2 = LinkedList.make(1)
        ll2.insert(None, Node(2))
        self.assertEqual(to_values(ll2), [1, 2])
        self.assertEqual(ll2.len(), 2)

        ll3 = LinkedList.make(1, 3, 4, 5)
        after_node = ll3.dummy.next
        ll3.insert(after_node, Node(2))
        self.assertEqual(to_values(ll3), [1, 2, 3, 4, 5])
        self.assertEqual(ll3.len(), 5)

        ll4 = LinkedList.make(1, 2, 3, 4, 5)
        after_node = ll4.dummy.prev
        ll4.insert(after_node, Node(6))
        self.assertEqual(to_values(ll4), [1, 2, 3, 4, 5, 6])
        self.assertEqual(ll4.len(), 6)

        ll5 = LinkedList.make(1, 2, 4, 5)
        after_node = ll5.find(2)
        ll5.insert(after_node, Node(3))
        self.assertEqual(to_values(ll5), [1, 2, 3, 4, 5])
        self.assertEqual(ll5.len(), 5)

        ll6 = LinkedList.make()
        for val in [1, 2, 3, 4, 5]:
            ll6.insert(None, Node(val))
        self.assertEqual(to_values(ll6), [1, 2, 3, 4, 5])
        self.assertEqual(ll6.len(), 5)

        ll8 = LinkedList.make(1, 2, 3, 4, 5)
        for val in [1, 2, 3, 4, 5]:
            ll8.insert(ll8.dummy.prev, Node(val))
        self.assertEqual(to_values(ll8), [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
        self.assertEqual(ll8.len(), 10)


if __name__ == '__main__':
    unittest.main()
