class Fraction(object):

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def simplify_fraction(Fract):
        i = 2
        while i < max(Fract.num, Fract.den):
            if Fract.num % i == 0 and Fract.den % i == 0:
                Fract.num /= i
                Fract.den /= i
            else:
                i += 1

    def suma(Fraction1, Fraction2):
        Fraction1.num *= Fraction2.den
        Fraction2.num *= Fraction1.den
        chislitel = int(Fraction1.num + Fraction2.num)
        Fraction1.den *= Fraction2.den
        Fraction2.den = Fraction1.den
        znamenatel = int(Fraction2.den)
        result = Fraction(chislitel, znamenatel)
        Fraction.simplify_fraction(result)
        print (result.num, "/", result.den)

        return result

    def razlika(Fraction1, Fraction2):
        Fraction1.num *= Fraction2.den
        Fraction2.num *= Fraction1.den
        chislitel = int(Fraction1.num - Fraction2.num)
        Fraction1.den *= Fraction2.den
        Fraction2.den = Fraction1.den
        znamenatel = int(Fraction2.den)
        result = Fraction(chislitel, znamenatel)
        Fraction.simplify_fraction(result)
        print (result.num, "/", result.den)

        return result

    def ravno(Fraction1, Fraction2):
        Fraction.simplify_fraction(Fraction1)
        Fraction.simplify_fraction(Fraction2)
        if Fraction1.num == Fraction2.num:
            return True
        return False

    def greater(Fraction1, Fraction2):
        if Fraction1.num / Fraction1.den > Fraction2.num / Fraction2.den:
            return True
        return False

    def smaller(Fraction1, Fraction2):
        return (not Fraction.greater(Fraction1, Fraction2))

drob = Fraction(2, 3)
drob2 = Fraction(1, 3)
Fraction.suma(drob, drob2)
Fraction.razlika(drob, drob2)
print (Fraction.smaller(drob, drob2))
print (Fraction.greater(drob, drob2))
print (Fraction.ravno(drob, drob2))
