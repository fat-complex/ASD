import unittest

from part_1.hashing.doubly_hashing import DoubleHashTable


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        table = DoubleHashTable(2)

        idx = table.put("1")
        self.assertNotEqual(idx, None)

        idx = table.put("2")
        self.assertNotEqual(idx, None)


        table = DoubleHashTable(17)
        for i in range(table.capacity):
            idx = table.put(str(i))
            self.assertTrue(idx is not None)
        self.assertEqual(table.put(str(table.capacity + 1)), None)


class TestFindMethod(unittest.TestCase):
    def test_find(self):
        table = DoubleHashTable(2)
        self.assertEqual(table.find("1"), None)

        idx = table.put("1")
        self.assertEqual(table.find("1"), idx)

        table = DoubleHashTable(19)
        for i in range(table.size):
            idx = table.put(str(i))
            self.assertEqual(table.find(str(i)), idx)

        self.assertEqual(table.find(str(table.size + 1)), None)


if __name__ == '__main__':
    unittest.main()
