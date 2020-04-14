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

if __name__ == '__main__':
    try:
        take = input('Enter arrays seperated with a comma: ')
    except:
        take = raw_input('Enter arrays seperated with a comma: ')
    unsort = []
    for i in take.split(','):
        int(i)
        unsort.append(i)
    print(monkey_sort(unsort))
