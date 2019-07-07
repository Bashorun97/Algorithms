'''
    This is a highly inefficient algorithm
    Worst-case performance: Unbounded (randomized version),[1] O((n+1)!) (deterministic version)
    Best-case performance: O(n)
    Average performance	O((n+1)!)
'''
import random

def monkey_sort(unsort):

    while not is_sort(unsort):
        random.shuffle(unsort)
    return unsort

def is_sort(unsort):
    arr_len = len(unsort)

    if arr_len < 2:
        return True
    for i in range(arr_len - 1):
        if unsort[i] > unsort[i+1]:
            return False
    return True


unsort = [4,3,2,1,10]
print(monkey_sort(unsort))
