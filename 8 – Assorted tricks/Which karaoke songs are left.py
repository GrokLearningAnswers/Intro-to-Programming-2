songlist = []
with open('songlist.txt') as f:
  file = f
  for i in file:
    x, y = i[:-1].split(', ')
    songlist.append((x,y))

songlist.reverse()
count = 0
amount = int(input("How many more songs? "))
for x, y in songlist:
  print(f"{x}, {y}")
  count+=1
  if count == amount:
    break