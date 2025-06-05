import numpy as np

def mean_variance_optimization(expected_returns, cov_matrix):
    inv_cov = np.linalg.inv(cov_matrix)
    ones = np.ones(len(expected_returns))
    weights = inv_cov @ expected_returns / (ones @ inv_cov @ expected_returns)
    return weights
