import unittest

from part_1.ordered_list.ordered_list import OrderedStringList, Node

def to_values(list_nodes: [Node | None]):
    return [node.value for node in list_nodes]

class TestAddMethod(unittest.TestCase):
    def test_add_ascending(self):
        ordered = OrderedStringList.make(True, "A  ", "   B")
        self.assertEqual(to_values(ordered), ["A  ", "   B"])
        self.assertEqual(ordered.len(), 2)

        ordered = OrderedStringList.make(True, "abandon", "abate", "abide")
        ordered.add("abduct")
        self.assertEqual(to_values(ordered), ["abandon", "abate", "abduct", "abide"])
        self.assertEqual(ordered.len(), 4)

        ordered = OrderedStringList.make(True, "abandon", "abate", "abide")
        ordered.add("abduct")
        ordered.add("able")
        self.assertEqual(to_values(ordered), ["abandon", "abate", "abduct", "abide", "able"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(True, "able")
        ordered.add("abandon")
        ordered.add("abate")
        ordered.add("abduct")
        ordered.add("abide")
        self.assertEqual(to_values(ordered), ["abandon", "abate", "abduct", "abide", "able"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(True, "abandon", "abandon", "abandon", "abandon")
        ordered.add("abate")
        self.assertEqual(to_values(ordered), ["abandon", "abandon", "abandon", "abandon", "abate"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(True, "abandon", "abandon", "abandon", "abandon")
        ordered.add("aba")
        self.assertEqual(to_values(ordered), ["aba", "abandon", "abandon", "abandon", "abandon"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(True, "abandon", "abandon", "abandon", "abandon")
        ordered.add("abandon")
        self.assertEqual(to_values(ordered), ["abandon", "abandon", "abandon", "abandon", "abandon"])
        self.assertEqual(ordered.len(), 5)

    def test_add_descending(self):
        ordered = OrderedStringList.make(False, "abandon", "abate")
        self.assertEqual(to_values(ordered), ["abate", "abandon"])
        self.assertEqual(ordered.len(), 2)

        ordered = OrderedStringList.make(False, "abide", "abate", "abandon")
        ordered.add("abduct")
        self.assertEqual(to_values(ordered), ["abide", "abduct", "abate", "abandon"])
        self.assertEqual(ordered.len(), 4)

        ordered = OrderedStringList.make(False, "abide", "abate", "abandon")
        ordered.add("abduct")
        ordered.add("able")
        self.assertEqual(to_values(ordered), ["able", "abide", "abduct", "abate", "abandon"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(False, "able")
        ordered.add("abandon")
        ordered.add("abate")
        ordered.add("abduct")
        ordered.add("abide")
        self.assertEqual(to_values(ordered), ["able", "abide", "abduct", "abate", "abandon"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(False, "abandon", "abandon", "abandon", "abandon")
        ordered.add("abate")
        self.assertEqual(to_values(ordered), ["abate", "abandon", "abandon", "abandon", "abandon"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(False, "abandon", "abandon", "abandon", "abandon")
        ordered.add("aba")
        self.assertEqual(to_values(ordered), ["abandon", "abandon", "abandon", "abandon", "aba"])
        self.assertEqual(ordered.len(), 5)

        ordered = OrderedStringList.make(False, "abandon", "abandon", "abduct", "abduct", "abide")
        ordered.add("abate")
        self.assertEqual(to_values(ordered), ["abide", "abduct", "abduct", "abate", "abandon", "abandon"])
        self.assertEqual(ordered.len(), 6)
#
#
class TestCleanMethod(unittest.TestCase):
    def test_clean(self):
        ordered = OrderedStringList.make(True, "abandon", "abate", "abduct", "abide", "able")

        ordered.clean(False)
        self.assertEqual(to_values(ordered), [])
        self.assertEqual(ordered.len(), 0)

        for s in ["able", "abide", "abduct", "abate", "abandon"]:
            ordered.add(s)
        self.assertEqual(to_values(ordered), ["able", "abide", "abduct", "abate", "abandon"])
        self.assertEqual(ordered.len(), 5)


class TestFindMethod(unittest.TestCase):
    def test_find(self):
        ordered = OrderedStringList.make(True, "abandon", "abate", "abduct", "abide", "able")
        self.assertTrue(ordered.find("abduct") is not None)
        self.assertTrue(ordered.find("glory") is None)

        ordered = OrderedStringList.make(False, "abandon", "abate", "abduct", "abide", "able")
        self.assertTrue(ordered.find("abduct") is not None)
        self.assertTrue(ordered.find("glory") is None)


class TestDeleteMethod(unittest.TestCase):
    def test_delete(self):
        ordered = OrderedStringList(True)
        ordered.delete("fix")
        self.assertEqual(ordered.size, 0)

        ordered = OrderedStringList.make(True, "fix")
        ordered.delete("fix")
        self.assertEqual(ordered.size, 0)

        ordered = OrderedStringList.make(True,  "abide", "abduct", "abate", "abandon")
        ordered.delete("abate")
        self.assertEqual(to_values(ordered), ["abandon", "abduct", "abide"])
        self.assertEqual(ordered.size, 3)

        ordered = OrderedStringList.make(False, "abandon", "abate", "abduct", "abide")
        ordered.delete("abduct")
        self.assertEqual(to_values(ordered), ["abide", "abate", "abandon"])
        self.assertEqual(ordered.size, 3)

if __name__ == '__main__':
    unittest.main()
