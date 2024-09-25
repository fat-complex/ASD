import unittest

import unittest

from part_1.native_dictionary.dict_with_ordered_list import OrderedListDict


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        dt = OrderedListDict()

        dt.put("1", 1)
        self.assertEqual(dt.get("1"), 1)
        self.assertTrue(dt.is_key("1"))
        self.assertFalse(dt.is_key("2"))

        dt.put("2", 2)
        self.assertEqual(dt.get("2"), 2)
        self.assertTrue(dt.is_key("1"))
        self.assertTrue(dt.is_key("2"))

        dt.put("1", 2)
        self.assertEqual(dt.get("1"), 2)
        self.assertNotEqual(dt.get("1"), 1)
        self.assertTrue(dt.is_key("1"))


        dt = OrderedListDict()
        for i in range(17):
            dt.put(str(i), i)
            self.assertEqual(dt.get(str(i)), i)
            self.assertTrue(dt.is_key(str(i)))

        self.assertEqual(dt.get("sdfdfg"), None)

class TestRemoveMethod(unittest.TestCase):
    def test_remove(self):
        dt = OrderedListDict()
        for i in range(5):
            dt.put(str(i), i)


        dt.remove("1")
        self.assertFalse(dt.is_key("1"))
        self.assertEqual(dt.get("1"), None)

        for i in range(len(dt) + 1):
            dt.remove(str(i))
            self.assertFalse(dt.is_key("1"))
            self.assertEqual(dt.get("1"), None)
        self.assertEqual(len(dt), 0)

if __name__ == '__main__':
    unittest.main()
