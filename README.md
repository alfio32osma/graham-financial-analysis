# Intrinsic Value Calculator (Benjamin Graham Model)
- Video Demo: <[CS50P Final Project - Intrinsic Value Calculator](https://youtu.be/DzkGx-fkUaQ)>

## Overview
The **Intrinsic Value Calculator** is a command-line tool written in Python designed to calculate the intrinsic value of a stock based on Benjamin Graham's classic valuation formula. By combining user inputs (such as the current market price and earnings per share) with macroeconomic data fetched dynamically from the Federal Reserve Economic Data (FRED) API, the program helps investors determine whether a stock is undervalued or overvalued relative to its calculated intrinsic value.

## How It Works
The script performs the following core steps:
1. **User Input Collection:** Prompts the user to securely input the current market price of a share and its earnings per share (EPS), validating that the inputs are valid positive numbers using custom error-handling functions.

2. **Macroeconomic Data Fetching:** Automatically connects to the official FRED API to retrieve historical and actual AAA corporate bond yields. It computes the long-term average yield and grabs the most recent yield to serve as the baseline discount/interest rate parameters in Graham's formula.
3. **Intrinsic Value Computation:** Applies Benjamin Graham's intrinsic value formula taking into account the EPS, expected growth rate, average AAA bond yield, and actual AAA bond yield.
4. **Recommendation:** Compares the resulting intrinsic value against the current market price and outputs a clear recommendation ("Is not worth it" vs. "If I were you I would buy some shares").

## Project Structure (`project.py`)
The project is structured around a main execution block and several independent, testable helper functions:
* **`main()`:** Coordinates the program flow. It gathers user inputs, handles potential API connection dropouts by falling back to safe default yields, calculates the intrinsic value, and prints out the final comparison and recommendation.

* **`worth_it(intrinsic_value, market_price)`:** Evaluates whether the market price is greater than or equal to the intrinsic value, returning a practical investment opinion.
* **`get_number(n)`:** A robust input-validation function that ensures the values provided by the user are floats and throws a `ValueError` if text or negative numbers are introduced.
* **`get_yields_AAA()`:** Connects to the FRED API via HTTP GET requests, processes the JSON response containing historical AAA bond observations, filters out non-numeric entries, and calculates both the current yield and the historical average yield.
* **`get_decimal(a)`:** Converts percentage integers into clean decimal multipliers for the growth rate calculation.
* **`get_intrinsic_value(...)`:** Encapsulates the mathematical logic of the Benjamin Graham formula, ensuring that division-by-zero or negative yield errors are properly caught.

## Testing (`test_project.py`)
To ensure high software reliability and correctness, unit tests have been implemented using the `pytest` framework.

* **`test_get_intrinsic_value()`:** Verifies that the mathematical formula computes expected outputs accurately and correctly raises `ValueError` exceptions if invalid yields are passed.

* **`test_get_number()`:** Tests multiple edge cases for user input validation, ensuring proper handling of valid floats, strings/names, and negative numbers.
* **`test_get_yields_AAA()` and `test_get_yields_AAA_error()`:** Utilizes `unittest.mock.patch` to mock external API responses. This allows testing of the JSON parsing and error-handling logic safely without depending on an active internet connection or live API availability.

## Dependencies (`requirements.txt`)

The project relies on external libraries specified in the `requirements.txt` file:

* `requests`: To handle HTTP GET requests directed at the FRED REST API.

* `fredapi`: For handling interactions with Federal Reserve economic data wrappers if needed.
