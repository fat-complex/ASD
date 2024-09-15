import unittest
from queue import *

class TestEnqueueMethod(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(1)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.back(), 1)
        self.assertEqual(queue.size(), 1)

        queue.enqueue(2)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.back(), 2)
        self.assertEqual(queue.size(), 2)

        for val in range(3, 6):
            queue.enqueue(val)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.back(), 5)
        self.assertEqual(queue.size(), 5)


class TestDequeueMethod(unittest.TestCase):
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.front(), None)
        self.assertEqual(queue.back(), None)
        self.assertEqual(queue.size(), 0)

        for val in range(2, 6):
            queue.enqueue(val)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.front(), 3)
        self.assertEqual(queue.back(), 5)
        self.assertEqual(queue.size(), 3)

        while queue.size() > 0:
            queue.dequeue()

        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.front(), None)
        self.assertEqual(queue.back(), None)
        self.assertEqual(queue.size(), 0)

if __name__ == '__main__':
    unittest.main()
