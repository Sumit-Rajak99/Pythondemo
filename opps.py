# class Student:
#     "student object data"
#     school_name="mp convent"
#     def __init__(self):
#         print("constracter called")
# print(id(Student))
# print(Student.school_name)        
 
 
# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student
# print(id(obj2))
# most important questtion interview
# class Student:
#     "this is opp's class"
#     x=10
#     y=20
#     z=30
#     def show():
#         print("this is opp's class")
# print(dir(Student))
# print(Student.__doc__)     
# print(Student.__module__) 
# print(Student.__dict__)  
# print(Student.__init__)     #inbuild_constracter    



# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student()
# print(id(obj2))


class Student:
    school='mp convent'
    def __init__(self):
        print("constracter called")
        print(id(self))
print(id(Student))        
obj=Student()
print(id(obj)) 
obj1=Student()
print(id(obj1))


# self= self is reference varibla it is hold a current obj of current obj address 
      
    