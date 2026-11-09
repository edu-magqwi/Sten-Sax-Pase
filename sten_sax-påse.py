import random as rand  # Importerar random-modulen för att datorn ska kunna göra slumpmässiga val

# Skapar variabler för att hålla reda på poängen
spelare_poang = 0
dator_poang = 0

# Skriver ut spelets välkomstmeddelande
print("Nu ska vi spela sten, sax eller påse!")
print("---------------------------------------")

# Frågar efter spelarens namn och sparar det i variabeln spelare
spelare = input("Ange ditt spelarnamn -> ")

# Frågar hur många spelomgångar som ska spelas
omgangar = int(input("Ange antal spelomgångar -> "))

# Startar en loop som upprepar spelet så många gånger som spelaren har valt
for i in range(1, omgangar + 1):

    # Skriver ut vilken spelomgång som pågår
    print(f"\nSpelomgång {i}")
    print("----------------")

    # Frågar spelaren om den vill välja sten, sax eller påse
    # capitalize() gör att första bokstaven blir stor och resten små
    val = input("Välj 'Sten', 'Sax' eller 'Påse' -> ").capitalize()

    # Kontrollerar att spelarens val är giltigt
    # Om valet är fel får spelaren försöka igen tills ett giltigt val anges
    while val not in ["Sten", "Sax", "Påse"]:
        val = input("Välj 'Sten', 'Sax' eller 'Påse' -> ").capitalize()

    # Datorn väljer slumpmässigt mellan sten, sax och påse
    botval = rand.choice(["Sten", "Sax", "Påse"])

    # Skriver ut spelarens och datorns val
    print(f"{spelare} spelar: {val}")
    print(f"Python311 spelar: {botval}")

    # Kontrollerar om spelaren och datorn har valt samma sak
    # Om de har det blir spelomgången oavgjord och ingen får poäng
    if val == botval:
        print(f"\nVinnare i spelomgång {i}: Oavgjort!")

    # Kontrollerar om spelaren har vunnit omgången
    # Sten vinner över sax, sax vinner över påse och påse vinner över sten
    elif (val == "Sten" and botval == "Sax") or \
         (val == "Sax" and botval == "Påse") or \
         (val == "Påse" and botval == "Sten"):

        # Skriver ut att spelaren vann och ökar spelarens poäng med 1
        print(f"\nVinnare i spelomgång {i}: {spelare}!")
        spelare_poang += 1

    # Om inget av ovanstående villkor stämmer har datorn vunnit
    else:
        # Skriver ut att datorn vann och ökar datorns poäng med 1
        print(f"\nVinnare i spelomgång {i}: Python311!")
        dator_poang += 1


# När alla spelomgångar är klara skrivs slutresultatet ut
print("\nSLUTRESULTAT")
print("============")

# Kontrollerar om spelaren har fått fler poäng än datorn
if spelare_poang > dator_poang:

    # Skriver ut spelarens poäng först eftersom spelaren har vunnit
    print(f"{spelare}: {spelare_poang}p")
    print(f"Python311: {dator_poang}p")
    print(f"\n{spelare} vann spelet!")

# Kontrollerar om datorn har fått fler poäng än spelaren
elif dator_poang > spelare_poang:

    # Skriver ut datorns poäng först eftersom datorn har vunnit
    print(f"Python311: {dator_poang}p")
    print(f"{spelare}: {spelare_poang}p")
    print("\nPython311 vann spelet!")

# Om ingen har fler poäng än den andra blir hela spelet oavgjort
else:
    # Skriver ut poängen när båda har lika många poäng
    print(f"{spelare}: {spelare_poang}p")
    print(f"Python311: {dator_poang}p")
    print("\nOavgjort!")

# Skriver ut ett meddelande som visar att programmet har avslutats
print("Programmet avslutades normalt")


