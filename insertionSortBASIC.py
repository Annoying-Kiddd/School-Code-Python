items = [77, 103, 29, 5, 1]
len_items = len(items)

for index in range (1, len_items):

    current = items[index]
    index2 = index

    while (index2 > 0 and  items[index2-1] > current):

        items[index2] = items[index2-1]
        index2 = index2 - 1

    items[index2] = current

print(items)