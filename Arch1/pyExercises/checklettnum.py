#Get the length then check if there is digits
y = 0
x = 0

inputUser = input("String: ")
for char in inputUser:
  if char.isdigit():
    x += 1
  elif char.isalpha():
    y += 1

print("Numbers: ", x)
print("letters: ", y)