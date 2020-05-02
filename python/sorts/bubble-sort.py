# Sat 02 May 2020 07:04:24 AM WAT 
# babaibeji

def bubble_sort(unsort):
  # first pass limits sorting to unsorted elements
  unsort_len = len(unsort)
  for i in range(unsort_len - 1):
    for j in range(unsort_len - 1- i):
      if unsort[j] > unsort[j + 1]:
        # swap pairs
        unsort[j], unsort[j + 1] = unsort[j + 1], unsort[j]
  return unsort

if __name__ == '__main__':
  inputs = input('Enter values separating each with a comma: ').strip()
  user_data = [item for item in inputs.split(',')]
  print(*bubble_sort(user_data), sep=', ')
