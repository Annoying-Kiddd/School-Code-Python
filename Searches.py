nlist = [1, 3, 5, 7, 8, 13, 16, 17, 18, 26, 28, 34, 38, 42, 57, 63, 65, 67, 69, 79, 83, 95, 97, 99]
#the list :O ^

def Linear():
    
    found = False
    
    #tells program what to search for
    sTerm = int(input('enter a search term: '))

    
    for x in range(0, len(nlist)):

        #searching bit
        if (sTerm == nlist[x]):

            found = True
        
        #prints not found till its found
        if found == False:
            print('Not found data item')
        else:
            print('found data item')
            exit()
                     
def Binary():

    target = int(input('Enter search term:  '))
    found = False
    count = 0
    first = 0
    last = len(nlist)-1

    #the loop :D
    #--------------------
    while (found == False and first <= last):
        mid = (first + last) // 2

        #if target is found first try
        if (target == nlist[mid]):
            found = True
            count += 1
        else:
            #for moving left/right pointers to find
            if (target < nlist[mid]):
                last = mid - 1
                count += 1
                print('the left side of the array was selected')
            elif (target > nlist[mid]):
                    first = mid + 1
                    count += 1
                    print('the right side of the array was selected')


    if (found):
        print('The data value,', target, 'was found')
    else:
        print('The data value,', target, 'was not found')
             
def main():
    choice = int(input('To search for your Data item, select a searching type:\n  1) Linear Search\n  2) Binary Search\n'))

    if choice == 1:
        Linear()
    elif choice == 2:
        Binary()
    else:
        print('Sorry i sont understand')
        exit()



main()