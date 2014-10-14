import sys


def chars():
    sum = 0
    file = open(sys.argv[2], "r")
    content = file.read()
    for char in content:
        sum += 1
    print (sum)


def words():
    sum = 0
    file = open(sys.argv[2], "r")
    content = file.read()
    content = content.split(" ")
    for word in content:
        sum += 1
    print (sum)


def lines():
    sum = 0
    file = open(sys.argv[2], "r")
    content = file.read()
    content = content.split("\n")
    for line in content:
        sum += 1
    print (sum)


def wc():
    if sys.argv[1] == "chars":
        chars()
    if sys.argv[1] == "words":
        words()
    if sys.argv[1] == "lines":
        lines()

wc()
