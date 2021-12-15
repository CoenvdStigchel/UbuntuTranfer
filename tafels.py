def toonTafel(getal : int ):
    for i in range(1,11):
        print(f"{i} x {getal} = " + str(i*getal))

tafel = int(input("Van welke getal wil je de tafel zien? "))

toonTafel(tafel)