words = {}
userInput = input("Enter line: ")
while userInput:
  splitUserInput = userInput.split()
  for i in splitUserInput:
    if i in words:
      words[i] = words[i] + 1
    else:
      words[i] = 1
  userInput = input("Enter line: ")
words = sorted(words.items())
words = dict(words)
for i, j in words.items():
  print(i, j)