def linear_search(arr, search):
    arr_len = len(arr)

    for i in range(1, arr_len):
        if arr[i] == search:
            return i
    return None

arr = [4,5,12,3,2,1]
search = 13
print(linear_search(arr, search))
