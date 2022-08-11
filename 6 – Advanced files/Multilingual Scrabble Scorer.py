points = {}
with open('scrabble_letters.txt') as f:
  file = f.read().split('\n')[:-1]
  for i in file:
    j, k = i.split()
    points[k] = j
word = input("Word: ")
total = 0
for j in word:
  i = j.upper()
  if i in points:
    total += int(points[i])
print(total, "points")