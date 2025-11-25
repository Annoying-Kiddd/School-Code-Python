import random
randomlist = []
valueone = 0
valuetwo = 5

for i in range(valueone, valuetwo):
    n = random.randint(0, 31) #randint -> random integer
    randomlist.append(n)

print(randomlist)
