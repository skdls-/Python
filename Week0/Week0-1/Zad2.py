def sum_of_digits(n):
	sum = 0
	if n<0:
		n = -n
	while n!=0:
		sum += n%10
		n = int(n/10)
	return sum

print (sum_of_digits(-12453))

