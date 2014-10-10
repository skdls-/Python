def contains_digit(number, digit):
	while (number != 0):
		if number%10 == digit:
			return True
		else:
			number = number//10

	return False
