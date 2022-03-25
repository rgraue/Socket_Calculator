# class to perform simple two argument math operations
class Calculator:
    # simple constructor
    def __init__ (self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    # handles and determines perfomance of the operations
    def perform (self):
        self.op = self.op.upper()
        if (self.op == '+'):                        # addition
            return self.add()
        elif (self.op == '-'):                      # subtraction
            return self.subtract()
        elif (self.op == '*' or self.op == 'X'):    # multiplication
            return self.multiply()  
        elif (self.op == '/'):                      # division
            return self.divide()    
        elif (self.op == '^'):                      # Exponents
            return self.power()
        elif (self.op == '%'):                      # Modulo
            return self.mod()
        elif (self.op == 'E'):                      # Scientific notation
            return self.scientific()
        else:
            return self.handleError("No viable operator")
    # addition method
    def add (self):
        return self.lhs + self.rhs
    # subtraction
    def subtract (self) :
        return self.lhs - self.rhs
    # multiplication
    def multiply (self) :
        return self.lhs * self.rhs
    # division
    def divide (self) :
        if (self.rhs == 0):
            return self.handleError('Cannot divide by 0')
        return self.lhs / self.rhs

    def mod (self) :
        return self.lhs % self.rhs

    # power functionality
    def power (self) :
        try:
            if (self.rhs == 0): #if power of 0
                return 1.0
            elif (self.rhs == 1):   #if power of 1
                return self.lhs
            else:
                base = self.lhs
                for x in range(abs(int(self.rhs)) - 1): # truncate floats to int
                    self.lhs *= base
            if (self.rhs < 0):      # invert if power of a negative
                return 1 / self.lhs
            return self.lhs
        except :
            return self.handleError('Power Error') # Troublshooting error handler

    # Scientific notation
    # input 2 E 3 = 2000
    def scientific (self):
        base = 1
        for x in range(abs(int(self.rhs))):
            base *= 10
        if (self.rhs < 0):
            return self.lhs / base
        return self.lhs * base

        
    # simple error handler
    def handleError (self, error):
        return "Error Thrown: {}".format(error)