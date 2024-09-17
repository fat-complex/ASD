import unittest

from part_1.deque.deque import Deque

def is_palindrome(word: str) -> bool:
    deque = Deque()
    for ch in word:
        deque.addTail(ch)

    while deque.size() >= 1:
        top = deque.top_value()
        back = deque.back_value()
        if top != back:
            return False
        deque.removeFront()
        deque.removeTail()
    return True

class TestIsPalindromeFunction(unittest.TestCase):
    def test_is_palindrome(self):
        word = "ABA"
        self.assertTrue(is_palindrome(word))

        word = "ABOBA"
        self.assertTrue(is_palindrome(word))

        word = "ABOBAR"
        self.assertFalse(is_palindrome(word))

        word = "rotator"
        self.assertTrue(is_palindrome(word))

        word = "A"
        self.assertTrue(is_palindrome(word))

        word = ""
        self.assertTrue(is_palindrome(word))


if __name__ == '__main__':
    unittest.main()