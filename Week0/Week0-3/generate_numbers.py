import sys
from random import randint


def generate_numbers():
    filename = sys.argv[1]
    file = open(filename, "w")
    n = int(sys.argv[2])  
    contents = []
    for i in range(0, n):
        number = randint(1, 1000)
        contents.append(str(number))
        
    file.write(" ".join(contents))
    file.close()


def main():
    generate_numbers()

if __name__ == '__main__':
    main()
