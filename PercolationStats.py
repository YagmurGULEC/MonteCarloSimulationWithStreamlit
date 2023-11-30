from Percolation import Percolation
import stdarray
import random
import math


class PercolationStats:
    confidenceInterval = 1.96

    def __init__(self, nrows, ncols, trials):
        if (nrows < 1 and ncols < 1 and trials < 1):
            raise ValueError

        self.trials = trials
        self.stats = None
        self.nrows = nrows
        self.ncols = ncols

    def mean(self):
        return (sum(self.stats)/len(self.stats))

    def stddev(self):
        total = 0
        for i in self.stats:
            total += (i-self.mean())*(i-self.mean())
        return total/(len(self.stats)-1)

    def confidenceHi(self):
        return self.mean()+(self.confidenceInterval*self.stddev()/math.sqrt(self.trials))

    def confidenceLo(self):
        return self.mean()-(self.confidenceInterval*self.stddev()/math.sqrt(self.trials))

    def run_simulation(self):

        self.stats = self.run_simulation_static(
            self.trials, self.nrows, self.ncols)

    @staticmethod
    def run_simulation_static(trials, nrows, ncols):
        stats = stdarray.create1D(trials, 0)
        for t in range(trials):
            percolation = Percolation(nrows, ncols)

            while True:
                i, j = random.randint(
                    0, nrows-1), random.randint(0, ncols-1)
                percolation.open(i, j)
                if percolation.percolates():
                    break
            stats[t] = percolation.numberOfOpenSites() / \
                (nrows*ncols)
        return stats


if __name__ == "__main__":
    pstats = PercolationStats(100, 100, 100)
    pstats.run_simulation()
    print("Mean: {}".format(pstats.mean()))
    print("Standard deviation: {}".format(pstats.stddev()))
    print("95 percentage confidence interval {} {}".format(pstats.confidenceLo(),
          pstats.confidenceHi()))
