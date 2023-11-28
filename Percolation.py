from QuickUnion import WeightedQuickUnion, QuickUnion, WeightedQuickUnionPathCompression
import stdarray
import stdio
import fileinput
import sys

test_dictionary = {
    'test_data/percolation/input2-no.txt':
    {'percolates': False,
     'noOfOpenSites': 2,
     'isFull': {'(1,1)': False}}

}


class Percolation:
    def __init__(self, nrows, ncols, method=None):
        if (nrows < 1) or (ncols < 1):
            raise ValueError

        self.uf = None
        self.uf2 = None
        self.noOfOpenSites = 0
        self.isOpen = stdarray.create2D(nrows, ncols, 0)
        self.nrows = nrows
        self.ncols = ncols
        self.virtualBottom = self.nrows*self.nrows+1
        self.virtualTop = 0
        if method == "WeightedQuickUnionPathCompression":
            self.uf = WeightedQuickUnionPathCompression(nrows*ncols+2)
            self.uf2 = WeightedQuickUnionPathCompression(nrows*ncols+2)
        elif method == "QuickUnion":
            self.uf = QuickUnion(nrows*ncols+2)
            self.uf2 = QuickUnion(nrows*ncols+2)
        elif method == "WeightedQuickUnion":
            self.uf = WeightedQuickUnion(nrows*ncols+2)
            self.uf2 = WeightedQuickUnion(nrows*ncols+2)

    def open(self, i, j):
        self.checkValidity(i, j)
        # if it is already opened
        if (self.isOpen[i][j] == 1):
            return
        self.isOpen[i][j] = 1
        self.noOfOpenSites += 1
        # find top, left, right and bottom neigbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if ((dx == 0 or dy == 0) and (not (dx == 0 and dy == 0))):
                    if (self.checkIndex(i+dx, j+dy) and self.isOpen[i+dx][j+dy]):
                        self.uf.union(self.convert2Dto1D(i, j),
                                      self.convert2Dto1D(i+dx, j+dy))
                        self.uf2.union(self.convert2Dto1D(i, j),
                                       self.convert2Dto1D(i+dx, j+dy))
        if (i == 0):
            self.uf.union(0, self.convert2Dto1D(i, j))
            self.uf2.union(0, self.convert2Dto1D(i, j))
        if (i == self.nrows-1):
            self.uf.union(self.virtualBottom, self.convert2Dto1D(i, j))

    def isOpen(self, i, j):
        self.checkValidity(i, j)
        return (self.isOpen[i][j] == 1)

    def isFull(self, i, j):
        self.checkValidity(i, j)
        index = self.convert2Dto1D(i, j)
        return (self.uf2.find(0) == self.uf2.find(index))

    def numberOfOpenSites(self):
        return self.noOfOpenSites

    def percolates(self):
        return (self.uf.find(0) == self.uf.find(self.virtualBottom))
    # converting 2D isOpen array to parents array

    def convert2Dto1D(self, i, j):
        return (i*self.ncols+j+1)

    def getParent(self):
        parents = stdarray.create2D(self.nrows, self.ncols, 0)
        for x in range(self.nrows):
            for y in range(self.ncols):
                parents[x][y] = self.uf.find(self.convert2Dto1D(x, y))
        return parents
    # get parents with index or only virtual top and bottom points

    def getParentVirtualOrIndex(self, i=None, j=None):
        if (i is not None and j is not None):
            index = self.convert2Dto1D(i, j)
            return self.uf.find(index), self.uf2.find(index)
        else:
            return self.uf.find(0), self.uf.find(self.virtualBottom), self.uf2.find(0), self.uf2.find(self.virtualBottom)
    # check the validity of index index

    def checkIndex(self, i, j):
        return ((i >= 0) and (i < self.nrows) and (j >= 0) and (j < self.ncols))

    def checkValidity(self, i, j):
        if not (self.checkIndex(i, j)):
            raise IndexError

    def getIsFull(self):
        isFull = stdarray.create2D(self.nrows, self.ncols, 0)
        for i in range(self.nrows):
            for j in range(self.ncols):
                isFull[i][j] = self.isFull(i, j)
        return isFull


if __name__ == "__main__":
    n = stdio.readInt()
    percolation = Percolation(n, n, method="WeightedQuickUnionPathCompression")

    while not stdio.isEmpty():
        i = stdio.readInt()
        j = stdio.readInt()

        percolation.open(i, j)

    print("Percolation is {}".format(percolation.percolates()))
    print("--------")
    print("Number of  open sites {}".format(percolation.numberOfOpenSites()))
    print("--------")
    print("Open sites")
    stdarray.write2D(percolation.isOpen)
    print("--------")
    print("Full sites")
    stdarray.write2D(percolation.getIsFull())
