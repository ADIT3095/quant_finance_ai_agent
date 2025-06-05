import re

def parse_command(text):
    params = {"ticker": "AAPL", "option_type": "call", "K": 100, "T": 0.25, "r": 0.05, "sigma": 0.2}
    if "put" in text.lower():
        params['option_type'] = "put"

    strike = re.search(r'strike\s*(\d+)', text)
    if strike: params['K'] = float(strike.group(1))

    expiry = re.search(r'(\d+)\s*(months?|days?)', text)
    if expiry:
        t = int(expiry.group(1))
        params['T'] = t / 12 if 'month' in expiry.group(2) else t / 365

    vol = re.search(r'volatility\s*(\d+)%', text)
    if vol: params['sigma'] = float(vol.group(1)) / 100

    rate = re.search(r'rate\s*(\d+)%', text)
    if rate: params['r'] = float(rate.group(1)) / 100

    return params
