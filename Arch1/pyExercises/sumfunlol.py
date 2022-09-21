# Bank 1 krijgt 5% per jaar ; Bank 2 krijgt 10 euro per jaar; Hoeveel jaar kost het om twee keer zoveel te krijgen als b1 of b2

bankAccount1 = 100
bankAccount2 = 100 

years = 0

run = True

while run:
    years += 1

    bankAccount1 += bankAccount1 / 100 * 5 
    bankAccount2 += 10

    #if a number is twice as big stop loop
    if bankAccount1 >= bankAccount2 * 2 or bankAccount2 >= bankAccount1 * 2:
        run = False
        print("Antwoord: ",years)
        print("Bank1 10 euro p/year : ",int(bankAccount1), " | " ,  "Bank1 10 euro 5 percent : ", bankAccount2)
