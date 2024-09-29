from __future__ import annotations

import unittest
from typing import Any
from part_1.set.multi_set import Bag

def to_dict(lst: [])-> {Any, int}:
    res: {Any, int} = {}
    for el in lst:
        if res.get(el):
            res[el] += 1
        else:
            res[el] = 1
    return res

class TestPutMethod(unittest.TestCase):
    def test_put(self):
        target = [2, 2, 2, 2, 2]
        mset = Bag.make(target)
        self.assertEqual(mset.size(), 5)
        self.assertEqual(mset.storage, sorted(target))


        target = [1, 2, 3, 2, 4, 2]
        mset = Bag.make(target)
        self.assertEqual(mset.size(), 6)
        self.assertEqual(mset.storage, sorted(target))


class TestRemoveMethod(unittest.TestCase):
    def test_remove(self):
        target = [2, 2, 2, 2, 2]
        mset = Bag.make(target)

        mset.remove(2)
        self.assertEqual(mset.size(), 4)
        print(mset.storage)

        for el in target:
            mset.remove(el)
        self.assertEqual(mset.size(), 0)


class TestGetFrequenciesMethod(unittest.TestCase):
    def test_get_frequencies(self):
        target = [2, 2, 2, 2, 2]
        mset = Bag.make(target)
        self.assertEqual(mset.size(), 5)
        self.assertEqual(mset.get_frequencies(), to_dict(target))

        mset.remove(2)
        self.assertEqual(mset.size(), 4)
        self.assertEqual(mset.get_frequencies(), to_dict(mset.storage))


        target = [1, 2, 3, 2, 4, 2]
        mset = Bag.make(target)
        self.assertEqual(mset.size(), 6)
        self.assertEqual(mset.storage, sorted(target))


if __name__ == '__main__':
    unittest.main()
