"""
Write a program that determines the name of a shape from its number of sides. 
Read the number of sides from the user and then report the appropriate name as part of a meaningful message. 
Your program should support shapes with anywhere from 3 up to (and including) 10 sides. 
If a number of sides outside of this range is entered then your program should display an appropriate error message.
"""

# 3 sides = triangle
# 4 sides = square
# 5 sides = pentagon
# 6 sides = hexagon
# 7 sides = heptagon
# 8 sides = octagon
# 9 sides = nonagon
# 10 sides = decagon

#make multidimensional array with shape names and number of sides
shapes = [["triangle", 3], ["square", 4], ["pentagon", 5], ["hexagon", 6], ["heptagon", 7], ["octagon", 8], ["nonagon", 9], ["decagon", 10]]

# 1. Ask the user for the number of sides
sides = int(input("Enter the number of sides: "))

# 2. Determine the name of the shape
if 3 <= sides <= 10:
    for shape in shapes:
        if shape[1] == sides:
            print("The shape with", sides, "sides is a", shape[0])

# 3. Display the result
else:
    print("Error: number of sides must be between 3 and 10")
