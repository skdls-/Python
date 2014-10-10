def sevens_in_a_row(arr, n):
    counter = 0
    search_for= []
    for k in range (0,n):
    	search_for.append(7)
    for i in range(0, len(arr) - 1):
        if arr[i] == 7:
            if arr[i: i+n] == search_for:
                return True
    return False

print (sevens_in_a_row([7, 4, 4, 5, 7,7,7,7,7,7,7,7], 9))
