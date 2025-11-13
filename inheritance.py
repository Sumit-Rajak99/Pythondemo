# single level inheritance
# class parents:
#     city='bhopal'
#     def car(self):
#         print("car from bhopal")
# class child(parents):
#     pass
# obj=child()
# print(obj.city) 
# obj.car() 



# override
# class parent:
#     car='nexon'
#     def home(self):
#         print("home from parents")
# class child(parent):
#     car='Creta'
#     car2=parent.car
#     def home(self):
#         super().home()
#         print("home from child")
        
# obj=child()
# print(obj.car)
# print(obj.car2)
# obj.home()                





# multi level inharitance

class Grandparent:
    car='nexon'
    def home(self):
        print("home from gp")
class parent(Grandparent):
    bank="SBI"
    def land(self):
        print("land from parent")
class Child(parent):
    pass
obj=Child()
print(obj.car,obj.bank)
obj.land()
obj.home()         

                
      
        