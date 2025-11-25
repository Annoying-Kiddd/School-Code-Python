cookiejar = 10
# ^ thats a global variable, available to the whole code

def setcookiejar():
    global cookiejar
    cookiejar = 10
    # now a local variable, set inside the suibroutine (the def)
    # when line 5 is added, becomes global again
    