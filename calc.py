import math

class Calc:

    ##Validate values first
    def validate(self, value):
        if not type(value) is int:
            raise(ValueError("Only integers are accepted as inputs"))

    ##Add values
    def add(self, a, b):
        self.validate(a)
        self.validate(b)
        return a + b

    ##Subtract values
    def subtract(self, a, b):
        self.validate(a)
        self.validate(b)
        return a - b

    ##Multiply values
    def multiply(self, a, b):
        self.validate(a)
        self.validate(b)
        return a * b

    ##Multiply values
    def divide(self, a, b):
        self.validate(a)
        self.validate(b)
        ##Additionally, check that divisor is not 0
        if b == 0:
            raise(ValueError("Cannot divide a value by 0"))
        return a / b
    
    ##Get power of values
    def power(self, a, b):
        self.validate(a)
        self.validate(b)
        return a ** b

    ##Get Squareroot of values
    def sqrt(self, a):
        self.validate(a)
        ##Additionally, check that value is not negative
        if a < 0:
            raise(ValueError("Squareroots are allowed for positive values only"))
        return math.sqrt(a)