rules = {
    ('scissors', 'paper'): 'Scissors cut Paper',
    ('paper', 'rock'): 'Paper covers Rock',
    ('rock', 'lizard'): 'Rock crushes Lizard',
    ('lizard', 'spock'): 'Lizard poisions Spock',
    ('spock', 'scissors'): 'Spock melts Scissors',
    ('scissors', 'lizard'): 'Scissors decapitate Lizard',
    ('lizard', 'paper'): 'Lizard eats Paper',
    ('paper', 'spock'): 'Paper disproves Spock',
    ('spock', 'rock'): 'Spock vaporizes Rock',
    ('rock', 'scissors'): 'Rock breaks Scissors',
}

hand1 = input("Hand 1: ")
hand2 = input("Hand 2: ")
if (hand1, hand2) in rules:
    print(rules[(hand1, hand2)])
elif (hand2, hand1) in rules:
    print(rules[(hand2, hand1)])
else:
    print("Tie")
