file = open('novel.txt').read().split()
dicto = {}
listo = []
for word in file:
  if word[0].isupper() == True:
    if word not in dicto:
      dicto[word]=1
    else:
      dicto[word] = dicto[word] + 1
for name in sorted(dicto, key=dicto.get):
  listo.append((name, dicto[name]))
listo.reverse()
print(listo[0][1], listo[0][0])
print(listo[1][1], listo[1][0])
print(listo[2][1], listo[2][0])