def count_vowels(n):
	counter = 0
	vowels = ["a","o","i","e","u"]
	for char in n:
		if char in vowels:
			counter += 1
	return counter

print (count_vowels("Pazar"))