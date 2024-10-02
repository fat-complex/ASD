import unittest

from part_1.caching.native_cache import NativeCache


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        target = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        dt = NativeCache.make(target)

        for key in target:
            self.assertTrue(dt.get(key) is not None)
        self.assertTrue(dt.full())

        dt.get("a")
        dt.get("a")
        dt.get("a")

        dt.get("c")
        dt.get("c")

        dt.get("d")
        dt.get("d")
        dt.get("e")

        # displace element b
        dt.put("f", 6)
        print(dt.slots)
        print(dt.values)
        print(dt.hits)

        self.assertTrue(dt.get("b") is None)







if __name__ == '__main__':
    unittest.main()
