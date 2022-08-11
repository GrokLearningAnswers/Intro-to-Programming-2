votes = {}
nameAndVote = input("Name:vote ")
while nameAndVote:
  name, vote = nameAndVote.split(":")
  if vote not in votes:
    votes[vote] = [name]
  else:
    votes[vote].append(name)
  nameAndVote = input("Name:vote ")
for i, j in votes.items():
  names = ' '.join(j)
  print(f"{i} {len(j)} vote(s): {names}")