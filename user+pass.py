
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
        #loop it somehow

def main():
    userinput()
    usercheck()

main()

 


    
