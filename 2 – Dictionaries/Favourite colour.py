nameAndColour = {}
userInput = input("Name and colour: ")
while userInput:
  splitUserInput = userInput.split()
  name = splitUserInput[0]
  colour = splitUserInput[1]
  nameAndColour[name] = colour
  userInput = input("Name and colour: ")
for i, j in nameAndColour.items():
  print(i, j)