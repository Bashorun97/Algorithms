def insertion_sort(sort):
    for i in range(len(sort)):

        j = i-1;
        key = sort[i]
        while sort[j] > key and j >= 0:
            sort[j + 1] = sort[j]
            sort[j] = key
            j = j - 1
        print(sort)    

insertion_sort([5, 2, 6, 4, 1, 3])
