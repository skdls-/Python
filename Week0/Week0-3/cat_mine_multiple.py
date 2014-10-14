import sys


def cat_mine():
    for i in range(1,int(len(sys.argv))):
        filename = sys.argv[i]
        file = open(filename, "r")

        content = file.read()
        print(content)

    file.close()


def main():
    cat_mine()

if __name__ == '__main__':
    main()
