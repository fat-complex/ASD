class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return self.__hash(value) % self.size

    def seek_slot(self, value):
        idx = self.hash_fun(value)
        if self.slots[idx] is None:
            return idx
        for i in range(idx, self.size, self.step):
            if self.slots[i] is None:
                return i
        return None

    def put(self, value):
        idx: int | None = self.seek_slot(value)
        if idx is not None:
            self.slots[idx] = value
        return idx

    def find(self, value):
        idx = self.hash_fun(value)
        if self.slots[idx] is not None and self.slots[idx] == value:
            return idx
        for i in range(idx, self.size, self.step):
            if self.slots[i] == value:
                return i
        return None

    def __hash(self, s: str) -> int:
        h = 0
        k = 31
        p = 1e9 + 7
        for c in s:
            h = (h * k + ord(c)) % p
        return int(h)
