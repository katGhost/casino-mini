import sys
import random
import time
import emoji
from emoji import EMOJI_DATA


emoji_dictionary = EMOJI_DATA

def main():
    casino_entry()
    answer = input(f"Enter [1] for Poker or [2] for Slots: ").strip().lower()

    if answer == "1":
        print("You selected Poker!")
        time.sleep(0.5)
        poker()
        
    elif answer == "2":
        print("You selected Slots!")
        time.sleep(0.5)
        start_slots()

    else:
        print("Invalid selection.")
        sys.exit(1)


""" Poker Mini """
final_hand = None
is_player_lost = False

def poker():
    print("Welcome to Mini Poker!, Beat the house if you can")
    print("How to Play: You can only win with STRAIGHT-FLUSH, THREE-OF-A-KIND, AND A PAIR")
    print("\n STRAIGHT-FLUSH -> highest win \n THREE-OF-A-KIND -> 2nd highest win \n PAIR -> Not a win but you did not lose\n")
    # Card representation with suits and ranks
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suits = ['Heart', 'Diamond', 'Club', 'Spade']

    # Global variables fr poker
    global is_player_lost, final_hand

    # Deck of cards in nested loop
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

    """ poker game loop """
    try:
        #print(deck[0], deck[1]) # hand these to the player on start
        print("Shuffling")
        time.sleep(1.5)
        hand_to_player = [deck[0], deck[1]]
        #hand_to_player = [(rank, emoji.emojize(suit, language="alias")) for rank, suit in hand_to_player]
        print(f"Player: , {hand_to_player}")

        #Program sleeps a little while dealing few more cards to player
        for _ in range(3):
            hand_to_player.append(deck.pop())

        # raise, call or flop
        player_call = input("\nPlease Select [r]aise OR [f]lop: ")
        if player_call == "r":
            #nxt_move = int(input("\nAmount to raise: "))
            print(f"Player chose to Raise")
            #if 200 <= nxt_move <= 500:
                #amount_on_table += nxt_move
            print("dealing...")
            time.sleep(2.5)
            print(win(hand_to_player))
            is_player_lost = False
        elif player_call == "f":
            is_player_lost = True
            print("Player flopped >>> Exiting the round")
            print(f"Final Hand: {hand_to_player}")
            print(f"House wins after showdown")
        else:
            raise ValueError("Value Error")
    # Error handling for invalid input or exit
    except (ValueError, KeyboardInterrupt) as e:
        if isinstance(e, KeyboardInterrupt):
            print("\nExiting Poker... Thanks for playing!")
        else:
            print("Invalid Input, Exiting Poker...")
            sys.exit(0)

    #final_hand = hand_to_player     #final 3 cards as in WSOP
    #print("Final Hand:\n ", hand_to_player)


def win(_hand_strength):
    global is_player_lost, final_hand

    final_hand = _hand_strength
    if is_straight_flush(final_hand):
        is_player_lost = False
        print(f"final_hand: {final_hand}\n Player wins with STRAIGHT FLUSH")
    if is_three_of_kind(final_hand):
        is_player_lost = False
        print(f"final_hand: {final_hand}\n Player wins with THREE-OF-A-KIND")
    if is_a_pair(final_hand):
        is_player_lost = False
        print(f"final_hand: {final_hand}\n Player is saved with a PAIR")
    elif not is_straight_flush(final_hand) or is_three_of_kind(final_hand) or is_a_pair(final_hand):
        is_player_lost = True
    else:
        is_player_lost = True
        print("Player Loses: Win did not Match any of the Winning Hands")


def is_straight_flush(_hand):
    # All cards are of the same suit
    suits = [card[1] for card in _hand]
    if len(set(suits)) != 1:
        return False

    # ranks consecutive
    ranks = [card[0] for card in _hand]
    rank_values = sorted([ranks.index(rank) for rank in ranks])
    for i in range(len(rank_values) - 1):
        if rank_values[i] + 1 != rank_values[i + 1]:
            return False

    return True

