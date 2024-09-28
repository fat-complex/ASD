import unittest

from part_1.set.power_set import PowerSet

def set_to_sorted_list(s: set) -> []:
    return sorted(list(s))

class TestPutMethod(unittest.TestCase):
    def test_put(self):
        ps = PowerSet.make([])
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(42))

        ps.put(1)
        self.assertEqual(ps.size(), 1)
        self.assertTrue(ps.get(1))
        self.assertFalse(ps.get(42))
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))

        ps.put(2)
        self.assertEqual(ps.size(), 2)
        self.assertTrue(ps.get(1))
        self.assertTrue(ps.get(2))
        self.assertFalse(ps.get(42))
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))

        target = [4, 1, 3, 2, 3, 4, 1]
        ps = PowerSet.make(target)

        expected = sorted(list(set(target)))
        self.assertEqual(ps.storage, expected)
        self.assertTrue(ps.equals(PowerSet.make(expected)))
        self.assertEqual(ps.size(), 4)
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))


class TestRemoveMethod(unittest.TestCase):
    def test_remove(self):
        ps = PowerSet.make([])
        self.assertFalse(ps.remove(42))
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(42))
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))

        ps.put(1)
        self.assertFalse(ps.remove(42))
        self.assertEqual(ps.size(), 1)
        self.assertFalse(ps.get(42))
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))

        self.assertTrue(ps.remove(1))
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.get(1))
        self.assertEqual(ps.storage, set_to_sorted_list(set(ps.storage)))

        target = [1, 2, 3, 4, 5]
        ps = PowerSet.make(target)
        for el in target:
            self.assertTrue(ps.remove(el))
            self.assertFalse(ps.get(el))
        self.assertEqual(ps.size(), 0)
        self.assertEqual(ps.storage, set_to_sorted_list(set([])))


class TestIntersectMethod(unittest.TestCase):
    def test_intersect(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))
        self.assertEqual(ps3.storage, set_to_sorted_list(set([])))


        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make(target)
        ps2 = PowerSet.make([])
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        s1 = set(target)
        s2 = set()
        s3 = s1.intersection(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make(target)
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        s1 = set(target)
        s2 = set()
        s3 = s1.intersection(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target1 = [1, 2, 3, 4, 5]
        target2 = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.intersection(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target1 = [1, 2, 3, 4, 5]
        target2 = [3, 4]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([3, 4])))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.intersection(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target1 = [7, 2, 3, 4, 5, 6, 7, 8]
        target2 = [5, 7, 9, 7]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.intersection(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([5, 7])))
        self.assertEqual(ps3.storage, set_to_sorted_list(set(ps3.storage)))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.intersection(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


class TestUnionMethod(unittest.TestCase):
    def test_union(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        s1 = set([])
        s2 = set([])
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make(target)
        ps2 = PowerSet.make([])
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        s1 = set(target)
        s2 = set([])
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make(target)
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        s1 = set([])
        s2 = set(target)
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target1 = [1, 2, 3, 4, 5]
        target2 = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))

        target1 = [1, 2, 3, 4, 5]
        target2 = [3, 4, 6, 7, 8, 9]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.union(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5, 6, 7, 8, 9])))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


        target1 = [str(i) for i in range(1, 101)]
        target2 = [str(j) for j in range(50, 151)]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)

        ps3 = ps1.union(ps2)

        set1 = set(target1)
        set2 = set(target2)
        s3 = set1.union(set2)

        self.assertTrue(ps3.equals(PowerSet.make(list(s3))))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.union(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))



class TestDifferenceMethod(unittest.TestCase):
    def test_difference(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))


        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make(target)
        ps2 = PowerSet.make([])
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3, 4, 5])))

        s1 = set(target)
        s2 = set([])
        s3 = s1.difference(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))

        target = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make(target)
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([])))

        s1 = set([])
        s2 = set(target)
        s3 = s1.difference(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))

        target1 = [1, 2, 3, 4, 5]
        target2 = [4, 5, 6, 7, 8]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = ps1.difference(ps2)
        self.assertTrue(ps3.equals(PowerSet.make([1, 2, 3])))

        s1 = set(target1)
        s2 = set(target2)
        s3 = s1.difference(s2)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))

        ps3 = ps2.difference(ps1)
        self.assertTrue(ps3.equals(PowerSet.make([6, 7, 8])))

        s3 = s2.difference(s1)
        self.assertEqual(ps3.storage, set_to_sorted_list(s3))


class TestSubsetMethod(unittest.TestCase):
    def test_subset(self):
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make([])
        self.assertTrue(ps1.issubset(ps2))
        self.assertTrue(ps2.issubset(ps1))


        target = [1, 2, 3]
        ps1 = PowerSet.make(target)
        ps2 = PowerSet.make([])
        s1 = set(target)
        s2 = set([])
        self.assertFalse(ps1.issubset(ps2) and s1.issubset(s2))


        target = [1, 2, 3]
        ps1 = PowerSet.make([])
        ps2 = PowerSet.make(target)
        s1 = set([])
        s2 = set(target)
        self.assertTrue(ps1.issubset(ps2) and s1.issubset(s2))


        target1 = [1, 2, 3, 4, 5]
        target2 = [1, 2, 3]
        ps1 = PowerSet.make([1, 2, 3, 4, 5])
        ps2 = PowerSet.make([1, 2, 3])
        s1 = set(target1)
        s2 = set(target2)
        self.assertFalse(ps1.issubset(ps2) and s1.issubset(s2))

        target1 = [1, 2, 3, 4, 5]
        target2 = [1, 3, 5]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        s1 = set(target1)
        s2 = set(target2)
        self.assertTrue(ps2.issubset(ps1) and s2.issubset(s1))

        target1 = [1, 2, 3]
        target2 = [1, 2, 3, 4, 5]
        ps1 = PowerSet.make([1, 2, 3])
        ps2 = PowerSet.make([1, 2, 3, 4, 5])
        s1 = set(target1)
        s2 = set(target2)
        self.assertTrue(ps1.issubset(ps2) and s1.issubset(s2))

        target1 = [1, 2, 3]
        target2 = [1, 2, 3]
        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        s1 = set(target1)
        s2 = set(target2)
        self.assertTrue(ps1.issubset(ps2) and s1.issubset(s2))
        self.assertTrue(ps2.issubset(ps1) and s2.issubset(s1))

        ps1 = PowerSet.make([1, 2, 4])
        ps2 = PowerSet.make([1, 2, 3])
        self.assertFalse(ps1.issubset(ps2))


if __name__ == '__main__':
    unittest.main()
