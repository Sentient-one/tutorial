class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


c1 = Complex(3, 4)
c2 = Complex(2, -1)


c3 = c1 + c2


print(f"First complex number: {c1}")
print(f"Second complex number: {c2}")
print(f"Sum of complex numbers: {c3}")