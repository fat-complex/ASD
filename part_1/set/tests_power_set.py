import unittest

from part_1.set.power_set import PowerSet


class TestPutMethod(unittest.TestCase):
    def test_put(self):
        ps = PowerSet.make([])
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(42))

        ps.put(1)
        self.assertEqual(ps.size(), 1)
        self.assertTrue(ps.get(1))
        self.assertFalse(ps.get(42))

        ps.put(2)
        self.assertEqual(ps.size(), 2)
        self.assertTrue(ps.get(1))
        self.assertTrue(ps.get(2))
        self.assertFalse(ps.get(42))

        target = [4, 1, 3, 2, 3, 4, 1]
        ps = PowerSet.make(target)

        expected = list(set(target))
        self.assertEqual(ps.storage, expected)
        self.assertEqual(ps.size(), 4)


class TestRemoveMethod(unittest.TestCase):
    def test_remove(self):
        ps = PowerSet.make([])
        self.assertFalse(ps.remove(42))
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(42))

        ps.put(1)
        self.assertFalse(ps.remove(42))
        self.assertEqual(ps.size(), 1)
        self.assertFalse(ps.get(42))

        self.assertTrue(ps.remove(1))
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(1))

        target = [1, 2, 3, 4, 5]
        ps = PowerSet.make(target)
        for el in target:
            self.assertTrue(ps.remove(el))
            self.assertFalse(ps.get(el))
        self.assertEqual(ps.size(), 0)


class TestIntersectMethod(unittest.TestCase):
    def test_intersect(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([3, 4])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([3, 4])))

        ps1 = PowerSet.make([7, 2, 3, 4, 5, 6, 7, 8])
        ps2 = PowerSet.make([5, 7, 9, 7])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([5, 7])))


class TestUnionMethod(unittest.TestCase):
    def test_union(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([3, 4, 6, 7, 8, 9])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5, 6, 7, 8, 9])))


class TestDifferenceMethod(unittest.TestCase):
    def test_difference(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([4, 5, 6, 7, 8])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3])))

        ps3 = ps2.difference(ps1)
        self.assertTrue(ps3.equals(PowerSet.make([6, 7, 8])))


class TestSubsetMethod(unittest.TestCase):
    def test_subset(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        self.assertTrue(ps1.issubset(ps2))

        ps1 = PowerSet.make([1, 2, 3])
        ps2 = PowerSet.make([])
        self.assertFalse(ps1.issubset(ps2))

        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([1, 2, 3])
        self.assertTrue(ps1.issubset(ps2))

        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([1, 2, 3])
        self.assertFalse(ps1.issubset(ps2))

        ps1 = PowerSet.make([1, 2, 3])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        self.assertTrue(ps1.issubset(ps2))

        ps1 = PowerSet.make([1, 2, 3])
        ps2 = PowerSet.make([1, 2, 3])
        self.assertTrue(ps1.issubset(ps2))


if __name__ == '__main__':
    unittest.main()
