'''
# Rock-Paper-Scissors Game

Code a game of rock paper scissors.

## Instructions

* take in a number 0-2 from the user that represents their hand
* generate a random number 0-2 to use for the computer's hand
* call the function `get_hand` to get the string representation of the user's hand
* call the function `get_hand` to get the string representation of the computer's hand
* call the function `determine_winner` to figure out who won
* print out the player hand and computer hand
* print out the winner

## Some Tips

Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

```

python
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass
```

'''

import random
again = 'y'

def get_hand(hand):
    if hand < 0 or hand > 2:
        print("Number out of range!!")
        quit()
    # 0 = scissors, 1 = rock, 2 = paper
    options = ['scissors', 'rock', 'paper']
    return options[hand]

def determine_winner(player, computer):
    if player == computer:
        return 'TIE'
    elif player == 'scissors' and computer == 'rock':
        return 'Computer'
    elif player == 'scissors' and computer == 'paper':
        return 'Player'
    elif player == 'rock' and computer == 'paper':
        return 'Computer'
    elif player == 'rock' and computer == 'scissors':
        return 'Player'
    elif player == 'paper' and computer == 'scissors':
        return 'Computer'
    elif player == 'paper' and computer == 'rock':
        return 'Player'

while again.lower() == 'y':
    print("0 = scissors, 1 = rock, 2 = paper")
    player_num = int(input("Enter a number (0, 1 or 2): "))
    comp_num = random.randint(0, 2)

    player_hand = get_hand(player_num)
    comp_hand = get_hand(comp_num)

    print(f"Player hand: {player_hand}")
    print(f"Computer hand: {comp_hand}")

    print(f"Winner is: {determine_winner(player_hand, comp_hand)}")
    again = input("Play again? (y / n) : ")
