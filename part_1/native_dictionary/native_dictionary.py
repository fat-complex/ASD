class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return self.__hash(key) % self.size

    def is_key(self, key):
        idx = self.__find_key(key)
        return True if idx is not None else False

    def put(self, key, value):
        idx: int | None = self.__find_key(key)
        is_inserted = self.__insert(key, value, idx)
        if is_inserted is False:
            idx = self.__find_insert_pace(key, self.slots)
            self.__insert(key, value, idx)


    def get(self, key):
        idx = self.__find_key(key)
        return self.values[idx] if idx is not None else None

    def __hash(self, s: str) -> int:
        h = 0
        k = 31
        p = 1e9 + 7
        for c in s:
            h = (h * k + ord(c)) % p
        return int(h)

    def __find_key(self, value):
        idx = self.hash_fun(value)
        if self.slots[idx] is not None and self.slots[idx] == value:
            return idx
        for i in range(idx, self.size):
            if self.slots[i] == value:
                return i
        return None

    def __find_insert_pace(self, value: str, table: []):
        idx = self.hash_fun(value)
        if table[idx] is None:
            return idx
        for i in range(idx, self.size):
            if table[i] is None:
                return i
        return None

    def __insert(self, key, value, idx) -> bool:
        if idx is None:
            return False
        self.slots[idx] = key
        self.values[idx] = value
        return True