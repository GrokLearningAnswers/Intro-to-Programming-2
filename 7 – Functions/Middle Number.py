def find_middle(a, b, c):
  tempList = []
  tempList.append(a)
  tempList.append(b)
  tempList.append(c)
  tempList = sorted(tempList)
  return tempList[1]
