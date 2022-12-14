import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def explained_variance(X):
    # Calculate the singular value decomposition of the matrix X
    U, s, V = np.linalg.svd(X)

    # Calculate the sum of the squared values in the diagonal elements of S
    s_sum = np.sum(s**2)

    # Calculate the sum of the squared values of all elements in X
    x_sum = np.sum(X**2)

    # Calculate the explained variance
    explained_variance = s_sum/x_sum

    return explained_variance
print("hey")

