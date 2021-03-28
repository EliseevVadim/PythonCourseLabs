class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()
    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)
    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
    def __invert__(self):
        temp=0
        temp=self.__num
        self.__num=self.__den
        self.__den=temp
        return self
    def __pow__(self, other):
        self.__num**=other
        self.__den**=other
        return self
    def __float__(self):
        return self.__num/self.__den
    def __int__(self):
        return int(self.__num/self.__den)
    def __neg__(self):
        self.__num*=-1
        return self
    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)