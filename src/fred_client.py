import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("FRED_API_KEY")
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