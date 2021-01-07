#!/usr/bin/env python3


def suffix_array(string):
  s_array = []
  for i in range(len(string)):
    s_array.append((string[i:], i))
  s_array.sort(key=lambda x: x[0])
  print(s_array)

suffix_array('Hello')
