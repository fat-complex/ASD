from __future__ import annotations
from typing import Any

from part_1.set.power_set import PowerSet


class Bag(PowerSet):
    def __init__(self):
        super().__init__()

    def put(self, value: Any) -> None:
        insert_place_idx = self.lower_bound(0, self.size(), value)
        self.storage.insert(insert_place_idx, value)

    def get_frequencies(self) -> [{Any: int}]:
        cursor = 0
        res: {Any: int} = {}
        while cursor != self.size():
            key = self.storage[cursor]
            start, end = self.equal_range(key)
            res[key] = end - start
            cursor = end
        return res

    def equal_range(self, value) -> (int, int):
        start = self.lower_bound(0, self.size(), value)
        end = self.lower_bound(0, self.size(), value + 1)
        return start, end

    @staticmethod
    def make(source_list: []) -> Bag:
        mset = Bag()
        for el in source_list:
            mset.put(el)
        return mset