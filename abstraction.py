from abc import ABC,abstractclassmethod
class Calculator(ABC):
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def multi(self,a,b):
        print(a*b)
    @abstractclassmethod
    def div(self):
        pass
    

class Junior(Calculator):
    def div(self,a,b):
        print(a//b)
        
obj=Junior() 
obj.add(3,4)
obj.sub(3,4)
obj.multi(3,4)
obj.div(3,4)
               