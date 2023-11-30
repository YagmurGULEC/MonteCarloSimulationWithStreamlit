from Percolation import Percolation
from test_run import time_func, test_from_file
import unittest
import glob

test_dictionary = {
    './test_data/percolation/input1.txt':
    {'percolates': True,
     'noOfOpenSites': 1,
     'isFull': {
         (0, 0): True
     }
     },
    './test_data/percolation/input2-no.txt':
    {'percolates': False,
     'noOfOpenSites': 2,
     'isFull': {(1, 1): False,
                (0, 0): True
                }
     },
    './test_data/percolation/input2.txt':
    {'percolates': True,
     'noOfOpenSites': 3,
     'isFull': {(1, 1): True,
                (0, 0): True,
                (0, 1): True
                }
     },
    './test_data/percolation/input3.txt':
    {'percolates': True,
     'noOfOpenSites': 6,
     'isFull': {(0, 0): True,
                (1, 0): True,
                (2, 0): True,
                (0, 2): True,
                (1, 2): True,
                (2, 2): True
                }
     },
    './test_data/percolation/input4.txt':
    {'percolates': True,
     'noOfOpenSites': 8,
     'isFull': {(0, 0): True,
                (1, 0): True,
                (1, 1): False,
                (2, 0): True,
                (3, 0): True,
                (0, 3): True,
                (1, 3): True,
                (2, 3): True,
                (3, 3): True

                }
     },
    './test_data/percolation/input5.txt':
    {'percolates': True,
     'noOfOpenSites': 25,
     'isFull': {(0, 0): True,
                (1, 0): True,
                (1, 1): True,
                (2, 0): True,
                (3, 0): True,
                (0, 3): True,
                (1, 3): True,
                (2, 3): True,
                (3, 3): True

                }
     },
    './test_data/percolation/input6.txt':
    {'percolates': True,
     'noOfOpenSites': 18,
     'isFull': {(0, 0): False,
                (1, 0): True,
                (5, 1): True,
                (5, 2): False

                }
     }

}


def test_run_percolation(test_file):
    with open(test_file) as f:
        n = int(f.readline())
        percolation = Percolation(
            n, n, method="WeightedQuickUnionPathCompression")
        while True:
            line = f.readline()
            l = []
            if not line:
                break
            for i in line.split(" "):
                try:
                    int(i)
                    l.append(int(i))
                except:
                    pass

            percolation.open(l[0], l[1])
        return percolation


if __name__ == '__main__':
    files = glob.glob('./test_data/percolation/*.txt')

    for f in files:
        if test_dictionary.get(f):
            p = test_run_percolation(f)
            assert (p.percolates() == test_dictionary[f]['percolates'])
            assert (p.numberOfOpenSites() ==
                    test_dictionary[f]['noOfOpenSites'])
            for x, v in test_dictionary[f]['isFull'].items():
                assert (p.isFull(x[0], x[1]) == v)
