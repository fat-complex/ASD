import unittest
from itertools import permutations

from part_1.hashing.dynamic_hash_table import DynamicHashTable

class TestHashFunMethod(unittest.TestCase):
    def test_hash_fun(self):
        table = DynamicHashTable(17, 1)

        key = "abcd"
        self.assertEqual(table.hash_fun(key), table.hash_fun(key))
        self.assertNotEqual(table.hash_fun(key), table.hash_fun(key[::-1]))

        key = key + "efgh"
        self.assertEqual(table.hash_fun(key), table.hash_fun(key))

        for l in [''.join(p) for p in permutations(key)]:
            self.assertEqual(table.hash_fun(key), table.hash_fun(key))


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        table = DynamicHashTable(1, 1)

        idx = table.put("1")
        self.assertEqual(table.hash_fun("1"), idx)
        self.assertEqual(table.seek_slot("1"), None)

        idx = table.put("2")
        self.assertNotEqual(idx, None)

        idx = table.put("2")
        print(table.slots)
        self.assertEqual(idx, None)

        old_size = table.size
        table = DynamicHashTable(17, 1)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertTrue(idx is not None)
        self.assertTrue(table.size > old_size)
        self.assertNotEqual(table.put(str(table.size + 1)), None)

        table = DynamicHashTable(17, 2)
        old_size = table.size
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertNotEqual(idx, None)
        self.assertTrue(table.size > old_size)
        self.assertNotEqual(table.put(str(table.size + 1)), None)


class TestFindMethod(unittest.TestCase):
    def test_find(self):
        table = DynamicHashTable(17, 1)
        self.assertEqual(table.find("1"), None)

        idx = table.put("1")
        self.assertEqual(table.find("1"), idx)

        table = DynamicHashTable(17, 1)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertEqual(table.find(str(i)), idx)

        self.assertEqual(table.find(str(table.size + 1)), None)


if __name__ == '__main__':
    unittest.main()
