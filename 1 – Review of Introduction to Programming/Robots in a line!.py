line = input("Line: ")
splitLine = line.split()
possibleRobot = False
for i in splitLine:
  if i == "robot":
    print("There is a small robot in the line.")
    possibleRobot = True
  elif i == "ROBOT":
    print("There is a big robot in the line.")
    possibleRobot = True
  elif i.lower() == "robot":
    print("There is a medium sized robot in the line.")
    possibleRobot = True
if possibleRobot == False:
  print("No robots here.")