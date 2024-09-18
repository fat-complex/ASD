import unittest

from part_1.deque.deque import Deque

# class BracketsValidator:
#     def __init__(self):
#         self.

def is_balanced(tokens: str) -> bool:
    deque = Deque()
    for token in tokens:
        if is_open_bracket(token):
            deque.addFront(token)
        elif is_close_bracket(token):
            deque.removeFront() if token == map_to_close_bracket(deque.top_value()) else deque.addFront(token)
    return deque.size() == 0

def is_open_bracket(token: str) -> bool:
    match token:
        case "(": return True
        case "{": return True
        case "[": return True
    return False


def is_close_bracket(token: str) -> bool:
    match token:
        case ")": return True
        case "}": return True
        case "]": return True
    return False


def map_to_close_bracket(token: str) -> str:
    match token:
        case "(": return ")"
        case "{": return "}"
        case "[": return "]"
    return ""

class TestIsValidBrackets(unittest.TestCase):
    def test_suite(self):
        target = "((1 + 2) * ((3 + 4) - (6 - 5)) * 4)"
        self.assertTrue(is_balanced(target))

        target = "((x - 1) * (x - 2) * ((x + 1)"
        self.assertFalse(is_balanced(target))

        target = "(1"
        self.assertFalse(is_balanced(target))

        target = ""
        self.assertTrue(is_balanced(target))

        target = "1 + 2"
        self.assertTrue(is_balanced(target))

        target = "())("
        self.assertFalse(is_balanced(target))

        target = "))(("
        self.assertFalse(is_balanced(target))

        target = "((())"
        self.assertFalse(is_balanced(target))

        target = "array[]"
        self.assertTrue(is_balanced(target))

        target = "()"
        self.assertTrue(is_balanced(target))

        target = "if (x == 1) {}"
        self.assertTrue(is_balanced(target))

        target = "{[()]}"
        self.assertTrue(is_balanced(target))

        target = "if (x == 1) { array[idx()] = 23}"
        self.assertTrue(is_balanced(target))

if __name__ == '__main__':
    unittest.main()