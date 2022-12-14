
import numpy as np

def partA():
    np.random.seed(24122022)
    N = 100
    mean = [0, 0]
    cov = [[1, 1.5], [1.5, 3]]
    x1, x2 = np.random.multivariate_normal(mean, cov, N).T

    cov_matrix = np.cov(x1, x2)
    print(cov_matrix)

    print("Hey")
partA();
#[[1.01593041 1.50250145]
#[1.50250145 3.00892133]]
