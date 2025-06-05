from math import exp

def asian_option_price(average_price, K, r, T, sigma):
    return max(average_price - K, 0) * exp(-r * T)
