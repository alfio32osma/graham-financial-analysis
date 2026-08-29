from src import (
    get_yields_AAA,
    get_intrinsic_value,
    worth_it,
    get_number,
    get_decimal
)

DEFAULT_ACTUAL_YIELD = 5.76
DEFAULT_AVERAGE_YIELD = 3.97 
DEFAULT_GROWTH_RATE = 3 # THIS IS A CONSERVATIVE GROWTH


def main():
    market_price = (get_number((input("Price share: $"))))
    earnings_per_share = (get_number(input("Earnings per share: $")))
    growth_rate = get_decimal(3)

    try:
        yield_actual_AAA, yield_average_AAA = get_yields_AAA()
    except Exception:
        print("Warning: Could not fetch real data, using default values.")
        yield_actual_AAA, yield_average_AAA = [DEFAULT_ACTUAL_YIELD, DEFAULT_AVERAGE_YIELD]

    intrinsic_value = get_intrinsic_value(earnings_per_share, growth_rate, yield_average_AAA, yield_actual_AAA)
    print(f"Intrinsic value: ${intrinsic_value:.02f}\nMarket price: ${market_price:.02f}")
    
    recommendation = worth_it(intrinsic_value, market_price)
    print(recommendation)


if __name__ == "__main__":
    main()
