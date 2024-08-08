# using random module to generate dice output

import random
outcomes = [1,2,3,4,5,6]
final_outcome = random.choice(outcomes)

print("the dice was rolled, it shows: ", final_outcome)