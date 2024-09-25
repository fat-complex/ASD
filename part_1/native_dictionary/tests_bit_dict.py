import unittest

from part_1.native_dictionary.bit_dict import FixedBitsDict


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        dt = FixedBitsDict(32)
        dt.put(1, "A")
        self.assertEqual(dt.get(1), "A")
        self.assertTrue(dt.is_key(1))
        self.assertFalse(dt.is_key(2))
        self.assertEqual(dt.get(2), None)

        dt = FixedBitsDict(32)
        for i in range(1, 31):
            dt.put(i, "A" + str(i))
            self.assertEqual(dt.get(i), "A" + str(i))
            self.assertTrue(dt.is_key(i))


class TestRemoveMethod(unittest.TestCase):
    def test_remove(self):
        dt = FixedBitsDict(32)

        dt.put(1, "A")
        dt.remove(1)
        self.assertNotEqual(dt.get(1), "A")
        self.assertFalse(dt.is_key(1))

        dt = FixedBitsDict(32)
        for i in range(1, 31):
            dt.put(i, "A" + str(i))

        for i in range(1, 31):
            dt.remove(i)
            self.assertFalse(dt.is_key(i))
            self.assertEqual(dt.get(i), None)
        self.assertTrue(dt.empty())


if __name__ == '__main__':
    unittest.main()
