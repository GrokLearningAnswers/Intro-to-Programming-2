with open("input.txt") as f:
  count = 1
  file = f.read().strip().lower().split("\n")
  for i in file:
    if i.count('a') >= 3 and i.count('r') >= 2 and i.count('d') >= 1 and i.count('v') >= 1 and i.count('k') >= 1:
      print(f"Aardvark on line {count}")
    count += 1