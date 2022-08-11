bigrams = {}

userInput = input("Line: ")
while userInput:
  tempList = userInput.strip().lower().split()
  count = 1
  for i in tempList:
    if i!= tempList[-1]:
      tempKey = f"{i} {tempList[count]}"
      bigrams[tempKey] = bigrams.get(tempKey, 0) + 1
      count += 1
  userInput = input("Line: ")
for i, j in bigrams.items():
  if j >= 2:
    print(f"{i}: {j}")