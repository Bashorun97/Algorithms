def gnome_sort(unsort):
    arr_len = len(unsort)
    if arr_len <= 1:
        return n

    i = 1
    while i < arr_len:
        if unsort[i-1] <= unsort[i]:
            i += 1
        else:
            unsort[i-1], unsort[i] = unsort[i], unsort[i-1]
            i -= 1
            if i == 0:
                i = 1

unsort = [2,3,1,34]
gnome_sort(unsort)
print(unsort)
