from part_1.dynamic_array.dyn_array import DynArray
import unittest


class MultiDimensionArray(DynArray):

    def __init__(self):
        super().__init__()

    @staticmethod
    def make(*args):
        arr: MultiDimensionArray = MultiDimensionArray()
        for arg in args:
            if isinstance(arg, list):
                arr.append(MultiDimensionArray.make(*arg))
            else:
                arr.append(arg)
        return arr

class TestMultiDimension(unittest.TestCase):
    def test_add_elem(self):

        # three-dimensional array
        arr = MultiDimensionArray.make(*[[[1], [2], [3]],  # row 0
                                         [[4], [5], [6]]]) # row 1
        arr[1][1].append(23)
        # Result:
        # [[[1], [2], [3]], row 0
        #  [[4], [5, 23], [6]]] row 1

        self.assertEqual(arr[1][1][0], 5)
        self.assertEqual(arr[1][1][1],  23)

        # add row
        arr.insert(len(arr), [[44], [45], [46]])
        self.assertEqual(arr[2][0][0], 44)



if __name__ == '__main__':
    unittest.main()

