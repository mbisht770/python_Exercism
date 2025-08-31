"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget, exchange_rate):
    """Calculate how much foreign currency you can get."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Return leftover amount after exchanging."""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of given bills."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Return how many whole bills can be obtained from the amount."""
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Return leftover amount after exchanging into whole bills."""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Return maximum value of foreign currency in whole bills after exchange."""
    adjusted_rate = exchange_rate * (1 + spread / 100)
    total_foreign_currency = budget / adjusted_rate
    number_of_bills = int(total_foreign_currency // denomination)
    return denomination * number_of_bills
