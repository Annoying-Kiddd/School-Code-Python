
def userinput():
    global user
    global passw
    user = input('enter your username (case sensitive)\n  ')
    passw = input('enter your password (case sensitive)\n  ')
    return user, passw


def usercheck():
    if (user == 'admin' and passw == 'passwd'):
        print('welcome', user)
    else:
        print('username or password incorrect')

def tryagain():
    again = 'y'
    while again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
        again = input ('Would you like to play again?')
        if again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
            return True
        else:
            return False

def main():
    userinput()
    usercheck()
    another = tryagain()
    if another == False:
        exit()

main()

 
        

    
