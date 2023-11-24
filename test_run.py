import unittest
from QuickUnion.QuickUnion import QuickUnion, WeightedQuickUnion, WeightedQuickUnionPathCompression, TicToc


def time_func(func):
    def wrapper(*args, **kwargs):
        tt = TicToc()
        start = tt.tic()
        result = func(*args, **kwargs)
        end = tt.toc()
        print("TIME = %.6f seconds in %s" % (tt.toc(), func.__name__))
        return result
    return wrapper


def test_from_file(test_file, method="QuickUnion"):
    with open(test_file) as f:

        n = int(f.readline())
        qf = None
        if method == "WeightedQuickUnion":
            qf = WeightedQuickUnion(n)
        elif method == "QuickUnion":
            qf = QuickUnion(n)
        elif method == "WeightedQuickUnionPathCompression":
            qf = WeightedQuickUnionPathCompression(n)
        while True:
            line = f.readline()
            if not line:
                break
            l = [int(i) for i in line.strip("\n").split(" ")]
            qf.union(l[0], l[1])

        return qf


class TestQuickUnion(unittest.TestCase):
    @time_func
    def test_one(self):
        qf = test_from_file("./test_data/tinyUF.txt", method="QuickUnion")
        self.assertTrue(qf.get_count() == 2)

    @time_func
    def test_two(self):
        qf = test_from_file("./test_data/tinyUF.txt",
                            method="WeightedQuickUnion")
        self.assertTrue(qf.get_count() == 2)

    @time_func
    def test_third(self):
        qf = test_from_file("./test_data/tinyUF.txt",
                            method="WeightedQuickUnionPathCompression")
        self.assertTrue(qf.get_count() == 2)


if __name__ == '__main__':
    unittest.main()
