import unittest

from part_1.ordered_list.ordered_list import OrderedList, Node

def to_values(list_nodes: [Node | None]):
    return [node.value for node in list_nodes]

class TestAddMethod(unittest.TestCase):
    def test_add_ascending(self):
        ordered = OrderedList.make(True, 1, 2)
        self.assertEqual(to_values(ordered), [1, 2])
        self.assertEqual(ordered.len(), 2)

        ordered = OrderedList.make(True, 1, 2, 4)
        ordered.add(3)
        self.assertEqual(to_values(ordered), [1, 2, 3, 4])
        self.assertEqual(ordered.len(), 4)

        ordered = OrderedList.make(True, 1, 2, 4)
        ordered.add(3)
        ordered.add(5)
        self.assertEqual(to_values(ordered), [1, 2, 3, 4, 5])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(True, 5)
        ordered.add(1)
        ordered.add(2)
        ordered.add(3)
        ordered.add(4)
        self.assertEqual(to_values(ordered), [1, 2, 3, 4, 5])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(True, 1, 1, 1, 1)
        ordered.add(2)
        self.assertEqual(to_values(ordered), [1, 1, 1, 1, 2])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(True, 1, 1, 1, 1)
        ordered.add(0)
        self.assertEqual(to_values(ordered), [0, 1, 1, 1, 1])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(True, 1, 1, 1, 1)
        ordered.add(1)
        self.assertEqual(to_values(ordered), [1, 1, 1, 1, 1])
        self.assertEqual(ordered.len(), 5)

    def test_add_descending(self):
        ordered = OrderedList.make(False, 1, 2)
        self.assertEqual(to_values(ordered), [2, 1])
        self.assertEqual(ordered.len(), 2)

        ordered = OrderedList.make(False, 4, 2, 1)
        ordered.add(3)
        self.assertEqual(to_values(ordered), [4, 3, 2, 1])
        self.assertEqual(ordered.len(), 4)

        ordered = OrderedList.make(False, 4, 2, 1)
        ordered.add(3)
        ordered.add(5)
        self.assertEqual(to_values(ordered), [5, 4, 3, 2, 1])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(False, 5)
        ordered.add(1)
        ordered.add(2)
        ordered.add(3)
        ordered.add(4)
        self.assertEqual(to_values(ordered), [5, 4, 3, 2, 1])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(False, 1, 1, 1, 1)
        ordered.add(2)
        self.assertEqual(to_values(ordered), [2, 1, 1, 1, 1])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(False, 1, 1, 1, 1)
        ordered.add(0)
        self.assertEqual(to_values(ordered), [1, 1, 1, 1, 0])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedList.make(False, 1, 1, 3, 3, 4)
        ordered.add(2)
        self.assertEqual(to_values(ordered), [4, 3, 3, 2, 1, 1])
        self.assertEqual(ordered.len(), 6)


class TestCleanMethod(unittest.TestCase):
    def test_clean(self):
        ordered = OrderedList.make(True, 1, 2, 3, 4, 5)

        ordered.clean(False)
        self.assertEqual(to_values(ordered), [])
        self.assertEqual(ordered.len(), 0)

        for val in range(1, 6):
            ordered.add(val)
        self.assertEqual(to_values(ordered), [5, 4, 3, 2, 1])
        self.assertEqual(ordered.len(), 5)


class TestFindMethod(unittest.TestCase):
    def test_find(self):
        ordered = OrderedList.make(True, 1, 2, 3, 4, 5)
        self.assertTrue(ordered.find(3) is not None)
        self.assertTrue(ordered.find(10) is None)

        ordered = OrderedList.make(False, 1, 2, 3, 4, 5)
        self.assertTrue(ordered.find(3) is not None)
        self.assertTrue(ordered.find(10) is None)


