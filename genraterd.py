# def outer(var):
#     def inner_fun(x,y):
#         x=x+5
#         y=y+10
#         var(x,y)
#     return inner_fun
# @outer
# def add(p,q):
#     print(p+q)
    
# x=int(input("enter any number:"))
# y=int(input("enter any number :"))

# add(x,y) 




# x=range(100)
# print(list(x))

def gen_number(n):
    i=1
    while i<=n:
        yield i
        i=i+1
        
n=int(input("enter any number :"))
var=gen_number(n)
for i in var:
    print(i)
    
print(var) 
# print(list(var))
ele1=next(var)
print(ele1)
print("hello")
print("welcome")
ele2=next(var)
print(ele2)       