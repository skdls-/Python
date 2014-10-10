def is_int_palindrome2(n):
	n = str(n)
	temp = n[::-1]
	if n == temp:
		return True
	return False

print (is_int_palindrome2(112211))