class TestDeleteMethod(unittest.TestCase):
    def test_delete(self):
        ordered = OrderedList(True)
        ordered.delete(2)
        self.assertEqual(ordered.size, 0)

        ordered = OrderedList.make(True, 1)
        ordered.delete(1)
        self.assertEqual(ordered.size, 0)

        ordered = OrderedList.make(True, 4, 3, 2, 1)
        ordered.delete(3)
        self.assertEqual(to_values(ordered), [1, 2, 4])
        self.assertEqual(ordered.size, 3)

        ordered = OrderedList.make(False, 1, 2, 3, 4)
        ordered.delete(3)
        self.assertEqual(to_values(ordered), [4, 2, 1])
        self.assertEqual(ordered.size, 3)


class TestRemoveDuplicateMethod(unittest.TestCase):
    def test_remove_duplicate(self):
        ordered = OrderedList.make(True, 1, 1, 2, 3, 3, 3, 4, 5, 5)
        ordered.remove_duplicates()
        self.assertEqual(to_values(ordered), [1, 2, 3, 4, 5])
        self.assertEqual(ordered.size, 5)

        ordered = OrderedList.make(True, 1, 1, 1, 1, 1)
        ordered.remove_duplicates()
        self.assertEqual(to_values(ordered), [1])
        self.assertEqual(ordered.size, 1)


class TestMergeMethod(unittest.TestCase):
    def test_emplace_merge(self):
        ll1 = OrderedList.make(True)
        ll2 = OrderedList.make(True,1, 2)
        ll1.merge(ll2)
        self.assertEqual(to_values(ll1), [1, 2])

        ll1 = OrderedList.make(True,1, 2)
        ll2 = OrderedList.make(True)
        ll1.merge(ll2)
        self.assertEqual(to_values(ll1), [1, 2])

        ll1 = OrderedList.make(True, 1, 2, 3)
        ll2 = OrderedList.make(True, 4, 5, 6)
        ll1.merge(ll2)
        self.assertEqual(to_values(ll1), [1, 2, 3, 4, 5, 6])

        ll1 = OrderedList.make(True, 1, 3, 6)
        ll2 = OrderedList.make(True, 2, 4, 5)
        ll1.merge(ll2)
        self.assertEqual(to_values(ll1), [1, 2, 3, 4, 5, 6])


class TestRangeContainsMethod(unittest.TestCase):
    def test_range_contains(self):
        ordered = OrderedList.make(True, 1, 2, 3, 4, 5)

        self.assertTrue(ordered.range_contains([1]))
        self.assertTrue(ordered.range_contains([1, 2]))
        self.assertTrue(ordered.range_contains([1, 2, 3]))
        self.assertTrue(ordered.range_contains([1, 2, 3, 4]))
        self.assertTrue(ordered.range_contains([1, 2, 3, 4, 5]))

        self.assertTrue(ordered.range_contains([5]))
        self.assertTrue(ordered.range_contains([4, 5]))
        self.assertTrue(ordered.range_contains([3, 4, 5]))
        self.assertTrue(ordered.range_contains([2, 3, 4, 5]))

        self.assertFalse(ordered.range_contains([1, 2, 3, 4, 5, 6]))
        self.assertFalse(ordered.range_contains([1, 2, 3, 7]))
        self.assertFalse(ordered.range_contains([7, 1, 2, 3]))


class TestMostCommonMethod(unittest.TestCase):
    def test_most_common(self):
        ordered = OrderedList.make(True)
        self.assertEqual(ordered.most_common(), None)

        ordered = OrderedList.make(True, 1)
        self.assertEqual(ordered.most_common(), 1)

        ordered = OrderedList.make(True, 1, 2, 2, 2, 4, 5)
        self.assertEqual(ordered.most_common(), 2)

        ordered = OrderedList.make(True, 1, 2, 3, 4, 5)
        self.assertEqual(ordered.most_common(), 1)
        self.assertNotEqual(ordered.most_common(), 2)
        self.assertNotEqual(ordered.most_common(), 3)
        self.assertNotEqual(ordered.most_common(), 4)
        self.assertNotEqual(ordered.most_common(), 5)

if __name__ == '__main__':
    unittest.main()
