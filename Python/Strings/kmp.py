def pi_array(pattern):
	failure = [0]
	i = 0
	j = 1
	while j < len(pattern):
		if pattern[i] == pattern[j]:
		    i += 1
		elif i > 0:
		    i = failure[i-1]
		    continue
		j += 1
		failure.append(i)
	return failure

print(pi_array('abcdabc'))
