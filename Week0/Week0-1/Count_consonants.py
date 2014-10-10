def count_consonants(n):
	counter = 0
	vowels = ["a","o","i","e","u"]
	for char in n:
		if char not in vowels:
			counter += 1
	return counter

print (count_consonants("Pazar"))