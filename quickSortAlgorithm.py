def quicksort(arr):
    # Base case: if the array has 0 or 1 items, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (here: the first element)
    pivot = arr[0]

    # Create three lists:
    #   left  -> elements smaller than pivot
    #   equal -> elements equal to the pivot
    #   right -> elements greater than pivot
    left = []
    equal = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    # Recursively sort left and right, then combine
    return quicksort(left) + equal + quicksort(right)


# Example use:
numbers = [12, 4, 5, 3, 8, 7, 4, 11]
sorted_numbers = quicksort(numbers)
print("Sorted:", sorted_numbers)
