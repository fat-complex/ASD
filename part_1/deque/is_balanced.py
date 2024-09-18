import unittest

from part_1.deque.deque import Deque

class ParenthesisValidator:
    def __init__(self):
        self.open_parenthesis = {"(", "{", "["}
        self.close_parenthesis = {")", "}", "]"}
        self.parenthesis_mapper = {"(": ")", "[": "]", "{": "}"}


    def validate_expression(self, expr: str) -> bool:
        deque = Deque()
        for token in expr:
            if token in self.open_parenthesis:
                deque.addFront(token)
            elif token in self.close_parenthesis and not deque.is_empty():
                deque.removeFront() if token == self.parenthesis_mapper.get(deque.top_value()) else deque.addFront(token)
        return deque.size() == 0


class TestIsValidBrackets(unittest.TestCase):
    def test_suite(self):
        parenthesis_validator = ParenthesisValidator()
        target = "((1 + 2) * ((3 + 4) - (6 - 5)) * 4)"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "((x - 1) * (x - 2) * ((x + 1)"
        self.assertFalse(parenthesis_validator.validate_expression(target))

        target = "(1"
        self.assertFalse(parenthesis_validator.validate_expression(target))

        target = ""
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "1 + 2"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "())("
        self.assertFalse(parenthesis_validator.validate_expression(target))

        target = "))(("
        self.assertFalse(parenthesis_validator.validate_expression(target))

        target = "((())"
        self.assertFalse(parenthesis_validator.validate_expression(target))

        target = "array[]"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "()"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "if (x == 1) {}"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "{[()]}"
        self.assertTrue(parenthesis_validator.validate_expression(target))

        target = "if (x == 1) { array[idx()] = 23}"
        self.assertTrue(parenthesis_validator.validate_expression(target))

if __name__ == '__main__':
    unittest.main()