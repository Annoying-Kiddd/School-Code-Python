import random, time


y = int(input('How long should the list be?\n')) #<-- sets list length
start = time.time() #istead of timing the list from when the program starts, it times the actual sorting part
#unordered list
items = [random.randint(0, 100) for x in range (y)]
len_items = len(items)

#range of items 1 - last item
for index in range (1, len_items):

    current = items[index]
    index2 = index
    #this part compares 2 of the numbers together
    #e.g: in a list of [3, 67, 33, 128], itd compare the numebrs as goes:
    #3 & 67, 67 & 33, 33 & 128. (this is one pass)
    #the passes continue till the list is sorted
    while (index2 > 0 and  items[index2-1] > current):

        items[index2] = items[index2-1]
        index2 = index2 - 1

    items[index2] = current

end = time.time()
speed = round(end - start, 5)
print('time taken: ', speed)

print(items)