import string
tally = {}
x = input("Tweet: ").lower()

while x:
  for word in x.split(" "):
    if word != "" and word[0] == "#":
      word = word.strip(string.punctuation + " ")
      if word in tally:
        tally[word] = tally[word]+1
      elif word not in tally:
        tally[word] = 1
  x = input("Tweet: ").lower()

for key in tally:
  print("#" + str(key) + " " + str(tally[key]))
