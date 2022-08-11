text = open("orders.txt")
for line in text:
  print(line.strip().upper())