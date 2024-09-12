import ctypes
import math


class DynArrayBanked:

    def __init__(self):
        self.count = 0
        self.min_capacity = 16
        self.capacity = self.min_capacity
        self.array = self.make_array(self.capacity)
        self.copy_coast = 3
        self.insert_coast = 3
        self.remove_coast = -2
        self.resize_coast = self.capacity
        self.bank_coins  = 0

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self):
        new_capacity = int(math.pow(self.bank_coins, 2))
        self.capacity = new_capacity if self.capacity < new_capacity else self.capacity
        self.bank_coins -= math.log(self.capacity, 2)

        new_array = self.make_array(self.capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
            self.bank_coins -= self.copy_coast
        self.array = new_array

    def append(self, itm):
        self.insert(len(self), itm)

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        self.bank_coins += self.insert_coast
        if self.count >= self.capacity:
            self.resize()
        for idx in range(self.count, i, -1):
            self.array[idx] = self.array[idx - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        self.bank_coins -= self.remove_coast
        for idx in range(i, self.count - 1):
            self.array[idx] = self.array[idx + 1]
        self.count -= 1
        percentage_loading = int(100 * self.count / self.capacity)
        if percentage_loading < 50:
            self.resize()


    def __iter__(self):
        idx = 0
        while idx < self.count:
            yield self.array[idx]
            idx += 1

    @staticmethod
    def make(*args):
        arr: DynArrayBanked = DynArrayBanked()
        for arg in args:
            arr.append(arg)
        return arr
