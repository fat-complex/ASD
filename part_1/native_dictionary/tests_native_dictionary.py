import unittest

from part_1.native_dictionary.native_dictionary import NativeDictionary


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        dt = NativeDictionary(1)

        dt.put("1", 1)
        self.assertEqual(dt.get("1"), 1)
        self.assertTrue(dt.is_key("1"))
        self.assertFalse(dt.is_key("2"))

        dt.put("2", 2)
        self.assertEqual(dt.get("2"), None)
        self.assertTrue(dt.is_key("1"))
        self.assertFalse(dt.is_key("2"))

        dt.put("1", 2)
        self.assertEqual(dt.get("1"), 2)
        self.assertTrue(dt.is_key("1"))
        self.assertFalse(dt.is_key("2"))


        dt = NativeDictionary(17)
        for i in range(dt.size):
            dt.put(str(i), i)
            self.assertEqual(dt.get(str(i)), i)
            self.assertTrue(dt.is_key(str(i)))

        dt.put(str(dt.size + 1), 333)
        self.assertFalse(dt.is_key(str(dt.size + 1)))


if __name__ == '__main__':
    unittest.main()
