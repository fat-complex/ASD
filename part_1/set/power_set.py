from __future__ import annotations
from typing import Any

class PowerSet:
    def __init__(self) -> None:
        self.storage = []

    def size(self) -> int:
        return len(self.storage)

    def put(self, value: Any) -> None:
        insert_place_idx = self.lower_bound(0, self.size(), value)
        if not self.__exists_value(insert_place_idx, value):
            self.storage.insert(insert_place_idx, value)

    def get(self, value: Any) -> bool:
        maybe_found_idx = self.lower_bound(0, self.size(), value)
        return self.__exists_value(maybe_found_idx, value)

    def remove(self, value: Any) -> bool:
        maybe_found_idx = self.lower_bound(0, self.size(), value)
        if self.__exists_value(maybe_found_idx, value):
            self.storage.pop(maybe_found_idx)
            return True
        return False

    def intersection(self, set2: PowerSet) -> PowerSet:
        idx_1 = 0
        idx_2 = 0
        intersect = PowerSet()
        while idx_1 != self.size() and idx_2 != set2.size():
            if self.storage[idx_1] < set2.storage[idx_2]:
                idx_1 += 1
            else:
                if not set2.storage[idx_2] < self.storage[idx_1]:
                    intersect.put(self.storage[idx_1])
                    idx_1 += 1
                idx_2 += 1
        return intersect

    def union(self, set2: PowerSet) -> PowerSet:
        idx_1 = 0
        idx_2 = 0
        set_union = PowerSet.make([])
        while idx_1 != self.size():
            if idx_2 == set2.size():
                self.__copy(self, idx_1, self.size(), set_union)
                break
            if set2.storage[idx_2] < self.storage[idx_1]:
                set_union.put(set2.storage[idx_2])
                idx_2 += 1
            else:
                set_union.put(self.storage[idx_1])
                if not self.storage[idx_1] < set2.storage[idx_2]:
                    idx_2 += 1
                idx_1 += 1
        self.__copy(set2, idx_2, set2.size(), set_union)
        return set_union

    def difference(self, set2: PowerSet) -> PowerSet:
        idx_1 = 0
        idx_2 = 0
        set_difference = PowerSet.make([])
        while idx_1 != self.size():
            if idx_2 == set2.size():
                self.__copy(self, idx_1, self.size(), set_difference)
                break
            if self.storage[idx_1] < set2.storage[idx_2]:
                set_difference.put(self.storage[idx_1])
                idx_1 += 1
            else:
                if not set2.storage[idx_2] < self.storage[idx_1]:
                    idx_1 += 1
                idx_2 += 1
        return set_difference

    def issubset(self, set2: PowerSet) -> bool:
        return all(i in self.storage for i in set2.storage)

    def equals(self, set2: PowerSet) -> bool:
        return self.storage == set2.storage

    def cartesian_product(self, *args):
        cartesian = PowerSet.make([])
        res = []
        self.__cartesian_product(res, [], self.storage, *args)
        for cart in res:
            cartesian.put(tuple(cart))
        return cartesian

    def lower_bound(self, first, last, value):
        distance = last - first
        start = 0
        while distance > 0:
            idx = start
            step = distance // 2
            idx += step
            if self.storage[idx] < value:
                start = (idx + 1)
                distance -= (step + 1)
            else:
                distance = step
        return start

    def __iter__(self):
        return iter(self.storage)

    def __cartesian_product(self, acc: [], lst: [], *args):
        if len(args) == 0:
            acc.append([i for i in lst])
            return
        for el in args[0]:
            lst.append(el)
            self.__cartesian_product(acc, lst, *args[1:])
            lst.pop()

    def __exists_value(self, idx: int, value):
        return idx != self.size() and self.storage[idx] == value

    def __copy(self, source, first: int, last: int, dest):
        while first != last:
            dest.put(source.storage[first])
            first += 1

    @staticmethod
    def make(source_list: []):
        ps = PowerSet()
        for el in source_list:
            ps.put(el)
        return ps



