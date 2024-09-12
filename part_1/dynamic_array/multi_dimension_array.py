from part_1.dynamic_array.dyn_array import DynArray

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

arr = MultiDimensionArray.make(*[[[1], [2], [3]],
                                 [[4], [5], [6]]])

arr[1][1].append(23)
