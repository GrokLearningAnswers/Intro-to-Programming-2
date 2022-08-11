classlist = open('classlist.txt').read().lower().split('\n')
used = []
counter = 0
for name in classlist:
    try:
        first, *middle, last = name.split()
        if first + ''.join(middle) not in used:
            used.append(first + ''.join(middle))
        else:
            name = first + ''.join(middle) + last[0]
            if name not in used:
                used.append(name)
            else:
                while True:
                    counter = counter + 1
                    if first + ''.join(middle) + last[0] + str(counter) not in used:
                        used.append(first + ''.join(middle) + last[0] + str(counter))
                    break

    except:
        pass
for username in used:
    print(username)