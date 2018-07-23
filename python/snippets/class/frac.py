class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def get_numberator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_value(self):
        return self.numerator/self.denominator


if __name__ == "__main__":

    frac1 = Fraction(12,3)
    print frac1.get_numberator()
    print frac1.get_denominator()
    print frac1.get_value()
