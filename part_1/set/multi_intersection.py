import unittest

from part_1.set.power_set import PowerSet

def set_intersection(sets: [PowerSet]) -> PowerSet:
    if not sets:
        return PowerSet.make([])
    res = sets[0]
    for pset in sets[1:]:
        res = res.intersection(pset)
    return res

class TestMultiIntersection(unittest.TestCase):
    def test_multi_intersection(self):
        target1 = [1, 2, 3]
        target2 = [2, 3, 4]
        target3 = [2, 4, 6]

        ps1 = PowerSet.make(target1)
        ps2 = PowerSet.make(target2)
        ps3 = PowerSet.make(target3)

        s1 = set(target1)
        s2 = set(target2)
        s3 = set(target3)

        actual = set_intersection([ps2, ps1, ps3])
        expected = s1 & s2 & s3

        self.assertEqual(actual.storage, sorted(list(expected)))


if __name__ == '__main__':
    unittest.main()