def is_three_of_kind(_hand):
    # use dict to check if rank will appear 3 times
    ranks = [card[1] for card in _hand]
    counts = {}
    for rank in ranks:
        if rank in counts:
            counts[rank] += 1
        else:
            counts[rank] = 1
    #  Occurences of rank 3 times
    for rank, count in counts.items():
        if count >= 3:
            return True
    return False

def is_a_pair(_hand):
    ranks = [card[1] for card in _hand]
    counts = {}
    for rank in ranks:
        if rank in counts:
            counts[rank] += 1
        else:
            counts[rank] = 1

    for rank, count in counts.items():
        if count == 2:
            return True
    return False

""" End of Poker Mini """

""" Slots Mini """
# slot machine variables
sl_player_bank = 200
sl_current_bet = 0
sl_total_won = 0
sl_total_lost = 0
hit_jackpot = False

# slot machine
def slot_machine():
    global sl_player_bank, sl_current_bet, sl_spin_count, sl_total_won, sl_total_lost

    if sl_player_bank == 0:
        print("Game Over!")
        return

    """ slots game loop """
    while sl_player_bank > 0:
        if sl_player_bank >= 5000:
            try:
                print("BIG SPENDER'S CLUB!!! >>> You are on FIRE!!!")
                bet = input("\n[ENTER] TO BET: \n")
                if bet == "":
                    actual_bet = int(input("STAKES INCREASED: PLACE YOUR BET! in [100, 200, 500]: "))
                    sl_current_bet = actual_bet
                    if actual_bet not in [100, 200, 500]:
                        slot_machine()
                elif bet == "Q":
                    sys.exit(0)
                else:
                    raise ValueError("Invalid input")

                if sl_player_bank >= actual_bet and actual_bet > 0:
                    #sl_player_bank -= actual_bet

                    print("\n-----SPINNING FOR: ${}-----\n".format(actual_bet))
                    #Simulating the slot machine spin and see the outcome
                    #Updating sl_total_won or sl_total_lost based on that outcome
                    print(slot_spinner())
                else:
                    return "Insufficient funds"
            except ValueError as e:
                pass
            except KeyboardInterrupt:
                print("\nExiting Slot Machine... Thanks for playing!")
                sys.exit(0)
        elif sl_player_bank >= 20000:
            try:
                bet = input("\n[ENTER] TO BET: \n")
                if bet == "":
                    print("HIGH ROLLERS STAKES! >>> You are a MENACE!!!")
                    actual_bet = int(input("STAKES INCREASED: PLACE YOUR BET! in [700, 1000, 2000]: "))
                    sl_current_bet = actual_bet
                    if actual_bet not in [700, 1000, 2000]:
                        slot_machine()
                elif bet == "Q":
                    sys.exit(0)
                else:
                    raise ValueError("Invalid input")

                if sl_player_bank >= actual_bet and actual_bet > 0:
                    #sl_player_bank -= actual_bet

                    print("\n-----SPINNING FOR: ${}-----\n".format(actual_bet))
                    #Simulating the slot machine spin and see the outcome
                    #Updating sl_total_won or sl_total_lost based on that outcome
                    print(slot_spinner())
                else:
                    return "Insufficient funds. Sorry Try again next Time!"
            except ValueError as e:
                pass
            except KeyboardInterrupt:
                print("\nExiting Slot Machine... Thanks for playing!")
                sys.exit(0)
        else:
            try:
                bet = input("\n[ENTER] TO BET: \n")
                if bet == "":
                    actual_bet = int(input("PLACE YOUR BET! in [25, 50, 100]: "))
                    sl_current_bet = actual_bet
                    if actual_bet not in [25, 50, 100]:
                        slot_machine()
                if sl_player_bank >= actual_bet and actual_bet > 0:
                    #sl_player_bank -= actual_bet

                    print("\n-----SPINNING FOR: ${}-----\n".format(actual_bet))
                    #Simulating the slot machine spin and see the outcome
                    #Updating sl_total_won or sl_total_lost based on that outcome
                    print(slot_spinner())
            except (ValueError, IndexError, EOFError) as e:
                raise e
            except KeyboardInterrupt:
                print("\nExiting Slot Machine... Thanks for playing!")
                sys.exit(0)

