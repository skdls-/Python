def is_an_bn(word):
	middle = len(word) // 2

	if word[0] != 'a':
		return False
	elif word[middle] != 'b':
		return False
	for i in range(0, int(len(word))//2):
		if word[i] != 'a':
			return False
		elif word[int(len(word))- i -1] != 'b':
			return False
	if word.count('a') != word.count('b'):
			return False
	return True


print(is_an_bn("aaaaabbb"))
