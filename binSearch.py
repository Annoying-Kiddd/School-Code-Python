array = [12, 24, 36, 48, 60, 72, 84, 98]
target = int(input('Enter target value:  '))
found = False
count = 0
first = 0
last = len(array)-1

#the loop :D
#--------------------
while (found == False and first <= last):
    mid = (first + last) // 2

    #if target is found first try
    if (target == array[mid]):
        found = True
        count += 1
    else:
        #for moving left/right pointers to find
        if (target < array[mid]):
            last = mid - 1
            count += 1
            print('the left side of the array was selected')
        elif (target > array[mid]):
                first = mid + 1
                count += 1
                print('the right side of the array was selected')

print(count, 'comaprison(s) used')
if (found):
     print('The data value,', target, 'was found')
else:
     print('The data value,', target, 'was not found')