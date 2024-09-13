import unittest

from stack_via_list import StackList

#5*
def is_balanced(tokens: str) -> bool:
    st = StackList()
    for token in tokens:
        if token == '(':
            st.push(token)
        elif token == ')':
            st.pop() if st.peek() == '(' else st.push(token)
    return st.size() == 0

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

if __name__ == '__main__':
    unittest.main()