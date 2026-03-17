userinp = int(input("enter a prime number from 1 to 1000:  "))

if userinp <= 1:
    print(False)
else:
    is_prime = True  # Flag variable
    for i in range(2, int(userinp**0.5) + 1):
        if userinp % i == 0:
            is_prime = False
            break
    print(is_prime)