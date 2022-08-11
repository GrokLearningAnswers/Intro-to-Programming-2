guessesLeft = 10
mistakes = 0
while True:
  userInput = int(input("Guess a multiple of 7: "))
  if (userInput % 7) != 0:
    if mistakes != 0:
      print("Another mistake. Too bad.")
      break
    else:
      print("Mistake! That number isn't a multiple of 7.")
      mistakes = 1
  else:
    if userInput == 42:
      print("You won!")
      break
    else:
      print("Nope!")
  guessesLeft += -1
  if guessesLeft == 0:
    print("No guesses left!")
    break
print("That was fun.")