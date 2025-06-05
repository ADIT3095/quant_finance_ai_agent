import numpy as np
from scipy.stats import norm

def calculate_var(returns, confidence_level=0.95):
    mean = np.mean(returns)
    std = np.std(returns)
    z = norm.ppf(1 - confidence_level)
    return -(mean + z * std)
