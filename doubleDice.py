import random

def rolls():
    global dice2
    global dice1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

def tries():
    count = 0
    while dice1 != dice2:
        print('Roll', count, ':', dice1, ',', dice2)
        break

    count =+ 1

    if dice1 == dice2:
        print('Roll', count, ':', dice1, ',', dice2)
        print('Congranaptulationalismingalings you won nothing')

def tryagain():
    again = 'y'
    while again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
        again = input ('Would you like to roll again?\n  ')
        if again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
            return True
        else:
            return False

def main():
    rolls()
    tries()
    another = tryagain()
    if another == False:
        exit()
    else:
        main()

main()