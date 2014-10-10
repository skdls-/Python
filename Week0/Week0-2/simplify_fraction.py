def simplify_fraction(fraction):
    for n in range(1, max(fraction)):
        if fraction[0] % n == 0 and fraction[1] % n == 0:
            ala = fraction[0]
            ala /= n
            bala = fraction[1]
            bala /= n
            n -= 1
    temp = (ala,bala)
    return temp

print (simplify_fraction((63,462)))
