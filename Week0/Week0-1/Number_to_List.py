def number_to_list(n):
	list = []
	for i in range(int(len(str(n))),0 , -1):
		list.append(n%10)
		n = n//10	
	return list[::-1]

print (number_to_list(123))