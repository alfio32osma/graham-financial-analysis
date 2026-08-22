def get_number(n):
    try:
        number = float(n)
        if number < 0:
            raise ValueError("The price never can be negative")
        return float(number)
    except ValueError:
        raise ValueError(f"Invalid input: '{n}' is not a valid number.")

def get_decimal(a):
    return a/100
