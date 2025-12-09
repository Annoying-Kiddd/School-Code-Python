import random

def Linear():

    items = [random.randint(0, 20) for x in range (10)]
    found = False
    
    #tells program what to search for
    sTerm = int(input('enter a search term: '))

    
    for x in range(0, len(items)):

        #searching bit
        if (sTerm == items[x]):

            found = True
        
        #prints not found till its found
        if found == False:
            print('Not found data item')
        else:
            print('found data item')
            exit()
    print(items)

    choice()





def Binary():
    items = [random.randint(0, 20) for x in range (10)]

    target = int(input('Enter search term:  '))
    found = False
    first = 0
    last = len(items)-1

    while (found == False and first <= last):
        mid = (first + last) // 2

        if (target == items[mid]):  
            found = True
        else:
            if (target < items[mid]):
                last = mid - 1

                print('the left side of the array was selected')
            elif (target > items[mid]):
                    first = mid + 1

                    print('the right side of the array was selected')
    if (found):
        print('The data value', target, 'was found')
    else:
        print('The data value,', target, 'was not found')

    print(items)
    choice()


def Bubble():

    items = [random.randint(0, 20) for x in range (10)]
    n = len(items) - 1 
    swapped = True
    index = 0

    print(items)

    while (swapped and n > 0):
        swapped = False

        for index in range(0, n):
        
            if (items[index] > items[index+1]):
            
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
            
                swapped = True
            
        n = n - 1

    print(items)

    choice()
    

def Insertion():
    
    items = [random.randint(0, 20) for x in range (10)]
    len_items = len(items)

    print(items)
    
    for index in range (1, len_items):

        current = items[index]
        index2 = index

        while (index2 > 0 and  items[index2-1] > current):

            items[index2] = items[index2-1]
            index2 = index2 - 1

        items[index2] = current

    print(items)

    choice()




def choice():
    userchoice = int(input('Which program would you like to run?\n  1. linear search\n  2. binary search\n  3. bubble sort\n  4. insertion sort\nOr to exit, type 0\n'))

    if userchoice == 1:
        Linear()
    elif userchoice == 2:
        Binary()
    elif userchoice == 3:
        Bubble()
    elif userchoice == 4:
        Insertion()
    else:
        exit()


choice()