import random

user = input("Enter a choice (rock, paper, scissors): ")
keuzes = ["rock", "paper", "scissors"]
computer= random.choice(keuzes)
print(f'\nJij kiest >> {user}, computer koos >> {computer}.\n')

if user == computer:
    print(f"Both players selected {user}. Ooh een gelijkspel!")
elif user == "rock":
    if computer == "scissors":
        print("Rock wint van scissors! Je hebt Gewonnen!")
    else:
        print("Paper verliest van rock! Je hebt verloren...")
elif user == "paper":
    if computer == "rock":
        print("Paper wint van rock! Je hebt Gewonnen!")
    else:
        print("Scissors cuts paper! Je hebt Verloren...")
elif user == "scissors":
    if computer == "paper":
        print("Scissors wint van  paper! Je hebt Gewonnen!")
    else:
        print("Rock wint van scissors! Je hebt Verloren...")

if not user.lower() in ["rock", "paper", "scissors"]:
    print("Is geen optie")