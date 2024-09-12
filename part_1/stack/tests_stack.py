import unittest
from stack import Stack

class TestInsertMethod(unittest.TestCase):
    def test_push(self):
        stack = Stack()
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

    def test_pop(self):
        stack = Stack()
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


if __name__ == '__main__':
    unittest.main()