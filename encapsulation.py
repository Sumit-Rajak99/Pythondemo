# public 
# class Parent:
#     bank="SBI"
#     def add(self):
#         print("hello")
# class Child(Parent):
#        pass

# obj=Child() 
# print(obj.bank)
# obj.add()       




# protictive
# class Parent:
#     _bank="SBI"
#     def _add(self):
#         print("hello")
# class Child(Parent):
#        pass

# obj=Child() 
# print(obj._bank)
# obj.add()   




class Parent:
    __bank="SBI"
    def __add(self):
        print("hello")
class Child(Parent):
       pass

obj=Child() 
# print(obj.__bank)
# obj.add()   
# print(Parent.__bank)
# print(dir(Parent))
print(obj._Parent__bank)
obj._Parent__add() 