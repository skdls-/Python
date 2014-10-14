import sys


def cat_mine():
    filename = sys.argv[1]
    file = open(filename, "r")

    content = file.read()
    print(content)

    file.close()


def main():
    cat_mine()

if __name__ == '__main__':
    main()
