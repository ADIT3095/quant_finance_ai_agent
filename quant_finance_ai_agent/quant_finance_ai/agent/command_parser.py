from models.pricing.black_scholes import black_scholes_price
from data_pipeline.data_loader import get_latest_price
from data_pipeline.preprocessing import parse_command

def parse_and_execute(command: str):
    params = parse_command(command)
    S = get_latest_price(params['ticker'])
    price = black_scholes_price(
        option_type=params['option_type'],
        S=S,
        K=params['K'],
        T=params['T'],
        r=params['r'],
        sigma=params['sigma']
    )
    return {"price": price, "params": params}
