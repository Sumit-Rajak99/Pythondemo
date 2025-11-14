# class Student:
#     pass
# print(dir(Student))

# inheritanc= method overriding , super method ya super key
# poloymorephism=method overload ,MRO 

#  python is supported  method overriding 
#  python is supported method overload



class Student:
    def add(x,y):
        print(x+y)
    def add(x,y,z):
        print(x+y+z)
    def add(x,y,z,p):
        print(x+y+z+p)
        
obj=Student
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)
obj.add(10,20,30,40)                
