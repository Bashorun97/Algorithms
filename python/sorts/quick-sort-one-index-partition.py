#!/usr/bin/env python3

def quick_sort(alist, l, u):
  print(alist)
  if l >= u :
    return alist

  m = l
  for i in range(l + 1, u + 1):
    if alist[i] < alist[l]:
      m += 1
      alist[m], alist[i] = alist[i], alist[m]
  alist[m], alist[l] = alist[l], alist[m]
  quick_sort(alist, l, m - 1)
  quick_sort(alist, m + 1, u)

unsorted = [6,5,3,1,8,7,2,4]
print(quick_sort(unsorted, 0, len(unsorted)-1))
