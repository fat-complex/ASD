import unittest
from itertools import permutations

from part_1.hashing.hash_table import HashTable

class TestHashFunMethod(unittest.TestCase):
    def test_hash_fun(self):
        table = HashTable(17, 1)

        key = "abcd"
        self.assertEqual(table.hash_fun(key), table.hash_fun(key))
        self.assertNotEqual(table.hash_fun(key), table.hash_fun(key[::-1]))

        key = key + "efgh"
        self.assertEqual(table.hash_fun(key), table.hash_fun(key))

        for l in [''.join(p) for p in permutations(key)]:
            self.assertEqual(table.hash_fun(key), table.hash_fun(key))


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        table = HashTable(1, 1)

        idx = table.put("1")
        self.assertEqual(table.hash_fun("1"), idx)
        self.assertEqual(table.seek_slot("1"), None)

        idx = table.put("2")
        self.assertEqual(idx, None)
        self.assertEqual(table.seek_slot("1"), None)


        table = HashTable(17, 1)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertTrue(idx is not None)
        self.assertEqual(table.put(str(table.size + 1)), None)

        table = HashTable(17, 2)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertNotEqual(idx, None)

        self.assertEqual(table.put(str(table.size + 1)), None)


class TestFindMethod(unittest.TestCase):
    def test_find(self):
        table = HashTable(17, 1)
        self.assertEqual(table.find("1"), None)

        idx = table.put("1")
        self.assertEqual(table.find("1"), idx)

        table = HashTable(17, 1)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertEqual(table.find(str(i)), idx)

        self.assertEqual(table.find(str(table.size + 1)), None)


if __name__ == '__main__':
    unittest.main()
