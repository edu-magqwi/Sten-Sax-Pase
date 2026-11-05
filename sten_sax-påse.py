import random as rand
svar = None
while svar != "n":
    print("Nu ska vi spela sten, sax eller påse!\nJag är python 311")


    namn = input("Ange ditt spelarnamn -> ")
    omgångar = int(input("Ange antal omgångar som vi ska spela -> "))
    for i in omgångar:
        botval = rand.randint(1, 3)

    print(f"Spelomgång {i} /n -----------------------")

    val = str(input("välj sten, sax eller påse "))
    if val != "sten" or "sax" or "påse":9
        print("ogiltigt val, välj igen")