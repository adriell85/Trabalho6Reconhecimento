import matplotlib
matplotlib.use('TkAgg')
from runs import KNNRuns,DMCRuns,BayesianGaussianDiscriminantRuns,KmeansQuantRuns, BayesianRejectionRuns


def main():
    BayesianRejectionRuns(0)
    BayesianRejectionRuns(1)
    BayesianRejectionRuns(2)

if __name__ == "__main__":
    main()
