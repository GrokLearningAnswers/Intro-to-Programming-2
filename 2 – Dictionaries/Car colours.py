cars = {}
userInput = input("Car: ")
while userInput:
  if userInput in cars:
    cars[userInput] = cars[userInput] + 1
  else:
    cars[userInput] = 1
  userInput = input("Car: ")
for i, j in cars.items():
  print(f"Cars that are {i}: {j}")