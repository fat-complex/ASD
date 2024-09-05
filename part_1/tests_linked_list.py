import unittest
from linked_list import *


def to_values(list_nodes: [Node | None]):
    return [node.value for node in list_nodes]

class TestLenMethod(unittest.TestCase):
    def test_len_empty(self):
        target = LinkedList.from_args()
        length = target.len()
        expected = 0

        self.assertEqual(length, expected)

    def test_len_is_not_empty(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        length = target.len()
        expected = 5

        self.assertEqual(length, expected)

class TestFindAllMethod(unittest.TestCase):
    def test_find_in_empty_list(self):
        target = LinkedList.from_args()
        found = target.find_all(1)
        self.assertEqual(found, [])

    def test_not_found(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        found = target.find_all(44)
        self.assertEqual(found, [])

    def test_find_value_if_list_consist_of_one_elem(self):
        target = LinkedList.from_args(1)
        found = to_values(target.find_all(1))
        expected = [1]
        self.assertEqual(found, expected)

    def test_find_one_value(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        found = to_values(target.find_all(3))
        expected = [3]
        self.assertEqual(found, expected)

    def test_find_more_values(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5, 3, 64, 15, 3)
        found = to_values(target.find_all(3))
        expected = [3, 3, 3]
        self.assertEqual(found, expected)

    def test_find_more_values_if_not_exists(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5, 3, 64, 15, 3)
        found = to_values(target.find_all(6))
        expected = []
        self.assertEqual(found, expected)


class TestDeleteMethod(unittest.TestCase):
    def test_delete_from_empty_list(self):
        target = LinkedList.from_args()
        target.delete(23)
        expected = []

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_one_value_from_list(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        target.delete(3)
        expected = [1, 2, 4, 5]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_multiple_values_for_one(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5, 0, 3, 44)
        target.delete(3)
        expected = [1, 2, 4, 5, 0, 3, 44]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_value_if_list_consist_of_one_elem(self):
        target = LinkedList.from_args(1)
        target.delete(1)
        expected = []

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_from_non_existing_value(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        target.delete(6)
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_all_values_equal_3(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5, 0, 3, 44, 3)
        target.delete(3, all=True)
        expected = [1, 2, 4, 5, 0, 44]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_all_values(self):
        target = LinkedList.from_args(1, 1, 1, 1)
        target.delete(1, all=True)
        expected = []

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_all_but_2(self):
        target = LinkedList.from_args(1, 2, 1, 1)
        target.delete(1, all=True)
        expected = [2]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_delete_values_if_place_end(self):
        target = LinkedList.from_args(2, 2, 1, 1)
        target.delete(1, all=True)
        expected = [2, 2]

        self.assertEqual(to_values(target), expected)


class TestInsertMethod(unittest.TestCase):
    def test_insert_in_begin(self):
        target = LinkedList.from_args(2, 3, 4, 5)
        target.insert(None, Node(1))
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_insert_after_2(self):
        target = LinkedList.from_args(1, 2, 4, 5)
        after_node = target.find(2)
        target.insert(after_node, Node(3))
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_insert_after_1(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        after_node = target.find(1)
        target.insert(after_node, Node(23))
        expected = [1, 23, 2, 3, 4, 5]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_insert_after_5(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        after_node = target.find(5)
        target.insert(after_node, Node(23))
        expected = [1, 2, 3, 4, 5, 23]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_insert_in_empty_list(self):
        target = LinkedList.from_args()
        target.insert(None, Node(23))
        expected = [23]

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))


class TestCleanMethod(unittest.TestCase):
    def test_clean_empty(self):
        target = LinkedList.from_args()
        target.clean()
        expected = []

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))

    def test_clean_is_not_empty(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        target.clean()
        expected = []

        self.assertEqual(to_values(target), expected)
        self.assertEqual(target.len(), len(expected))


class TestSymmetricSumFunc(unittest.TestCase):
    def test_sum_for_equality_range(self):
        ll1 = LinkedList.from_args(1, 2, 3, 4, 5)
        ll2 = LinkedList.from_args(1, 2, 3, 4, 5)

        result = symmetric_sum(ll1, ll2)
        self.assertEqual(to_values(result), [2, 4, 6, 8, 10])

    def test_sum_for_non_equality_range(self):
        ll1 = LinkedList.from_args(1, 2, 3, 4, 5)
        ll2 = LinkedList.from_args(1, 2, 3)

        result = symmetric_sum(ll1, ll2)
        self.assertEqual(to_values(result), [])

    def test_sum_for_empty_range(self):
        ll1 = LinkedList.from_args()
        ll2 = LinkedList.from_args()

        result = symmetric_sum(ll1, ll2)
        self.assertEqual(to_values(result), [])


class TestBehaviour(unittest.TestCase):
    def test_noop(self):
        target = LinkedList.from_args(1, 2, 3, 4, 5)
        target.delete(3)
        not_fount_3 = target.find_all(3)
        self.assertEqual(not_fount_3, [])

        node_5 = target.find(5)
        target.insert(node_5, Node(3))
        self.assertEqual(to_values(target), [1, 2, 4, 5, 3])

        target.insert(None, Node(7))
        target.insert(None, Node(7))
        target.insert(None, Node(7))
        target.insert(node_5, Node(7))
        self.assertEqual(to_values(target), [7, 7, 7, 1, 2, 4, 5, 7, 3])

        target.delete(7, all=True)
        target.delete(3)
        node_4 = target.find(2)
        target.insert(node_4, Node(3))
        self.assertEqual(to_values(target), [1, 2, 3, 4, 5])

        target.clean()
        target.insert(None, Node(1))
        target.delete(1)
        self.assertEqual(to_values(target), [])

if __name__ == '__main__':
    unittest.main()
