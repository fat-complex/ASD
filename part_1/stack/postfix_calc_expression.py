import math
import unittest

from stack import Stack

def calc_expression(postfix_expr: str) -> int:
    target = to_stack(postfix_expr)
    operands = Stack()

    while target.size() > 0 and target.peek() != '=':
        token = target.pop()
        if is_operand(token):
            operands.push(token)
        elif is_operator(token):
            operand_a = operands.pop()
            operand_b = operands.pop()
            operands.push(cal(token, int(operand_a), int(operand_b)))
    return operands.peek() if target.peek() == '=' else math.nan

def to_stack(postfix_expr: str) -> Stack:
    stack = Stack()
    for token in reversed(postfix_expr):
        if is_operand(token) or is_operator(token):
            stack.push(token)
    return stack


def is_operator(token: str) -> bool:
    match token:
        case '+': return True
        case '-': return True
        case '*': return True
        case '/': return True
        case '=': return True
    return False

def is_operand(token: str) -> bool:
    return token.isdigit()

def cal(op: str, a: int, b: int) -> int:
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a // b
    raise ValueError('Operation {} does not supported'.format(op))


class TestIsValidBrackets(unittest.TestCase):
    def test_expr(self):
        expr = "1 2 + 3 * ="
        self.assertEqual(calc_expression(expr), 9)

        expr = "1 2 +"
        self.assertTrue(math.isnan(calc_expression(expr)))

        expr = "8 2 + 5 * 9 + ="
        self.assertEqual(calc_expression(expr), 59)

if __name__ == '__main__':
    unittest.main()