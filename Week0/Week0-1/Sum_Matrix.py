def sum_of_arr(elem):
	sum = 0
	for i in elem:
		sum+=i
	return sum

def sum_matrix(m):
	sum = 0
	for elem in m:
		sum += sum_of_arr(elem)
	return sum

print (sum_matrix ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))