from calculations.future_value_calculator import calculate_future_value


def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)


def ask_for_float_value(message):
    input_value = input(message)
    return float(input_value)


init_value = ask_for_float_value("Initial investment value: ")
interest_rate = ask_for_float_value("Interest rate (%): ")
investment_time_years = ask_for_int_value("Investment time (years): ")

investment_future_value = calculate_future_value(init_value, interest_rate, investment_time_years)

print(f"Your investment after {investment_time_years:.0f} yars: {investment_future_value:,.2f}")
