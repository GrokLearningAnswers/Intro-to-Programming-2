translation = {}
with open("dictionary.txt") as f:
    for line in f:
        english, abo = line.strip().split(',')
        translation[english] = abo

userInput = input("English: ")
while userInput:
    temp = []
    for word in userInput.split():
        temp.append(translation[word])
    print(' '.join(temp))
    userInput = input("English: ")
