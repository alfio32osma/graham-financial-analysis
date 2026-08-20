import requests
import os
from fredapi import Fred

api_key = os.getenv("FRED_API_KEY", "0caf5c25af1e8960129399b268c5c102")

def main():
    market_price = (get_number((input("Price share: $"))))
    earnings_per_share = (get_number(input("Earnings per share: $")))
    growth_rate = get_decimal(3)

    try:
        yield_actual_AAA, yield_average_AAA = get_yields_AAA()
    except Exception:
        print("Warning: Could not fetch real data, using default values.")
        yield_actual_AAA, yield_average_AAA = [5.76, 3.97]

    intrinsic_value = get_intrinsic_value(earnings_per_share, growth_rate, yield_average_AAA, yield_actual_AAA)
    print(f"Intrinsic value: ${intrinsic_value:.02f}\nMarket price: ${market_price:.02f}")
    recommendation = worth_it(intrinsic_value, market_price)
    print(recommendation)

def worth_it(intrinsic_value, market_price):
    if market_price >= intrinsic_value:
        return "Is not worth it"
    else:
        return "If I were you I would buy some shares"

def get_number(n):
    try:
        number = float(n)
        if number < 0:
            raise ValueError("The price never can be negative")
        return float(number)
    except ValueError:
        raise ValueError("Please type the price in numbers")

def get_yields_AAA():
    response = requests.get(f"https://api.stlouisfed.org/fred/series/observations?series_id=AAA&observation_start=2015-01-01&realtime_end=9999-12-31&api_key={api_key}&file_type=json")
    content = response.json()
    if content["observations"][-1]["value"].isalpha():
        raise ValueError("Is not a number")
    else:
        actual = float(content["observations"][-1]["value"])
    list_historical_yield_AAA = []
    for value in content["observations"]:
        try:
            number = float(value['value'])
            if number > 0:
                list_historical_yield_AAA.append(number)
        except ValueError:
            pass
    average = sum(list_historical_yield_AAA) / len(list_historical_yield_AAA)
    return [actual, round(average, 2)]

def get_decimal(a):
    return a/100

def get_intrinsic_value(earnings_per_share, growth_rate, yield_average_AAA, yield_actual_AAA):
    if yield_average_AAA <= 0 or yield_average_AAA is None:
        raise ValueError("The average yield is not correct")

    if yield_actual_AAA <= 0 or yield_actual_AAA is None:
        raise ValueError("The actual yield is not correct")

    return (earnings_per_share * ((yield_actual_AAA * 2) + 2 * growth_rate) * yield_average_AAA) / yield_actual_AAA

if __name__ == "__main__":
    main()
