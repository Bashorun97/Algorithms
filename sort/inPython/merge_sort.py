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
n = [345, 2, 6]
print(merge_sort(n))
