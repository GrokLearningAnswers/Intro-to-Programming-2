with open("english.txt") as f:
  english = set(f.read().split())
with open("french.txt") as f:
  french = set(f.read().split())
same = english & french
for i in same:
  print(i)