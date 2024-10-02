from select import select
from typing import Any


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def put(self, key, value):
        if self.full():
            to_remove_key_idx = self.hits.index(min(self.hits))
            self.__remove_by_idx(to_remove_key_idx)
        idx: int | None = self.__find_key(key)
        is_inserted: bool = self.__insert(key, value, idx)
        if is_inserted is False:
            idx = self.__find_insert_place(key, self.slots)
            self.__insert(key, value, idx)


    def get(self, key: str):
        idx = self.__find_key(key)
        if idx is not None:
            self.hits[idx] += 1
            return self.values[idx]
        return  None

    def full(self) -> bool:
        return self.slots.count(None) == 0

    def __remove_by_idx(self, idx: int) -> bool:
        if idx < 0 or idx >= self.size:
            return False
        self.slots[idx] = None
        self.values[idx] = None
        self.hits[idx] = 0
        return True

    def __find_key(self, key: str) ->  None | int:
        idx = NativeCache.hash(key) % self.size
        if self.slots[idx] is not None and self.slots[idx] == key:
            return idx
        for i in range(self.size):
            if self.slots[i] == key:
                return i
        return None

    def __find_insert_place(self, key: str, table: []):
        idx = self.hash(key) % self.size
        if table[idx] is None:
            return idx
        for i in range(self.size):
            if table[i] is None:
                return i
        return None

    def __insert(self, key, value, idx) -> bool:
        if idx is None:
            return False
        self.slots[idx] = key
        self.values[idx] = value
        return True


    @staticmethod
    def hash(s: str) -> int:
        h = 0
        k = 31
        p = 1e9 + 7
        for c in s:
            h = (h * k + ord(c)) % p
        return int(h)

    @staticmethod
    def make(entries: {str: Any}):
        dt = NativeCache(len(entries))
        for key, val in entries.items():
            dt.put(key, val)
        return dt