
def settingamt():
    principal = int(input('Plesase enter hte principal amount:   '))
    rate = int(input('Please enter the rate:   '))
    time = int(input('Please enter the time (in years):   '))

    if (principal * rate * time) == 0:
        print('Invalid, cannot calculate')
    else:
        print('Thank you for you input\n\nLoading results...')
        print('Simple interest:', ((principal * rate * time) / 100))

settingamt()