def insertion_sort(sort):
    for i in range(len(sort)):

        j = i-1
        key = sort[i]
        # j >=0 is used to ensure that comparison ends at zeroth position
        # of array
        while sort[j] > key and j >= 0:
            sort[j + 1] = sort[j]
            sort[j] = key
            j = j - 1
    return sort

print(insertion_sort([5, 2, 6, 4, 1, 3]))
