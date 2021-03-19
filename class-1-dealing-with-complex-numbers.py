import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real if real else 0.0
        self.imag = imaginary if imaginary else 0.0

    def __add__(self, no):
        return Complex(self.real + no.real, self.imag + no.imag)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imag - no.imag)
        
    def __mul__(self, no):
        return Complex(
    self.real * no.real + self.imag * no.imag * -1,
    self.real * no.imag + self.imag * no.real
    )

    def __truediv__(self, no):
        n = self.__mul__(Complex(no.real, -no.imag))
        return n.__mul__(complex(1.0/(no.mod().real)**2, 0))        

    def mod(self):
        return Complex(math.pow(self.real**2 + self.imag**2, 0.5), 0)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real:.2f}+{self.imag:.2f}i"
        return f"{self.real:.2f}{self.imag:.2f}i"

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    # print(x+y)
    print('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))
