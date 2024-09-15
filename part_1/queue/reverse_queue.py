from part_1.queue.queue import Queue
from part_1.stack.stack import Stack


def reverse_queue(q: Queue) -> Queue:
    st = Stack()
    while q.size() > 0:
        st.push(q.dequeue())
    while st.size() > 0:
        q.enqueue(st.pop())
    return q


import unittest

class TestRevereQueueFunction(unittest.TestCase):
    def test_reverse(self):
        q = Queue()
        target = [val for val in range(1, 6)] # [1, 2, 3, 4, 5]
        for val in target:
            q.enqueue(val)

        q = reverse_queue(q)
        self.assertEqual(q.front(), 5)
        self.assertEqual(q.back(), 1)

        rev = []
        while q.size() > 0:
            rev.append(q.dequeue())

        target.reverse()
        self.assertEqual(target, rev)


if __name__ == '__main__':
    unittest.main()
