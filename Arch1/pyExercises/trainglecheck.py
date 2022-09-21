"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. 
All 3 sides of an equilateral triangle have the same length. 
An isosceles triangle has two sides that are the same length, and a third side that is a different length. 
If all of the sides have different lengths then the triangle is scalene. 

Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.
"""

#Get inputs
x1 = int(input("Triangle lenght 1: "))
x2 = int(input("Triangle lenght 2: "))
x3 = int(input("Triangle lenght 3: "))

if x1 == x2 == x3:
    print("equilateral")
elif x1 == x2 or x3 == x1 or x3 == x2:
    print("isosceles")
else:
    print("scalene")
