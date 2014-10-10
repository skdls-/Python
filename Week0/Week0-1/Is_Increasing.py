def is_increasing(seq):
	for i in range(0, int(len(seq) - 1)):
		if seq[i] > seq[i+1]:
			return False
	
	return True

print (is_increasing([1,2,3,4,5]))

