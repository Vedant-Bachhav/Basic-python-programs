

# using random function to play a toss

import random

coin_move = ["heads", "tails"]
move_generated = random.choice(coin_move)

print("the coin was tossed, result is: ", move_generated)