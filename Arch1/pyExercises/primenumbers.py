#De gebruiker wil weten of er priemgetallen tussen 0 en dat getal zitten. Het programma vraagt daarom om een nummer van een gebruiker en 
#gaat langs alle nummers tot en met het ingevoerde nummer van de gebruiker. De input en output ziet er als volgt uit: 

x = int(input("Enter a number: "))

#print all prime numbers beteween 0 and x input
for num in range(0, x + 1):
    #Als nummer hoger is dan 1 doe dan
    if num > 1:
        #for loop in range 2 -> num
        for i in range(2, num):
            #Als num % i == 0 dan break
            if (num % i) == 0:
                break
        else:
            #print nummers 
            print(num)

