import zlib

class DoubleHashTable:
    def __init__(self, capacity):
        self.capacity: int = capacity
        self.slots = [None] * self.capacity
        self.some_prime: int = 31
        self.size = 0

    def put(self, value: str) -> int | None:
        if self.__is_full():
            return None
        return self.__insert(value)


    def find(self, value: str) -> int | None:
        idx, step = self.__get_start_end_offset_for(value)
        while self.slots[idx] is not None:
            if self.slots[idx] == value:
                return idx
            idx += step
            idx %= self.capacity
        return None

    def __hash1(self, s: str) -> int:
        h = 0
        k = 31
        p = 1e9 + 7
        for c in s:
            h = (h * k + ord(c)) % p
        return int(h) % self.capacity

    def __hash2(self, s: str) -> int:
        h = (zlib.crc32(s.encode()) * self.some_prime) % (self.capacity - 1)
        if h % 2 == 0:
            h += 1
        return int(h)

    def __is_full(self):
        return self.size == self.capacity

    def __insert(self, value):
        idx, step = self.__get_start_end_offset_for(value)
        while self.slots[idx] is not None:
            if self.slots[idx] == value:
                return idx
            idx += step
            idx %= self.capacity
        self.slots[idx] = value
        self.size += 1
        return idx

    def __get_start_end_offset_for(self, value: str) -> (int, int):
        idx: int = self.__hash1(value)
        step = self.__hash2(value)
        return idx, step



