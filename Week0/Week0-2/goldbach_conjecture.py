def is_Prime(num):
    devisor = 2
    while devisor <= int(num ** 0.5):
        if num % devisor == 0:
            return False
        devisor += 1
    return True


def list_of_primes(n):
    list_of_primes = []
    num = 1
    while num < n:
        if is_Prime(num):
            list_of_primes.append(num)
        num += 1
    return list_of_primes


def goldbach(num):
    temp = list_of_primes(num)
    result = []
    a = 1
    b = 1
    for a in range(0, num // 2):
        for b in range(0, num):
            if is_Prime(a) and is_Prime(b) and a + b == num:
                result. append((a, b))
    return result


print (goldbach(100))
