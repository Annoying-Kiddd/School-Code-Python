num1 = int(input('Input an integer:  '))
num2 = int(input('Input another integer:  '))
num3 = int(input('Input another integer:  '))
num4 = int(input('Input another integer:  '))
num5 = int(input('Input another integer:  '))
num6 = int(input('Input another integer:  '))


def largest():
    a = (num1, num2, num3, num4, num5, num6)
    big = max(a)
    print('The largest number input is: ', big)

def smallest():
    a = (num1, num2, num3, num4, num5, num6)
    small = min(a)
    print('The smallest number input is: ', small)

def average():
    avg = ((num1 + num2 + num3 + num4 + num5 + num6) / 6)
    print('The average of the inputs is:', avg)


def main():
    largest()
    smallest()
    average()
   

main()