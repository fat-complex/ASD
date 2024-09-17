import unittest

from part_1.deque.deque import Deque, DequeWithMinSupport


class TestAddFrontMethod(unittest.TestCase):
    def test_add_front(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)

        deque.addFront(2)
        self.assertEqual(deque.top_value(), deque.back_value())
        self.assertEqual(deque.top_value(), 2)
        self.assertEqual(deque.back_value(), 2)
        self.assertEqual(deque.size(), 1)

        deque.addFront(3)
        self.assertEqual(deque.top_value(), 3)
        self.assertEqual(deque.back_value(), 2)
        self.assertEqual(deque.size(), 2)


class TestAddTailMethod(unittest.TestCase):
    def test_add_tail(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)

        deque.addTail(2)
        self.assertEqual(deque.top_value(), deque.back_value())
        self.assertEqual(deque.top_value(), 2)
        self.assertEqual(deque.back_value(), 2)
        self.assertEqual(deque.size(), 1)

        deque.addTail(3)
        self.assertEqual(deque.top_value(), 2)
        self.assertEqual(deque.back_value(), 3)
        self.assertEqual(deque.size(), 2)


class TestAddFrontAndTailMethod(unittest.TestCase):
    def test_add_front_tail(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)

        deque.addFront(2)
        self.assertEqual(deque.top_value(), deque.back_value())
        self.assertEqual(deque.top_value(), 2)
        self.assertEqual(deque.back_value(), 2)
        self.assertEqual(deque.size(), 1)

        deque.addTail(3)
        self.assertEqual(deque.top_value(), 2)
        self.assertEqual(deque.back_value(), 3)
        self.assertEqual(deque.size(), 2)

        deque.addFront(1)
        deque.addTail(4)
        self.assertEqual(deque.top_value(), 1)
        self.assertEqual(deque.back_value(), 4)
        self.assertEqual(deque.size(), 4)


class TestRemoveFrontlMethod(unittest.TestCase):
    def test_remove_front(self):
        deque = Deque()
        self.assertEqual(deque.removeFront(), None)

        deque.addTail(1)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.top_value(), None)
        self.assertEqual(deque.size(), 0)

        for val in range(1, 6):
            deque.addTail(val)
        self.assertEqual(deque.top_value(), 1)
        self.assertEqual(deque.back_value(), 5)
        self.assertEqual(deque.size(), 5)

        while not deque.is_empty():
            deque.removeFront()
        self.assertEqual(deque.top_value(), None)
        self.assertEqual(deque.back_value(), None)
        self.assertEqual(deque.size(), 0)


class TestRemoveTailMethod(unittest.TestCase):
    def test_remove_tail(self):
        deque = Deque()
        self.assertEqual(deque.removeTail(), None)

        deque.addTail(1)
        self.assertEqual(deque.removeTail(), 1)
        self.assertEqual(deque.back_value(), None)
        self.assertEqual(deque.size(), 0)

        for val in range(1, 6):
            deque.addTail(val)
        self.assertEqual(deque.top_value(), 1)
        self.assertEqual(deque.back_value(), 5)
        self.assertEqual(deque.size(), 5)

        while not deque.is_empty():
            deque.removeTail()
        self.assertEqual(deque.top_value(), None)
        self.assertEqual(deque.back_value(), None)
        self.assertEqual(deque.size(), 0)


class TestGetMinMethod(unittest.TestCase):
    def test_get_min(self):
        deque = DequeWithMinSupport()

        for val in range(5, 10):
            deque.addTail(val)
        self.assertEqual(deque.get_min(), 5)

        deque.addTail(2)
        self.assertEqual(deque.get_min(), 2)

        while not deque.is_empty():
            deque.removeFront()
        self.assertEqual(deque.top_value(), None)



if __name__ == '__main__':
    unittest.main()
