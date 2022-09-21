"""
Positions on a chess board are identified by a letter and a number. 
Usually, the letter identifies the column, while the number identifies the row. 
Write a program that reads a position from the user. 
The program should determine if the column begins with a black square or a white square. 
Then use modular arithmetic (check if you know this concept) to report the color of the square in that row. 
For example, if the user enters a1 then your program should report that the square is black. 
If the user enters d5 then your program should report that the square is white. 
Your program may assume that a valid position will always be entered. 
It should report proper error message in case on invalid input values.
"""
import re
#Positions are identified by letter and number

#letter = column , number = row
q1 = input("Enter a square you want to investigate (ex.a1): ")

#check if string length is gud else stop
if re.match("[a-h]+[1-8]", q1[0:2]) and len(q1) == 2:
    if(ord(q1[0]) % 2 == int(q1[1]) % 2):
        print(f"Position of {q1} is black")
    else: 
        print(f"Position of {q1} is white")

else:
    print("Wrong input please enter the coords as example !")    


    



