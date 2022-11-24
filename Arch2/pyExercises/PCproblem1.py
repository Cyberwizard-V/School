# Er is een dictionary die vol zit met kamers van een woning en
# hoeveel vierkante meters elke kamer heeft (dictionary is hieronder te kopiëren).
# De gebruiker wilt meerdere kamers selecteren en dan de totale
# vierkante meters krijgen van de geselecteerde kamers bij elkaar.
data = []
while True:
    rooms = {
        "living room": 20,
        "kitchen": 8,
        "master bedroom": 18,
        "children's bedroom": 14,
        "basement": 6,
        "attic": 23,
        "hallway": 4
    }
    for key in rooms:
        print(key)
    userInput = input("Selecteer je kamer ex.(living room) : ")
    data.append(rooms[userInput])
    total = sum(data)
    print("De totale vierkante meters zijn: ", total)
    userInput2 = input("Wil je meer kamers selecteren? (Y/N): ")
    if userInput2 == "N":
        print(data)
        break
