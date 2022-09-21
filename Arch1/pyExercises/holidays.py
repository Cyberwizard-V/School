"""
Make a list of national holidays in The Netherlands (assume current year). 
Write a program that reads a month and day from the user. 
If the month and day match one of the holidays in the list then your program should display the holiday’s name. 
Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
"""
#make list of holidays
holidays = [["Nieuwjaarsdag", 1, 1], ["Koningsdag", 4, 27], ["Bevrijdingsdag", 5, 5], ["Hemelvaartsdag", 5, 30], ["Pinksteren", 6, 9], ["Kerstmis", 12, 25]]

inpUser = int(input("Enter a month: "))
inpUser2 = int(input("Enter a day: "))

#check if input is in list
for holiday in holidays:
    if holiday[1] == inpUser and holiday[2] == inpUser2:
        print("The holiday is", holiday[0])
        break
else:
    print("No holiday found")
    


    