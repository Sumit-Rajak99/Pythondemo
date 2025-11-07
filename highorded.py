# map() 
# l=[1,2,3,4,5]
# def squre(n):
#     return n*n
# res=map(squre,l)
# print(res)
# print(tuple(res))
# print(list(res))


# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.append(i*i)
# print(l1)   

# without using new list 

# l=[1,2,3,4,5]
# x=0
# for i in l:
#     l[x]=i*i
#     x=x+1
# print(l)    



# add tree list elemnet 
# l3=[4,5]
# l=[1,2,3,4,5]
# l2=[3,4,5,6]

# def add(x,y,z):
#     return x+y+z
# res=map(add,l3,l2,l)
# print(tuple(res))                      
 

 
# l1,l2,l3=[1,2,3,4],[5,6,7,8],[9,10,11,12]
# def add(x,y,z):
#     return x+y+z
# print(list(map(add,l1,l2,l3)))



# filter ()

# filter systax
# iterable 
# def fun_name(n)
#    code 
    #  retunr 
# res =filter(fun_name,iratbale)



# s=[50,60,65,70,30,30,90]
# def division(n):
#     if n>=60:
#         return n
# print(list(filter(division,s))) 


# even find in collection
# n=eval(input("enter any collection:"))
# def division(n):
#     if n%2==0:
#         return n
# print(list(filter(division,n))) 


# odd find in collection
# n=eval(input("enter any collection:"))
# def division(n):
#     if n%2!=0:
#         return n
# print(list(filter(division,n)))    

# s=input("enter any string:")
# def string(n):
#     # if n=='a' or n=='e' or n=='i' or n=='o' or n=='u'or n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
#     if n in('a','e','i','o','u','A','E','I','O','U'):
#         return n
# res=list(filter(string,s))
# print(''.join(res))  

# s=input("enetr any string:")
# # s1=''
# v=0
# for i in s:
#     if i in('a','e','i','o','u','A','E','I','O','U'):
#         # s1=''.join([s1,i])
#         v=v+1
        
# print(v) 


# count vowel and count 
s=input("enetr any string:")
v,c=0,0
for i in s:
    if i in('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    elif i==' ':
        pass
    else:
        c=c+1     
        
print(c,v)  




# iterable 
# def function name():
#     Code 
#     return
# res =functools.reduce(funname,itrable,intial valed)     
  
           
