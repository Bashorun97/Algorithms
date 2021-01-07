#!/usr/bin/env python3

class Hash:
  def __init__(self, string, **kwargs):
    self.string = string
    self.p_pow = kwargs['p_pow']
    self.hash_value = kwargs['hash_value']
    self.m = kwargs['m']
    self.p = kwargs['p']

  # Compute hash with rolling function
  def compute_hash(self):
    for i in self.string:
      self.hash_value = (self.hash_value + (ord(i) - ord('a') + 1) * self.p_pow) % self.m
      self.p_pow = (self.p_pow * self.p_pow) % self.m
    return self.hash_value

# hash_ = Hash('Hello World!', p_pow=1, hash_value=0, m=1E9 + 9, p=31)
# print(hash_.compute_hash())
