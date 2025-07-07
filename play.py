from card import * 
import random

score1 = 0
score2 = 0
round = 1

while score1 < 2 and score2 < 2:
    print(f"\n --- Round {round} ---")

    card1, card2 = random.sample(deck, 2)

    print(f"Player 1 plays: {card1}")
    print(f"Player 2 plays: {card2}")

    result = card1.beats(card2)
    if result == "Win":
        print("Player 1 wins the round!")
        score1 += 1
    elif result == "Lose":
        print("Player 2 wins the round!")
        score2 += 1
    else:
        print("It's a tie!")

    print(f"Score: Player 1 - {score1} | Player 2 - {score2}")
    round += 1

print("\n ### Game Over! ###")
if score1 == 2:
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")
