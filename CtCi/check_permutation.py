def sort_string(string):
  char_arr = list(string)
  char_arr.sort()
  return char_arr

def check_permutation(s1, s2):
  if len(s1) != len(s2):
    return False
  return True if sort_string(s1) == sort_string(s2) else False

def compute_hash_table(str1):
  hash_table = {chr(i):0 for i in range(0, 256)}
  for char in str1:
    hash_table[char] += 1
  return hash_table
    
def check_permutation2(s1, s2):
  if len(s1) != len(s2):
    return False
  
  s2 = list(s2)
  hash_table = compute_hash_table(s1)
  for index in range(len(s2)):
    char = s2[index]
    hash_table[char] -= 1
    if hash_table[char] < 0 :
      return False
  return True

print(f"1st algorithm: {check_permutation('emma', 'emma')}")
print(f"2nd algorithm: {check_permutation2('BEmmanuel', 'EmmanuelB')}")
print(f"2nd algorithm: {check_permutation2('god ', 'd og')}")
