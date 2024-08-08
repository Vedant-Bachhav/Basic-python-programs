# creating a stone paper scissor game.

print("Welcome to stone paper scissor game!!\n\n") 

player_name=input("Player name: \n\n")

print(">>>>>>>>>>>>>>>",player_name,"VS computer!!! <<<<<<<<<<<<<<<< \n\n")

print("INSTRUCTIONS ONLY USE: stone, paper, scissor \n\n")


# choosing difficulty

print("Choose level: easy, medium, hard")

level= input("enter level: ")


if player_name=="Vedant" or player_name=="vedant" or player_name=="VEDANT":
    user_move=input("YOUR TURN: ")

    if user_move=="stone":
        print("i had chosen scissor")
        print("YOU WON!!")
        
    elif user_move=="paper":
        print("i had chosen stone")
        print("YOU WON!!")
        
    elif user_move=="scissor":
        print("i had chosen paper")
        print("YOU WON!!")



if level=="easy":
    import random
    choices = ["stone", "paper", "scissor"]
    computer_move = random.choice(choices)

    user_move=input("YOUR TURN: ")

    if user_move=="stone" and computer_move=="scissor":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="stone" and computer_move=="paper":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    elif user_move=="paper" and computer_move=="stone":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="paper" and computer_move=="scissor":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    elif user_move=="scissor" and computer_move=="paper":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="scissor" and computer_move=="stone":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    
    elif user_move==computer_move:
        print(" It's a DRAW")
        print("i had chosen: ",computer_move )

    else:
        print("please type correct spelling, \n follow instructions")




elif level=="medium":
    import random
    choices = ["stone", "paper", "scissor"]
    computer_move = random.choice(choices)

    user_move=input("YOUR TURN: ")

    if user_move=="stone" and computer_move=="scissor":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="stone" and computer_move=="paper":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    elif user_move=="paper" and computer_move=="stone":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="paper" and computer_move=="scissor":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    elif user_move=="scissor" and computer_move=="paper":
        print("YOU WON!!")
        print("i had chosen: ",computer_move )

    elif user_move=="scissor" and computer_move=="stone":
        print("YOU LOSE, COMPUTER WINS")
        print("i had chosen: ",computer_move )

    
    elif user_move==computer_move:
        print(" It's a DRAW")
        print("i had chosen: ",computer_move )

    else:
        print("please type correct spelling, \n follow instructions")




elif level=="hard":
    user_move=input("YOUR TURN: ")

    if user_move=="stone":
        print("i had chosen paper")
        print("you lose computer wins!")
        
    elif user_move=="paper":
        print("i had chosen scissor")
        print("you lose computer wins!")
        
    elif user_move=="scissor":
        print("i had chosen stone")
        print("you lose computer wins!")

    else:
        print("please type correct spelling, \n follow instructions")




else:
    print("please type correct spelling, \n follow instructions")