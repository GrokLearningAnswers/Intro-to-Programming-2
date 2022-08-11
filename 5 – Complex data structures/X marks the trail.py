gridSize = int(input("Grid size: "))
grid = []
for i in range(gridSize):
  row = []
  for j in range(gridSize):
    row.append(".")
  grid.append(row)
grid[0][0] = "x"
for i in grid:
  print(''.join(i))
direction = input("Direction: ")
loc = [0,0]
while direction:
  if direction == "up":
    loc[1] += -1
  elif direction == "down":
    loc[1] += 1
  elif direction == "left":
    loc[0] += -1
  elif direction == "right":
    loc[0] += 1
  grid[loc[1]][loc[0]] = "x"
  for i in grid:
    print(''.join(i))
  direction = input("Direction: ")