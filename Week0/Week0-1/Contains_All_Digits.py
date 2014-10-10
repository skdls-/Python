from Contains_Digit import contains_digit

def contains_all_digits(number, digits):
	for digit in digits:
		if contains_digit(number,digit):
			return True
	return False

print (contains_all_digits(1234, [1,2]))