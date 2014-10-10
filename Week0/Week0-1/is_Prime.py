def is_Prime(num):
    devisor = 2
    while devisor <= int(num ** 0.5):
        if num % devisor == 0:
            return False
        devisor += 1
    return True