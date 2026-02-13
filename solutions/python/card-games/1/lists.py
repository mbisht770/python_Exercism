"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(n):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [n,n+1,n+2]

    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1+(rounds_2)
    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return True if number in rounds else False
    pass


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    card_average=sum(hand) / len(hand)
    return card_average
    pass


def approx_average_is_average(hand):
    # True average
    true_avg = sum(hand) / len(hand)

    # Average of first and last card
    approx_avg = (hand[0] + hand[-1]) / 2

    # Middle card
    middle_card = hand[len(hand) // 2]

    # Check condition
    return approx_avg == true_avg or middle_card == true_avg


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    s_even=0
    s_odd=0
    c_od=0
    c_e=0
    for i in range(len(hand)):
        if i%2==0:
            c_e+=1
            s_even+=hand[i]
        else:
            c_od+=1
            s_odd+=hand[i]
    
    return (s_even/c_e)==(s_odd/c_od)
    


def maybe_double_last(hand):

    if hand[-1] == 11:
        hand[-1] *= 2

    return hand
    