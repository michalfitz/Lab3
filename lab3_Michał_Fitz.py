
class Wektor(object):

    number_of_objects = 0

    def __init__(self, x, y):
        self.a = x
        self.b = y
        Wektor.number_of_objects += 1

    def __str__(self):
        return ('Wektor o skladowych ({}, {})'.format(self.a, self.b))

    def __add__(self, other):
        return Wektor(self.a + other.a, self.b + other.b)
    
    def length(self):
        "Dlugosc wektora"
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def __neg__(self):
        tmp = self.a
        self.a = self.b
        self.b = tmp
    
    def neg_copy(self):
        return Wektor(self.b, self.a)

    def __mul__(self, other):
        return Wektor(self.a * other.a, self.b * other.b)

    def mul_num(self, m):
        return Wektor(self.a * m, self.b * m)

    def __del__ (self):
        del(self.a, self.b)


    

    

    

    
        

