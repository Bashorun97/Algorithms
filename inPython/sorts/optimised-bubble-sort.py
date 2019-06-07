from __future__ import print_function

def bubble_sort(arr):

    arr_length = len(arr)
    for i in range(arr_length-1):
        switch = False
        for j in range(arr_length-1-i):
            if arr[j] > arr[j+1]:
                switch = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not switch:
            break
    return arr

user_input = input('Enter values: ').strip()
unsort = []
for item in user_input.split(','):
    unsort.append(item)
print(*bubble_sort(unsort), sep=', ')
