from app import slot_spinner, is_a_pair, is_three_of_kind
import pytest
import sys

def main():
    test_slot_spinner()
    test_is_three_of_kind()
    test_is_a_pair()


def test_slot_spinner():
    global sl_player_bank, sl_current_bet, bet, sl_total_won, sl_total_lost, hit_jackpot

    sl_player_bank = 200
    sl_current_bet = 0
    sl_total_won = 0
    sl_total_lost = 0
    hit_jackpot = False

    #side effects
    slot_spinner()

    # Check the results
    if sl_player_bank == 200 and hit_jackpot == True:
        assert hit_jackpot == True
        assert sl_total_won == 200000
        assert sl_player_bank == 200000
    else:
        assert sl_player_bank == 200
        assert hit_jackpot == False


def test_is_three_of_kind():
    # check where there is a three of a kind
    hand_with_three_of_kind = [('H', '2'), ('D', '2'), ('S', '2'), ('C', '5'), ('H', '9')]
    assert is_three_of_kind(hand_with_three_of_kind) == True

    # check if the three of a kind does not exist
    hand_without_three_of_kind = [('H', '2'), ('D', '3'), ('S', '4'), ('C', '5'), ('H', '9')]
    assert is_three_of_kind(hand_without_three_of_kind) == False

def test_is_a_pair():
    # Test case where there is a pair
    hand_with_pair = [('H', '2'), ('D', '2'), ('S', '4'), ('C', '5'), ('H', '9')]
    assert is_a_pair(hand_with_pair) == True

    # Test case where there is no pair
    hand_without_pair = [('H', '2'), ('D', '3'), ('S', '4'), ('C', '5'), ('H', '9')]
    assert is_a_pair(hand_without_pair) == False



if __name__ == "__main__":
    main()
