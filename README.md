# CASINO MINI

## Description

Welcome to Casino Mini! - You can play one out of the two games. Upon entering, Player is presented with two choices,

   1. Mini Poker
   2. Mini Slots.

Mini Poker - Play against the house/bot and be proud of beating the house, this game is not money focused but only a fun game for Player(s) to test their resilience against the formidable house - mini adaptation of WSOP, just not money focused.

   ```python
      print("Welcome to Mini Poker!, Beat the house if you can")
      print("How to Play: You can only win with STRAIGHT-FLUSH, THREE-OF-A-KIND, AND A PAIR")
      print("\n STRAIGHT-FLUSH -> highest win \n THREE-OF-A-KIND -> 2nd highest win \n PAIR -> Not a win but you did not lose\n")
   ```

The dealer will first hand you two cards, then ask you if you would like to [R]aise or [F]lop, raise just means ot keep playing and flop implies quitting. If you choose to raise, then dealer shuffles and hand you the rest of the remaining three cards and it is then win is decided and how.

   ```python
      print("Shuffling")
      time.sleep(1.5)
      hand_to_player = [deck[0], deck[1]]
      print(f"Player: , {hand_to_player}")
   ```

Using some helper functions to create customized wins:

   ```python
      def is_a_pair(): Declares a pair, saving player to not lose

      def is_three_of_kind(): The 2nd highest win

      def is_straight_flush(): The highest win
   ```

   The win strategy functions are custom and adjusted to the structure, implementation and goal of this mini game series.

Player must win by having a hand that matches any one of the winning hands, otherwise the game exists with:

   ```python
      Player Loses: Win did not Match any of the Winning Hands
   ```

Mini Slots - Slots are fun, a way to spend less cash as possible. In these slots you get a starting amount of $200, as the game begins you are to place a bet from your $200 in the format [25, 50, 100] or slots will read "Invalid Value" if not prompt you to enter a valid amount, your winning chances will depend on the Algorithm logic - which is random.

   ```python
      #the winnings for 2 reels ,match
      #equal to at least 25 percent of the winning total multiplied
      #by the player's bet
      # winning total set to 100 by default
      sl_total_won = 0.25 * 100 * sl_current_bet
   ```

If lucky and end up winning an amount greater than 2000, then the betting stakes change from [25, 50, 100] to [ 100, 200, 500] giving you more chances to win even more, or well... lose.

The Jackpot is 250 000, meaning you have beaten the House.

As aforementioned, the reels outcome is random.Using a List to create symbols then created a function that will turn symbols into Emojis using the emoji library. !([Emoji library](https://pypi.org/project/emoji/))

   ```python
      def symbol_emojizer(symbol):
         try:
            new_text = emoji_dictionary.get(symbol, symbol)
            return emoji.emojize(f"{new_text}", language="alias", variant="emoji_type")
   ```

### Installation and Usage

Run these commads, in this order.

```bash
git clone https://github.com/katGhost/casino-mini.git
```

then

```bash
cd casino-mini
```

Create and Activate the virtual envirnoment inside of the project folder.

```bash
python -m venv venv

source venv/Scripts/activate
```

Install the required dependencies in order to run this program.

```bash
pip install -r requirements
```

RUN:

```bash
   python project.py
```

#### AUTHOR: ANDRIES N. MOGASHOA
