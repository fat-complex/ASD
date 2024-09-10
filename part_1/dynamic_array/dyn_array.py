import ctypes
from array import array
from itertools import count


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.min_capacity = 16

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if i == self.count:
            self.append(itm)
            return
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for idx in range(self.count, i, -1):
            self.array[idx] = self.array[idx - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for idx in range(i, self.count - 1):
            self.array[idx] = self.array[idx + 1]
        self.count -= 1
        percentage_loading = int(100 * self.count / self.capacity)
        if percentage_loading < 50:
            new_size = int(self.capacity / 1.5)
            if new_size < self.min_capacity:
                self.resize(self.min_capacity)
            else:
                self.resize(new_size)


    def __iter__(self):
        idx = 0
        while idx < self.count:
            yield self.array[idx]
            idx += 1

    @staticmethod
    def make(*args):
        arr: DynArray = DynArray()
        for arg in args:
            arr.append(arg)
        return arr

# 5.3 Complexity: insert: 1) resize: ~O(1) allocating + O(N) copy element from source array to dest
#                         2) shift = (count - i) shifts ~ O(N)
#                         total = O(1) + O(N) + O(N) = O(N)
#
#             delete: 1) shift = (count - i) shifts ~ O(N)
#                     2) resize: ~O(1) allocating + O(N) copy element from source array to dest
#                     3) total = O(1) + O(N) + O(N) = O(N)
