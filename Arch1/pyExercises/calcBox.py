#Maak een programma dat als input een lengte, breedte en diepte vraagt en 
# het volume van een doos berekent. print deze volume uit in console

# Ask the user to enter the length, width and height of a box.
length = float(input("Enter the length of the box: "))
width = float(input("Enter the width of the box: "))
height = float(input("Enter the height of the box: "))

# Calculate the volume of the box.
volume = length * width * height

# Display the volume of the box.
print("The volume of the box is", volume)
