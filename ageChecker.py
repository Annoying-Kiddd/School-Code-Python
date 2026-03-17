
age = int(input('Input your age:  '))

while age <= 0 or age >= 130:
    print('...nuh uh')
    exit()
    

if age > 0 or age < 130:
    print('good job you know how old you are :D')
