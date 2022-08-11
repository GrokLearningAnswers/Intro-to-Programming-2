import csv
nominees = {}
winningTitle = input("Winning title: ")
with open('nominees.csv', newline='') as f:
  for i in csv.DictReader(f):
    nominees[i['title']] = i['director(s)']
print(f"Congratulations: {nominees[winningTitle]}")