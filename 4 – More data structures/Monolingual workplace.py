line1 = input("Line: ").split()
mainSet = set(line1[1:])
lineOther = input("Line: ").split()
while lineOther:
  tempSet = set(lineOther[1:])
  mainSet = mainSet - tempSet
  lineOther = input("Line: ").split()
if mainSet:
  for temp in mainSet:
    print(temp, "is monolingual.")
else:
  print("Everyone is multilingual!")