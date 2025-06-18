import random
print("Welcome to a game of rock, paper, or scissors against the computer!")
numRounds = input("How many rounds do you want to play: ")
choices = ["rock","paper","scissors"]
userWinCount = 0
compWinCount = 0
for i in range(int(numRounds)):
    randChoice = random.randint(0,2)
    compChoice = choices[randChoice]
    userChoice = input("Rock, paper or scissors: ")

    if compChoice == "rock":
        if userChoice == "paper":
            print("You win this round! The computer chose " + compChoice)
            userWinCount += 1
        elif userChoice == "scissors":
            print("The computer picked " + compChoice + " and won this round!")
            compWinCount += 1
        else:
            print("You tied with the computer!")
    elif compChoice == "paper":
        if userChoice == "rock":
            print("The computer picked " + compChoice + " and won this round!")
            compWinCount += 1
        elif userChoice == "scissors":
            print("You win this round! The computer chose " + compChoice)
            userWinCount += 1
        else:
            print("You tied with the computer!")

    elif compChoice == "scissors":
        if userChoice == "rock":
            print("You win this round! The computer chose " + compChoice)
            userWinCount += 1
        elif userChoice == "paper":
            print("The computer picked " + compChoice + " and won this round!")
            compWinCount += 1
        else:
            print("You tied with the computer!")

print("-------------------------------------------------------------")
print("Your score: " + str(userWinCount))
print("Computer score: " + str(compWinCount))
if userWinCount > compWinCount:
    print("You won overall!")
elif userWinCount == compWinCount:
    print("You both tied!")
else:
    print("The computer won overall!")
