f = open('mail.txt')
lines = f.readlines()
deliveries = {}
for line in lines:
  newDel = line.strip().split(',')
  if newDel[0] not in deliveries:
    if newDel[1] == 'Letter':
      deliveries[newDel[0]] = (1,0)
    elif newDel[1] == "Package":
      deliveries[newDel[0]] = (0,1)
  elif newDel[0] in deliveries:
    if newDel[1] == 'Letter':
      letters = deliveries[newDel[0]][0]
      packages = deliveries[newDel[0]][1]
      deliveries[newDel[0]] = (letters+1,packages)
    elif newDel[1] == "Package":
      letters = deliveries[newDel[0]][0]
      packages = deliveries[newDel[0]][1]
      deliveries[newDel[0]] = (letters,packages+1)
name = input('Name: ')
if name in deliveries:
  letters = deliveries[name][0]
  packages = deliveries[name][1]
if name not in deliveries:
  print('No mail')
elif letters == 0:
  print('No Letters')
  if packages > 1:
    print(packages, 'Packages')
  else:
    print(packages, 'Package')
elif packages == 0:
  if letters > 1:
    print(letters, 'Letters')
  else:
    print(letters, 'Letter')
  print('No Packages')
else:
  if letters > 1:
    print(letters, 'Letters')
  else:
    print(letters, 'Letter')
  if packages > 1:
    print(packages, 'Packages')
  else:
    print(packages, 'Package')