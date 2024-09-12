import unittest
from dyn_array_bank_method import *

class TestInsertMethod(unittest.TestCase):
    def test_insert(self):
        arr1 = DynArrayBanked.make()
        old_capacity = arr1.capacity
        arr1.insert(0, 1)
        self.assertEqual(list(arr1), [1])
        self.assertEqual(len(arr1), 1)
        self.assertEqual(arr1.capacity, old_capacity)

        arr2 = DynArrayBanked.make(1)
        old_capacity = arr2.capacity
        arr2.insert(0, 2)
        self.assertEqual(list(arr2), [2, 1])
        self.assertEqual(len(arr2), 2)
        self.assertEqual(arr2.capacity, old_capacity)

        arr3 = DynArrayBanked.make(1)
        old_capacity = arr3.capacity
        arr3.insert(len(arr3), 2)
        self.assertEqual(list(arr3), [1, 2])
        self.assertEqual(len(arr3), 2)
        self.assertEqual(arr3.capacity, old_capacity)

        arr4 = DynArrayBanked.make(1, 2, 4, 5, 6)
        old_capacity = arr4.capacity
        arr4.insert(2, 3)
        self.assertEqual(list(arr4), [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(arr4), 6)
        self.assertEqual(arr4.capacity, old_capacity)

        arr5 = DynArrayBanked.make(1, 2, 3, 4, 5)
        old_capacity = arr5.capacity
        arr5.insert(len(arr5), 6)
        self.assertEqual(list(arr5), [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(arr5), 6)
        self.assertEqual(arr5.capacity, old_capacity)

        arr6 = DynArrayBanked.make()
        old_capacity = arr6.capacity
        for val in range(1, old_capacity + 1):
            arr6.append(val)
        self.assertEqual(list(arr6), [val for val in range(1, old_capacity + 1)])
        self.assertEqual(len(arr6), 16)

        for val in range(1, old_capacity + 1):
            arr6.insert(len(arr6), val)
        expected = [val for val in range(1, old_capacity + 1)] + [val for val in range(1, old_capacity + 1)]
        self.assertEqual(list(arr6), expected)
        self.assertEqual(len(arr6), 32)
        self.assertTrue(arr6.capacity > old_capacity)

        arr7 = DynArrayBanked.make(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            arr7.insert(-1, 2)
        with self.assertRaises(IndexError):
            arr7.insert(len(arr7) + 1, 2)


class TestDeleteMethod(unittest.TestCase):
    def test_delete(self):
        arr1 = DynArrayBanked.make()
        with self.assertRaises(IndexError):
            arr1.delete(0)
            arr1.delete(2)
            arr1.delete(-1)

        arr2 = DynArrayBanked.make(1)
        arr2.delete(0)
        self.assertEqual(list(arr2), [])
        self.assertEqual(len(arr2), 0)

        arr3 = DynArrayBanked.make(1, 2)
        arr3.delete(0)
        self.assertEqual(list(arr3), [2])
        self.assertEqual(len(arr3), 1)

        arr4 = DynArrayBanked.make(1, 2)
        arr4.delete(1)
        self.assertEqual(list(arr4), [1])
        self.assertEqual(len(arr4), 1)

        arr5 = DynArrayBanked.make(1, 2, 3, 4, 5)
        arr5.delete(2)
        self.assertEqual(list(arr5), [1, 2, 4, 5])
        self.assertEqual(len(arr5), 4)

        arr6 = DynArrayBanked.make(1, 2, 3, 4, 5)
        arr6.delete(2)
        self.assertEqual(list(arr6), [1, 2, 4, 5])
        self.assertEqual(len(arr6), 4)

if __name__ == '__main__':
    unittest.main()
