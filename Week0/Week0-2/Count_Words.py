def count_words(arr):
    print(arr)
    dicto = {}
    for elem in arr:
        if elem not in dicto.keys():
            dicto[elem] = 1
        else:
            dicto[elem] += 1
        print (dicto)
    return dicto

print(count_words(["apple", "banana", "apple", "pie"]))
