# Opdracht Append To Dictionary 

# Maak een programma waarbij de gebruiker meerdere keren gevraagd wordt om een key en een value te geven 
# (tot een stop tegen zoals niks invoeren of ‘quit’. Iets anders mag natuurlijk ook). 
# Vervolgens doet het programma een functie call met drie parameters; 
# een key, een value en een default parameter value die niet wordt meegegeven in de functie call “dictionary = {}”.  

# Deze parameter met default value blijft niet leeg en wanneer de functie meerdere keren is aangeroepen zal de dictionary ook groter worden. 

# De functie gaat vervolgens de nieuwe key value pair toevoegen aan de dictionary en print het uit. Zorg ervoor dat het programma niet over al bestaande keys heen schrijft. 


# Hier een voorbeeld met de functie parameters: 

# def appendDictionary(key, value, dictionary = {}): 

def appendDictionary(key, value, dictionary = {}):
    if key in dictionary:
        print("Loser") 
    else:
        dictionary[key]=value
    print(dictionary)

print(f"""
---------------- ADD TO DICTIONARY ----------------

    """)
while True:
    userInput1 = input("Key: ")
    userInput2 = input("Value: ")
    appendDictionary(userInput1, userInput2)
    userInput2 = input("Wil je meer toevoegen aan je dic (Y/N): ")
    if userInput2 == "N":
        break   