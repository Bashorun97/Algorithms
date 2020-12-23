# Sat May 02 09:40:15 WAT 2020
# Baba ibeji

# shell_sort a.k.a insertion sort on steriods
def shell_sort (unsort):
  h = int(input("Enter max increment (odd value) value: "))
  while h >= 1:
    for i in range(h, len(unsort)):
      temp = unsort[i]
      j = i - h
      while j >= 0 and unsort[j] > temp:
        unsort[j+h] = unsort[j]
        j = j - h
      unsort[j+h] = temp
    h = h - 2
  return unsort

if __name__ == '__main__':
  inputs = input('Enter values separating each with a comma: ').strip()
  user_data = [item for item in inputs.split(',')]
  if len(user_data) == 1: print(user_data[0])
  else:
    print(*shell_sort(user_data), sep=', ')
