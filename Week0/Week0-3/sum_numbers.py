import sys

def sum_numbers():
	filename = sys.argv[1]
	file = open(filename, "r")
	contents = file.read()
	contents = contents.split(" ")
	sum = 0
	for i in range(0, int(len(contents))):
		sum += int(contents[i])

	return sum

print (sum_numbers())
