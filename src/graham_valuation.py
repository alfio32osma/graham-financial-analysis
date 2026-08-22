
def get_intrinsic_value(earnings_per_share, growth_rate, yield_average_AAA, yield_actual_AAA):
    if yield_average_AAA <= 0 or yield_average_AAA is None:
        raise ValueError("The average yield is not correct")

    if yield_actual_AAA <= 0 or yield_actual_AAA is None:
        raise ValueError("The actual yield is not correct")

    return (earnings_per_share * ((yield_actual_AAA * 2) + 2 * growth_rate) * yield_average_AAA) / yield_actual_AAA

def worth_it(intrinsic_value, market_price):
    if market_price >= intrinsic_value:
        return "Is not worth it"
    else:
        return "If I were you I would buy some shares"
