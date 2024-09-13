import unittest

from stack_via_list import StackList

class TestInsertMethod(unittest.TestCase):
    def test_push(self):
        stack = StackList()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 1)

        stack.push(2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)

        for i in range(3, 5 + 1):
            stack.push(i)
        self.assertEqual(stack.size(), 5)
        self.assertEqual(stack.peek(), 5)

class TestPopMethod(unittest.TestCase):
    def test_pop(self):
        stack = StackList()
        top = stack.pop()
        self.assertEqual(top, None)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.peek(), None)

        stack.push(1)
        top = stack.pop()
        self.assertEqual(top, 1)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.peek(), None)

        for i in range (1, 5 + 1):
            stack.push(i)
        top = stack.pop()
        self.assertEqual(top, 5)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 4)

        while stack.size() != 0:
            stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.peek(), None)


class TestGetMinMethod(unittest.TestCase):
    def test_get_min_value(self):
        stack = StackList()

        min_val = stack.get_min_value()
        self.assertEqual(min_val, None)

        stack.push(1)
        min_val = stack.get_min_value()
        self.assertEqual(min_val, 1)

        for val in range(2, 6):
            stack.push(val)
        min_val = stack.get_min_value()
        self.assertEqual(min_val, 1)
        self.assertEqual(stack.peek(), 5)

        stack.pop()
        min_val = stack.get_min_value()
        self.assertEqual(min_val, 1)
        self.assertEqual(stack.peek(), 4)


class TestGetAverageMethod(unittest.TestCase):
    def test_get_average(self):
        stack = StackList()
        self.assertEqual(stack.get_average(), None)

        for val in range(1, 6):
            stack.push(val)
        self.assertEqual(stack.get_average(), 3)

        stack.pop()
        self.assertEqual(stack.get_average(), 2)

if __name__ == '__main__':
    unittest.main()