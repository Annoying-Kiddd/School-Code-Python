

def mainmenu():
    choice = int(input('Hello! would you like to:\n   1)Add a record\n   2)update a record\n   3)delete a record'))
    if choice == 1:
        print('added a record')
    elif choice == 2:
        print('updated a record')
    elif choice == 3:
        print('deleted a record')
    else:
        print('invalid input try again')
