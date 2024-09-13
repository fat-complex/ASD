import unittest

from stack_via_list import StackList

# 6*
def is_balanced(tokens: str) -> bool:
    st = StackList()
    for token in tokens:
        if is_open_bracket(token):
            st.push(token)
        elif is_close_bracket(token):
            st.pop() if token == map_to_close_bracket(st.peek()) else st.push(token)
    return st.size() == 0

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
        target = "(()((())()))"
        self.assertTrue(is_balanced(target))

        target = "(()()(()"
        self.assertFalse(is_balanced(target))

        target = "("
        self.assertFalse(is_balanced(target))

        target = ""
        self.assertTrue(is_balanced(target))

        target = "())("
        self.assertFalse(is_balanced(target))

        target = "))(("
        self.assertFalse(is_balanced(target))

        target = "((())"
        self.assertFalse(is_balanced(target))

        target = "[]"
        self.assertTrue(is_balanced(target))

        target = "()"
        self.assertTrue(is_balanced(target))

        target = "{}"
        self.assertTrue(is_balanced(target))

        target = "{[()]}"
        self.assertTrue(is_balanced(target))

        target = "{[()}]}"
        self.assertFalse(is_balanced(target))

if __name__ == '__main__':
    unittest.main()