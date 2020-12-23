def merge(a1, a2, temp):
  i, j, k, n1, n2 = 0, 0, 0, len(a1), len(a2)

  while i <= n1 - 1 and j < n2 - 1:
    if a1[i] < a2[j]: temp[k], i = a1[i], i + 1
    else: temp[k], j = a2[i], j+1
    k += 1

  while i <= n1 - 1:
    temp[k] = a1[i]
    i, k = i+1, k+1

  while j <= n2 - 1:
    temp[k] = a2[j]
    j, k = j+1, k+1


def array_to_sort():
  array1_length = int(input("Enter list of length for array 1: "))
  array_1 = [int(input("Enter values in sorted order: ")) for i in range(array1_length)]

  array2_length = int(input("Enter list length for array 2: "))
  array_2 = [int(input("Enter values in sorted order: ")) for i in range(array2_length)]

  temp = [-1]*(array1_length + array2_length)
  merge(array_1, array_2, temp)
  print(temp)
array_to_sort()

