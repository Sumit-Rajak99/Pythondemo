# single level inheritance
# class Parents:
#     city="bhopal"
#     def car(self):
#         print("car form parents")

# class Child(Parents):
#     pass

# obj=Child()
# print(obj.city) 
# # x=obj.city
# # print(x)
# obj.car()    




# multilevel inhetice

class Grand_parants:
    car="creata"
    def Home(self):
        print("home form Grand parants")
class Parants(Grand_parants):
    Bank="SBI"
    def land(self):
        print("land from parants")
class Child(Parants):
    pass
obj=Child()
print(obj.car,obj.Bank)
obj.land()
obj.Home()            
        