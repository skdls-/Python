def prepare_meal(number):
    temp = number
    count = 0
    result = ""
    while number % 3 == 0:
        count += 1
        number //= 3
        result += "spam "
    if temp % 5 == 0:
        result += "and eggs"
    return result

print(prepare_meal(45))
