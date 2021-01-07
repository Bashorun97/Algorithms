#!/usr/bin/env python3


def naive_matching(pattern, text):
	p_len = len(pattern)
	t_len = len(text)
	count = 0

	for i in range(t_len - p_len + 1):
		j = 0
		while (j < p_len):
			if text[i+j] == pattern[j]:
				j += 1
			else:
				break
		if j == p_len:
			count += 1

	return f"{count} patterns found"

print(naive_matching("abcd", "abcdefabcdef"))

# Adapted from GeeksforGeeks
