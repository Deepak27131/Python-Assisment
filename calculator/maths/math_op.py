
class MathOperation:
    def add(self, a,b):
        return a+b
    
    def mul(self,a,b):
        return a * b
    
    def div(self ,a ,b):
        try :
            return a / b
        except ZeroDivisionError as z : 
            return 'Cannot divide by zero' 
        else:
            return a / b
    
    def sqrt(self,a,b):
        return a ** b
    
    def sub(self,a,b):
        return a - b
    
    def module(self,a,b):
        return a % b
    