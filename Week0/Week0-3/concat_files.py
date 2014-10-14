import sys

def concat_files():
	contents = []
	for i in range (1, int(len(sys.argv))):
		file = open(sys.argv[i], "r")
		contents.append(file.read())
		file.close()
	file = open("Concatenated", "w")
	file.write("\n".join(contents))
	file.close()


print (concat_files())

