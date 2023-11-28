# Implemented based on Java implementations
# https://algs4.cs.princeton.edu/15uf/QuickFindUF.java.html
# https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionPathCompressionUF.java.html
# https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionUF.java.html

from abc import ABC, abstractmethod
from TicToc import TicToc


class BaseQuickUnion(ABC):
    def __init__(self, n):
        # size of parent array
        self.n = n
        # number of components
        self.count = n
        # array for showing the root of its component
        self.parent = [i for i in range(n)]

    def get_count(self):
        return self.count

    def validate(self, p):

        if (p < 0 or p >= self.n):
            raise ValueError

    def find(self, p):

        self.validate(p)
        while (p != self.parent[p]):
            p = self.parent[p]
        return p


class QuickUnion(BaseQuickUnion):
    def __init__(self, n):
        super().__init__(n)

    def union(self, p, q):
        rootP = super().find(p)
        rootQ = super().find(q)
        if (rootP == rootQ):
            return
        self.parent[rootP] = rootQ
        self.count -= 1


class WeightedQuickUnion(BaseQuickUnion):
    def __init__(self, n):
        super().__init__(n)
        self.size = [1]*self.count

    def union(self, p, q):
        rootP = super().find(p)
        rootQ = super().find(q)
        if (rootP == rootQ):
            return
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -= 1


class WeightedQuickUnionPathCompression(WeightedQuickUnion):
    def __init__(self, n):
        super().__init__(n)

    def find(self, p):
        super().validate(p)
        root = p
        while (root != self.parent[root]):
            root = self.parent[root]
        while (p != root):
            newp = self.parent[p]
            self.parent[p] = root
            p = newp
        return root
