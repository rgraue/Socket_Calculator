# class to perform simple two argument math operations
class Calculator:
    # simple constructor
    def __init__ (self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    # handles and determines perfomance of the operations
    def perform (self):
        if (self.op == '+'):                        # addition
            return self.add()
        elif (self.op == '-'):                      # subtraction
            return self.subtract()
        elif (self.op == '*' or self.op == 'X'):    # multiplication
            return self.multiply()  
        elif (self.op == '/'):                      # division
            return self.divide()
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
        
    # simple error handler
    def handleError (self, error):
        return "Error Thrown: {}".format(error)