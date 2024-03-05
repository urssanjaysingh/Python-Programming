class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, number): #here self refers to n1 object
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result
        
n1 = Complex(5, 6)
n2 = Complex(-4, 2)
# here we're calling n1 object
# and pass n2 object to it
# so inside the add() self will be n1 and number will be n2
result = n1.add(n2)
print("real =", result.real)
print("imag =", result.imag)