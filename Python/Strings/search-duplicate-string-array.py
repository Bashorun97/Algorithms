#! /usr/env/bin python3
import collections
import compute_hash

class GroupStrings:

  def __init__(self, string_array):
    self.string_array = string_array

  def group_identical_strings(self):
    hashes = {}
    for i, string in enumerate(self.string_array):
      hash_ = compute_hash.Hash(string, p_pow=1, hash_value=0, m=1E9 + 9, p=31)
      hashes.update({hash_.compute_hash(): i})
      order = collections.OrderedDict(sorted(hashes.items()))
    return order


gstrings = GroupStrings(['hello', 'hello', 'world'])
print(gstrings.group_identical_strings())
