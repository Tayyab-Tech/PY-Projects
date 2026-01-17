# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module

from random import randint 
n = randint(1,100)
user = -1
gusses = 1
while (user != n):
    user = int(input("Guess the number between 1 to 100 : "))
    if(user>n):
        print("Lower number plz")
        gusses += 1
    elif(user<n):
        print("Higher number plz")
        gusses += 1

print(f"You Guess the number {n} correctly in {gusses} attempts")
