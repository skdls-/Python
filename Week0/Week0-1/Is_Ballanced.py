def sum_of_digits(n):
	sum = 0
	while n!=0:
		sum += n%10
		n = n//10
	return sum


def is_ballanced(num):
	lenght = int(len(str(num)))
	if lenght %2 == 0:
		if sum_of_digits(num//(10**(lenght/2))) == sum_of_digits(num%(10**(lenght/2))):
			return True
		return False

		