import time, random

start = time.time()

y = 10 #<-- sets list length
#unordered list
items = [random.randint(0, 100) for x in range (y)]
n = len(items) - 1 #<-- thats the comparisons
swapped = True
index = 0

#prints the list --> print(items)
#prints the first item in the list
print(items[0])

#this prints length of the list
print('length of list is:', n)

#boolean variable: swapped, lets the loop keep repeating
while (swapped):
    swapped = False
    #this is the code for one pass over the list
    for index in range(0, n):
        #does the same as the if statement above, but for EVERY number
        if (index > index+1):
            #swaps the first 2 values, 23 and 41
            temp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = temp


            #when sorted, and there are no more swaps to be made, swapped remains False and the loop breaks
            swapped = True

end = time.time()
speed = round(end - start, 5)
print('time taken: ', speed)
print(items)