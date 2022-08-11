currentFloor = int(input("Current floor: "))
destinationFloor = int(input("Destination floor: "))
floors = list(range(currentFloor, destinationFloor + 1))
for i in floors:
  print(f"Level {i}")