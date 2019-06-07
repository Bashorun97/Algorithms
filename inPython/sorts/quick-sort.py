def quick_sort(arr):
    arr_len = len(arr)
    great = []
    less = []
    if arr_len <= 1:
        return arr
    else:
        pivot = arr[0]
        for element in arr[1:]:
            if element > pivot:
                great.append(element)
            else:
                less.append(element)
    #recursively sort the smaller sorts
    return quick_sort(less) + [pivot] + quick_sort(great)


print(quick_sort([3,4,2,1,5,35,0,55,2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]))
