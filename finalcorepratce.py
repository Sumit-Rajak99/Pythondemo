# # l=[1,2,3,44,5,44,5]


# # print(l.count(5))
# # print(l.index(5))
# # l.append(10)
# # l2=l
# # print(l2)
# # l.sort()
# # l2=l 
# # print(l2)
# # l.remove(5)
# # l2=l
# # print(l2)
# # l2=l.append(10)
# # print(l2)

# # print(l)
# # print(l.pop(1))
# # print(l)
# # print(id(l))
# # l2=l.copy()
# # print(l2)
# # print(id(l2))

# # l.insert(1,2)
# # l2=l
# # print(l2)

# # l1=[1,2,3,3,4,55,4]
# # l2=[1,2,3,3,4,4,3,3,2,5]
# # print(l1%l2)

# # tupples


# t=(342,45,35,647,75,785,7,3,7)
# # print(max(t))
# # print(t.count(7))
# # print(t.index(7))
# # print(t.)





# dict 


# d={"name":"sumit",
#    "age":19,
#    "course":"fullsatck",
   
#    }
# print(len(d))
# print(d.keys())
# print(d.get("name"))
# print(d.values())
# d1=d.items()
# print(type(d1))


# print(d.fromkeys("age"))




# for i in range(1,11):
#    if i==5:
#       continue
#    else:
#       print(i)


# for i in range(1,10):
#    if i==2:
#       pass
#    else:
#       print(i) 
   
   
   
   
   #  output
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# num=int(input("enter row number :"))
# for j in range(1,num+1):
#    for i in range(1,num+1):
#       print(i,end=" ")
#    print()  

# num=int(input("enter any number: "))
# for i in range(1,num+1):
#    for j in range(1,num+1):
#       print(j,end=" ")
#    print()   
   
   
# num=int(input("enter row number:"))
# for j in range(1,num+1):
#     for i in range(1,num+1):
#         print(i,end=' ')
#     print() 



# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num=int(input("enetr row number :"))
# for j in range(1,num+1):
#    for i in range(1,j+1):
#       print(i,end=" ")
#    print()   


# num=int(input("enter any number: "))
# for i in range(1,num+1):
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print()   




   
   
   
# 1
# 2 3
# 4 5 6
# 7 8 9 10   

# num=1
# for j in range(1,5):
#    for i in range(j):
#       print(num,end=" ")
#       num=num+1
#    print()   
   


# num=int(input("enter row number:"))
# for j in range(1,num+1):
#     for i in range(1,j+1):
#         print(i*2,end=' ')
#     print()    
   
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10


# WAP to print below menetion pattern.
# num = 2
# for i in range(1, 5):  
#     for j in range(i):
#         print(num, end=" ")
#         num=num+2
#     print() 
# 2
# 4 6
# 8 10 12
# 14 16 18 20
# 22 24 26 28

# num=int(input("enter row number :"))
# for i in range(1,num+1):
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print()   

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5




# num=int(input("enter ow number: "))
# for i in range(1,6):
#    for j in range(1,i+1):
#       print(j*2,end=" ")
      
#    print()   

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10


# num=int(input("enter row number :"))
# for i in range(1,num+1):
#    for j in range(1,num+1):
#       print(j,end=" ")
#    print()   

# n='A'
# num=int(input("enter row number:"))
# for i in range(1,num+1):
#    ch='A'
#    for j in range(1,num+1):
#       print(ch,end=" ")
#       ch=chr(ord(ch)+1)
#    print()   
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E



# n='A'
# # y=chr(ord(n)+1)
# # print(y)

# num=int(input("enter number of row:"))
# for i in range(1,num+1):
#     ch='A'
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print() 

# # output
# # A
# # A B
# # A B C
# # A B C D
# # A B C D E



# n='A'
# num=int(input("enetr any number: "))
# for i in range(1,num+1):
#    ch='A'
#    for j in range(1,i+1):
#       print(n,end=" ")
#       n=chr(ord(n)+1)
#    print()   

# A
# B C
# D E F
# G H I J
# K L M N O



# num=int(input("enetr any numbre:"))
# for i in range(1,num+1):
#    ch='A'
#    for _ in range(1,i+1):
#       print(ch,end=" ")
#       ch=chr(ord(ch)+2)
#    print()   
# A
# A C
# A C E
# A C E G
# A C E G I


# num=int(input("enter any number"))
# i=num
# while i>=1:
#    print(" "*(num-i)+"*"*i)
#    i=i-1

# n=int(input("enter any number :"))
# i=n
# while i>=1:
#     print('*'*i)
#     i=i-1




# num=int(input("enter any number: "))
# i=1
# while i<=num:
#    if i%2==0:
#       print(i)
#    i=i+1   