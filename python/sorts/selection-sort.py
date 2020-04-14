def selection_sort(arr):

    arr_len  = len(arr)
    for i in range(arr_len - 1):
        least = i
        for j in range(i+1, arr_len):
            if arr[j] < arr[least]:
                least = j
        arr[least], arr[i] = arr[i], arr[least]
    print(arr)
selection_sort([4,3,2,1])
