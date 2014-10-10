def is_decreasing(seq):
	for i in range(0, int(len(seq) - 1)):
		if seq[i] < seq[i+1]:
			return False
	
	return True

print (is_decreasing([5,4,3,5,2,5]))