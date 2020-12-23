def merge_sort(n):
    start = []
    end = []
    while len(n) > 1:
        a = min(n)
        b = max(n)
        start.append(a) and end.append(b)
        n.remove(a) and n.remove(b)
    if n:
        start.append(n[0])
    end.reverse()
    return (start + end)
n = [3,4,2,1,5,35,0,55,2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
print(merge_sort(n))
