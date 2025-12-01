#unordered list
import time, random
start = time.time()#

y = 10 #<-- sets list length
items = [78, 56, 34, 43, 780, 324, 85, 234324]
n = len(items) - 1 #<-- thats the comparisons
index = 0

#prints the first item in the list
print(items[0])

#this prints length of the list
print('length of list is:', n)

#only swaps them if item 0 is larger than item 1. as we are sorting in ascending order
#if (items[0] > items[1]):
    #swaps the first 2 values, 23 and 41
   # temp = items[0]
   # items[0] = items[1]
   # items[1] = temp

#for iterating passes
for x in range(0, n):
    #this is the code for one pass over the list
    for index in range(0, n):
        #does the same as the if statement above, but for EVERY number
        if (index > index+1):
            #swaps the first 2 values, 23 and 41
            temp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = temp

end = time.time()
speed = round(end - start, 5)
print('time taken: ', speed)
print(items)