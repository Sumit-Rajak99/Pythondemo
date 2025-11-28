# l=[1,2,3,3,45,5]
# l1=[34,34,54,65,56,6]
# def add(x,y):
#     return x+y
# res=map(add,l,l1)
# print(list(res))



# l=[1,2,3]
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]

# def add(x,y,z):
#     return x+y+z
# res=map(add,l,l1,l2)
# print(list(res))



# l,l1,l2=[1,2,3],[1,2,3,4,5],[1,2,3,4,5]
# def add(x,y,z):
#     return x+y+z
# print(list(map(add,l,l1,l2)))



# s=[60,50,40,30,60,50,7,77,6,88,66,88]
# def div(n):
#     if n>=60:
#         return n
# print(list(filter(div,s)))    

# s=[10,20,30,40,50,60]
# def max(n):
#     if n>=30:
#         return n 
# print(list(filter(max,s)))   




# s=eval(input("enetr any collcetion = "))
# def odd(n):
#     if n%2!=0:
#         return n 
 
# print(list(filter(odd,s)))     


# s=input("enetr any string: ")
# def str(n):
#     if n in('a','e','i','o','u','A','E','I','U','O'):
#         return n 
    
# res =list(filter(str,s))
# print("".join(res))    
    
    
    
# import functools

# l = [1,2,3,4,5,6,7,8,9,10]

# def add(a,b):
#     return a + b

# res = functools.reduce(add, l)
# print(res)
       

import functools
# l=[1,2,3,4,5,6,7,8,9,10]
# def add(a,b):
#     return a+b 
# # print(list(functools.reduce(add,l)))
# res=functools.reduce(add,l)
# print(res)  

# l=[1,2,3,4,5,6,7,8,,99,10]
# def even(a,b):
#     if a%2==0:
#         return a 
#     else:
          
# l=[4,5,6,7,8,6,5,444,5,6,6,7,7,55,4,344553,53,53,5]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res=functools.reduce(max,l)
# print(res)            