#Slot machine spinner or spin wheel?!
def slot_spinner():
    global sl_player_bank, sl_current_bet, sl_total_won, sl_total_lost, hit_jackpot
    # Use dict to store symbols and replace for nums
    #REMEMBER: change symbols to emojis later, or emojize lib them
    symbols = {
        1: ":cherries:",
        2: ":lemon:",
        3: ":orange:",
        4: ":red_heart:",
        5: ":bell:",
        6: ":trophy:",
        7: ":slot_machine:",
        8: ":gem_stone:",
        9: ":money_bag:",
        10: ":star:"
    }
    
    try:
        # using reels and randint to simulate the winning odds
        reel1 = random.randint(1, 10)
        reel2 = random.randint(1, 10)
        reel3 = random.randint(1, 10)

        # Mapping the numbers to symbols
        symbol1 = symbols[reel1]
        symbol2 = symbols[reel2]
        symbol3 = symbols[reel3]
        print(f"Reels: >>> | {symbol_emojizer(symbol1)}", end=" ")
        time.sleep(0.4)
        print(f"| {symbol_emojizer(symbol2)}", end=" ")
        time.sleep(0.4)
        print(f"| {symbol_emojizer(symbol3)} | <<<\n")

        if symbol1 == symbol2 == symbol3:
            hit_jackpot = True
            sl_total_won += 200000
            sl_player_bank += sl_total_won
            print(f"WIN: ${sl_total_won} >>Jackpot!!<<")
            print(f"Current Bank Balance: {sl_player_bank}")
            return
        elif symbol1 in (symbol2, symbol3) or symbol2 == symbol3:
            #making the winnings for at leat 2 reels
            #equal to at least 25 percent of the winning total multiplied
            #by the player's bet
            # winning total set to 100 by default
            sl_total_won = 0.25 * 100 * sl_current_bet
            sl_player_bank += sl_total_won
            hit_jackpot = False
            print(f"WIN: ${sl_total_won}")
            print(f"Total Won: ${sl_total_won} | Total Lost: ${sl_total_lost} \nCurrent Balance: ${sl_player_bank}")
        else:
            sl_total_lost += sl_current_bet
            sl_player_bank -= sl_current_bet
            hit_jackpot = False
            print(f"Loss: ${sl_total_lost}")
            print("--------------------TRY AGAIN :(------------------------")
            print(f"Current Balance: ${sl_player_bank}")
            pass
        if sl_player_bank >= 250000:
            print("\nYou have reached the Jackpot Amount! WELL DONE!!")
            sys.exit(0)
    except ValueError:
        pass

""" Some helper fucntions """
# Emojize symbols in slots
def symbol_emojizer(symbol):
    try:
        new_text = emoji_dictionary.get(symbol, symbol)
        return emoji.emojize(f"{new_text}", language="alias", variant="emoji_type")
    except (TypeError, ValueError):
        pass
    return None

# Games Entry function
def casino_entry():
    print("Welcome to Casino-Mini, Choose a Game to play\n")
    #name = input("Please Enter your name: ").strip().capitalize()
    time.sleep(1)

#Start slots function if player chose to play slots
def start_slots():
    global sl_player_bank
    print("Welcome to Mini Slots!, Here's $200 to get started\n")

    prompt = input("Press [S] to START, [Q] to Quit Game: ")
    if prompt == "S":
        sl_player_bank == 200
        slot_machine()
    elif prompt == "Q":
        print("Thanks for stopping by :D")
        casino_entry()


# Run main
if __name__ == "__main__":
    main()
