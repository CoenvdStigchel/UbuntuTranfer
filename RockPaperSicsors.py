import random

while True:
    user = input("Enter a choice (steen, papier, schaar): ")
    keuzes = ["steen","steen","steen", "papier","papier","papier", "schaar","schaar","schaar"]
    computer= random.choice(keuzes)
    if not user.lower() in ["steen", "papier", "schaar"]:
        print("Is geen optie")
        continue
    print(f'\nJij kiest >> {user}, computer koos >> {computer}.\n')

    if user == computer:
        print(f"Allebei de spelers gebruikte {user}. Ooh een gelijkspel!")
    elif user == "steen":
        if computer == "schaar":
            print("Steen wint van schaar! Je hebt Gewonnen!")
        else:
            print("Paper wint van rock! Je hebt Gewonnen!")
    elif user == "papier":
        if computer == "steen":
            print("Papier wint van steen! Je hebt Gewonnen!")
        else:
            print("schaar wint van papier! Je hebt Verloren...")
    elif user == "schaar":
        if computer == "papier":
            print("Schaar wint van  papier! Je hebt Gewonnen!")
        else:
            print("Steen wint van schaar! Je hebt Verloren...")
       

    if input("Wil je nog een keer spelen Y/N >> ") == "y":
        continue
    else:
        exit()






