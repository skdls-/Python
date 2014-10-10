def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    return nth_fib_lists(n - 1) + nth_fib_lists(n - 2)

print (nth_fib_lists([], [1, 2, 3],4)