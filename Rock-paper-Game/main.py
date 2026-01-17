# PROJECT  1: Rock , Paper , Scissor GAME  
# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user. 

'''
-1 == Rock
0 == Paper
1 == Scissor
'''
import random
computer = random.choice([-1,0,1])
print("R for Rock, P for Paper and S for Scissor.")
userinput = input("Enter your choice : ")
userdict = {
    "s":1,
    "S":1,
    "p":0,
    "P":0,
    "r":-1,
    "R":-1        
            }
reverseuserdict = {
    1 : "Scissor",
    0 : "Paper",
    -1 : "Rock"  
            }
if userinput in userdict:
    user = userdict[userinput]
    print(f"You select {reverseuserdict[user]} and computer selected {reverseuserdict[computer]}")
    if (computer == user):
        print("It's Draw!!!!")
    else:
        if ((computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1)):
            print("Computer Wins!!!")
        else:
            print("You wins!!!!")
else:
    print("You Entered the wrong command....")