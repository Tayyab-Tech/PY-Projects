import random

computer = ["rock","paper","scissor"]

winner = lambda user,comp:(
    "Tie" if user == comp else
    "You win" if (user == "rock" and comp == "scissor") or 
                (user == "paper" and comp == "rock") or
                (user == "scissor" and comp == "paper")
     else "Computer wins"
)

user = input("Enter Rock, Paper, Scissor : ").lower()
comp = random.choice(computer)

print(f"\n You chose {user} and computer chose {comp}")
print("  ",winner(user,comp))