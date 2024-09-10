import unittest
from dyn_array import *

class TestInsertMethod(unittest.TestCase):
    def test_insert(self):
        arr1 = DynArray.make()
        old_capacity = arr1.capacity
        arr1.insert(0, 1)
        self.assertEqual(list(arr1), [1])
        self.assertEqual(len(arr1), 1)
        self.assertEqual(arr1.capacity, old_capacity)

        arr2 = DynArray.make(1)
        old_capacity = arr2.capacity
        arr2.insert(0, 2)
        self.assertEqual(list(arr2), [2, 1])
        self.assertEqual(len(arr2), 2)
        self.assertEqual(arr2.capacity, old_capacity)

        arr3 = DynArray.make(1)
        old_capacity = arr3.capacity
        arr3.insert(len(arr3), 2)
        self.assertEqual(list(arr3), [1, 2])
        self.assertEqual(len(arr3), 2)
        self.assertEqual(arr3.capacity, old_capacity)

        arr4 = DynArray.make(1, 2, 4, 5, 6)
        old_capacity = arr4.capacity
        arr4.insert(2, 3)
        self.assertEqual(list(arr4), [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(arr4), 6)
        self.assertEqual(arr4.capacity, old_capacity)

        arr5 = DynArray.make(1, 2, 3, 4, 5)
        old_capacity = arr5.capacity
        arr5.insert(len(arr5), 6)
        self.assertEqual(list(arr5), [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(arr5), 6)
        self.assertEqual(arr5.capacity, old_capacity)

        arr6 = DynArray.make()
        old_capacity =  arr6.capacity
        for val in range(1, old_capacity + 1):
            arr6.append(val)
        self.assertEqual(list(arr6), [val for val in range(1, old_capacity + 1)])
        self.assertEqual(len(arr6), 16)
        self.assertEqual(arr6.capacity, old_capacity)

        arr6.insert(len(arr6), 17)
        expected = [val for val in range(1, old_capacity + 1)] + [17]
        self.assertEqual(list(arr6), expected)
        self.assertEqual(len(arr6), 17)
        self.assertTrue(arr6.capacity > old_capacity)

        arr7 = DynArray.make(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            arr7.insert(-1, 2)
        with self.assertRaises(IndexError):
            arr7.insert(len(arr7) + 1, 2)


class TestDeleteMethod(unittest.TestCase):
    def test_delete(self):
        arr1 = DynArray.make()
        with self.assertRaises(IndexError):
            arr1.delete(0)
            arr1.delete(2)
            arr1.delete(-1)

        arr2 = DynArray.make(1)
        old_capacity = arr2.capacity
        arr2.delete(0)
        self.assertEqual(list(arr2), [])
        self.assertEqual(len(arr2), 0)
        self.assertEqual(arr2.capacity, old_capacity)
        self.assertEqual(arr2.min_capacity, old_capacity)

        arr3 = DynArray.make(1, 2)
        old_capacity = arr3.capacity
        arr3.delete(0)
        self.assertEqual(list(arr3), [2])
        self.assertEqual(len(arr3), 1)
        self.assertEqual(arr3.min_capacity, old_capacity)

        arr4 = DynArray.make(1, 2)
        old_capacity = arr4.capacity
        arr4.delete(1)
        self.assertEqual(list(arr4), [1])
        self.assertEqual(len(arr4), 1)
        self.assertEqual(arr4.capacity, old_capacity)
        self.assertEqual(arr4.min_capacity, old_capacity)

        arr5 = DynArray.make(1, 2, 3, 4, 5)
        old_capacity = arr5.capacity
        arr5.delete(2)
        self.assertEqual(list(arr5), [1, 2, 4, 5])
        self.assertEqual(len(arr5), 4)
        self.assertEqual(arr5.capacity, old_capacity)
        self.assertEqual(arr5.min_capacity, old_capacity)

        arr6 = DynArray.make(1, 2, 3, 4, 5)
        old_capacity = arr6.capacity
        arr6.delete(2)
        self.assertEqual(list(arr6), [1, 2, 4, 5])
        self.assertEqual(len(arr6), 4)
        self.assertTrue(arr6.capacity == old_capacity == 16)
        self.assertEqual(arr6.min_capacity, old_capacity)

        arr7 = DynArray.make(*[val for val in range(1, arr4.capacity // 2 + 1)])
        old_capacity = arr7.capacity
        arr7.delete(len(arr7) - 1)
        self.assertEqual(list(arr7), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(len(arr7), 7)
        self.assertTrue(arr7.capacity == old_capacity == 16)
        self.assertEqual(arr7.min_capacity, old_capacity)

        arr8 = DynArray.make(*[val for val in range(1, arr4.capacity * 4 + 1)])
        old_capacity = arr8.capacity
        for idx in range(len(arr8) // 2):
            arr8.delete(len(arr8) - 1)
        self.assertEqual(list(arr8), [val for val in range(1, len(arr8) + 1)])
        self.assertEqual(len(arr8), 32)
        self.assertTrue(arr8.capacity == old_capacity == 64)
        self.assertNotEqual(arr8.min_capacity, old_capacity)

        arr8.delete(len(arr8) - 1)
        self.assertEqual(len(arr8), 31)
        self.assertTrue(arr8.capacity < old_capacity)
        self.assertNotEqual(arr8.min_capacity, arr8.capacity)



if __name__ == '__main__':
    unittest.main()
