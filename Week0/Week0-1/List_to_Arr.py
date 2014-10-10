def list_to_number(list):
	sum = 0
	for i in range ( 0, len(list)):
		sum += list[int(len(list))-i-1] * 10**i
	return sum

print (list_to_number([1,2,3]))