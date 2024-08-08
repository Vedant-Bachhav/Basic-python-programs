# this program uses random module to select the order of batsmen

print("Welcome to the program!!")

print('''____________INSTRUCTIONS___________ 
      this program takes input from 2 to 10 and randomly puts the order of players''')

print("Below enter the number of players")

number_players=int(input("Enter the number[2 to 10]: "))

import random

if number_players==1:
    print("Atleast 2 players required, Try again!!")

elif number_players==2:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    players= [p1,p2]
    
    players= [p1,p2]
    random.shuffle(players)
    print(players)

elif number_players==3:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    
    
    players= [p1,p2,p3]
    random.shuffle(players)
    print(players)
     
elif number_players==4:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    
    
    players= [p1,p2,p3,p4]
    random.shuffle(players)
    print(players)

elif number_players==5:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
   
    
    players= [p1,p2,p3,p4,p5]
    random.shuffle(players)
    print(players)

elif number_players==6:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
    p6=input("Enter player name: ")
  
    
    players= [p1,p2,p3,p4,p5,p6]
    random.shuffle(players)
    print(players)

elif number_players==7:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
    p6=input("Enter player name: ")
    p7=input("Enter player name: ")
    
    
    players= [p1,p2,p3,p4,p5,p6,p7]
    random.shuffle(players)
    print(players)

elif number_players==8:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
    p6=input("Enter player name: ")
    p7=input("Enter player name: ")
    p8=input("Enter player name: ")
   
    
    players= [p1,p2,p3,p4,p5,p6,p7,p8]
    random.shuffle(players)
    print(players)

elif number_players==9:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
    p6=input("Enter player name: ")
    p7=input("Enter player name: ")
    p8=input("Enter player name: ")
    p9=input("Enter player name: ")
   
    
    players= [p1,p2,p3,p4,p5,p6,p7,p8,p9]
    random.shuffle(players)
    print(players)

elif number_players==10:
    p1=input("Enter player name: ")
    p2=input("Enter player name: ")
    p3=input("Enter player name: ")
    p4=input("Enter player name: ")
    p5=input("Enter player name: ")
    p6=input("Enter player name: ")
    p7=input("Enter player name: ")
    p8=input("Enter player name: ")
    p9=input("Enter player name: ")
    p10=input("Enter player name: ")
    
    players= [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
    random.shuffle(players)
    print(players)
     
else:
    print("PLEASE FOLLOW INSTRUCTIONS \n ______TRY AGAIN______")