from part_1.queue.queue import Queue


def shift(target: Queue, shifts: int) -> Queue:
    while shifts != 0:
        d_val = target.dequeue()
        target.enqueue(d_val)
        shifts -= 1
    return target


import unittest

class TestShiftFunction(unittest.TestCase):
    def test_shift_1(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, 1)
        self.assertEqual(queue.front(), 2)
        self.assertEqual(queue.back(), 1)
        self.assertEqual(queue.size(), 5)

    def test_shift_2(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, 2)
        self.assertEqual(queue.front(), 3)
        self.assertEqual(queue.back(), 2)
        self.assertEqual(queue.size(), 5)

    def test_shift_3(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, 3)
        self.assertEqual(queue.front(), 4)
        self.assertEqual(queue.back(), 3)
        self.assertEqual(queue.size(), 5)

    def test_shift_4(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, 4)
        self.assertEqual(queue.front(), 5)
        self.assertEqual(queue.back(), 4)
        self.assertEqual(queue.size(), 5)

    def test_shift_5(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, 5)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.back(), 5)
        self.assertEqual(queue.size(), 5)

    def test_shift_size_plus_n(self):
        queue = Queue()
        for val in range(1, 6):
            queue.enqueue(val)
        queue = shift(queue, queue.size() + 2)
        self.assertEqual(queue.front(), 3)
        self.assertEqual(queue.back(), 2)
        self.assertEqual(queue.size(), 5)


if __name__ == '__main__':
    unittest.main()
