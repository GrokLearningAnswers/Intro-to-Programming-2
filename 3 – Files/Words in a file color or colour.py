word = input("Word to look for: ")
with open("book.txt") as f:
  if word in f.read().lower():
    print(f"{word} was found in the book.")
  else:
    print(f"{word} was not found in the book.")