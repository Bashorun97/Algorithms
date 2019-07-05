#Binary search works only on sorted arrays
#Time complexity: 0(logn)
#The binary function takes to arguments. 1) sorted array 2) Value to be searched

def binary_search(n, x):
    i = 0
    d = len(n) - 1

    while i < len(n):
        center = i + (d - i)//2;
        if n[center] == x:
            return center
        elif n[center] < x:
            i = center + 1
        else:
            i = center -1
    return 'Position not found';

sorted = [52,3,4,5,6,456,24,546,68,23,1,78,0,-1,32]
print(binary_search(sorted, 546))