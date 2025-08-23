"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    1.  'J', 'Q', or 'K' = 10
    2.  'A' = 1
    3.  '2' - '10' = numerical value
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.
    :return: str or tuple - card with higher value, or both if equal.
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 == v2:
        return card_one, card_two
    elif v1 > v2:
        return card_one
    else:
        return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the upcoming ace card.

    :param card_one, card_two: str - cards already in hand.
    :return: int - either 1 or 11 value of the upcoming ace card.
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if card_one == "A" or card_two == "A":
        return 1
    if v1 + v2 + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Check if the two-card hand is a blackjack (Ace + 10-card)."""
    ten_cards = ["10", "J", "Q", "K"]

    return (card_one == "A" and card_two in ten_cards) or \
           (card_two == "A" and card_one in ten_cards)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Check if two cards can be split into pairs."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Check if a hand can be doubled down (total = 9, 10, or 11)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
