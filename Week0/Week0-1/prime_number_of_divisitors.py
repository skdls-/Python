from week0_Zad4_is_Prime import is_prime

def prime_number_of_divisitors(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0:
			count +=1
	return is_prime(count)

print (prime_number_of_divisitors(7))
