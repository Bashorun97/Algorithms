#!/usr/env/bin python3

class RabinKarp:
  def __init__(self, pattern, text):
    self.pattern = pattern
    self.text = text

  def rabin_karp(self):
    count = 0
    p_hash = hash(self.pattern)
    p_len = len(self.pattern)

    for i in range(len(self.text)-(p_len-1)):
      t_hash = hash(self.text[i:i+p_len])
      if t_hash == p_hash and self.text[i:i+p_len] == self.pattern:
        print(f"{i}")
    #return count

rb = RabinKarp("foobarfoo", "barfoobarfoobarfoobarfoobarfoo")
rb.rabin_karp()
