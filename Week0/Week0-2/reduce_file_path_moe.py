def reduce_file_path(path):
	path = path.split('/')
	result = []
	for i, element in enumerate(path):
		if element == '..':
			del path[i]
			del path[i-1]
		elif element == '.':
			del path[i]
		for i, elem in enumerate(path):
			if elem== "":
				del path[i]
	

	return "/".join(path)

print(reduce_file_path("/home/////radorado/code/./hackbulgaria/week0/../'"))