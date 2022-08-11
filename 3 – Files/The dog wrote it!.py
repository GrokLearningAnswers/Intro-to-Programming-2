fixed = ''
with open("letter.txt", 'r') as nullLetter:
    openedLetter = nullLetter.read()
    letter = openedLetter.split("\n")
    for i in letter:
        if len(i) >= len(letter):
            if i[0] == 'W' and i[1] == 'O' and i[2] == 'O' and i[3] == 'F' and i[4] == '!':
                null = False
            else:
                fixed += str(i) + '\n'
with open("fixed.txt", 'w') as f:
    print(fixed.strip(), file=f)
