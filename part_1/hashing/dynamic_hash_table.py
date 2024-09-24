from part_1.hashing.hash_table import HashTable


class DynamicHashTable(HashTable):
    def __init__(self, sz, stp):
        super().__init__(sz, stp)
        self.load_factor = 0.75
        self.count = 0

    def put(self, value):
        if self.find(value) is not None:
            return None
        if self.__limit_has_been_reached():
            self.__reallocate()
        idx = super().put(value)
        self.count += 1
        return idx

    def __limit_has_been_reached(self):
        return self.count / self.size > self.load_factor
    
    def __reallocate(self):
        new_size = self.size * 2
        new_storage = [None] * new_size
        for val in self.slots:
            if val is not None:
                idx = self.find_insert_pace(val, new_storage)
                new_storage[idx] = val
        self.size = new_size
        self.slots = new_storage
