cords = set()
guess = input("Guess: ")
while guess:
  if guess in cords:
    print("You've chosen that square already")
  else:
    cords.add(guess)
    print(f"Hit {guess}")
  guess = input("Guess: ")