# x=10
# def display():
#     x=20
#     print(x)
# display() 
# print(x)   

# x=20
# def show():
#     x=10
#     print(globals()['x'])
# show()    

# with argument and with return type 

# def add(x,y):
#     return x-y  

# x=int(input("enter any number: "))
# y=int(input("enter any number: "))
# print(add(x,y))

# with  arguument and without return type

# def display(x,y):
#     print(x+y)
# x=int(input("enter any number: "))
# y=int(input("enter any number: "))
# display(x,y)    

# without argumnet and with return type

# def display():
#     return "hello" 
# print(display())



# without argumnet and without return type

# def display():
#     return "test"
# print(display())




# on the  basic of argument

# 1.posotional argument

# def add(c,b,a):
#     print(a+c+b)
# add(10,1,2) 

# defult positnal argument 
# def add(a=0,b=0,z=0):
#     print(a+b+z)
# add(12,3)  


# def add(*n):
#     print(n)
# add(12+3+4)         
    
    
    
    # 4. key-word positonal argument
# def add(x,y,z):
#     print(x+y+z)
# add(x=21,y=4,z=5)   


#  5.     defualt  key-word positonal argument
# def add(x=0,y=0,z=0):
#     print(x+y+z)
# add(12,3,5)    


# def display(**n):
#     for i,j in n.items():
#         print(i,'=',j)
# x=eval(input("enter any value:"))
# display(**x)    


# 1. WAP to print below menetion pattern.
# num=int(input("enter row number:"))
# for j in range(1,num+1):
#     for i in range(1,num+1):
#         print(i,end=' ')
#     print()

# num=int(input("enter row number:"))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(j,end=' ')
#     print()    

# output
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 2. WAP to print below menetion pattern.
# num=int(input("enter row number:"))
# for j in range(1,num+1):
#     for i in range(1,j+1):
#         print(i,end=' ')
    # print() 

# output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 3. WAP to print below menetion pattern.
# num = 1
# for i in range(1, 5):  
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# output
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# 4. WAP to print below menetion pattern.
# num=int(input("enter row number:"))
# for j in range(1,num+1):
#     for i in range(1,j+1):
#         print(i*2,end=' ')
#     print()


# output
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

# 5. WAP to print below menetion pattern.
# num = 2
# for i in range(1, 5):  
#     for j in range(i):
#         print(num, end=" ")
#         num=num+2
#     print()


# output
# 2
# 4 6
# 8 10 12
# 14 16 18 20
# 22 24 26 28
 
 
#6 WAP to print below menetion pattern.
# n = int(input("Enter how many rows you want: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 7. WAP to print below menetion pattern.
# n = int(input("Enter how many rows you want: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j*2, end=" ")
#     print()

# output
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

#  8. WAP to print below menetion pattern.
# n='A'
# num=int(input("enter any number: "))
# for j in range(1,num+1):
#     ch='A'
    
#     for i in range(1,num+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()    
    

# output
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# 9. WAP to print below menetion pattern.
# n='A'
# y=chr(ord(n)+1)
# # print(y)

# num=int(input("enter number of row:"))
# for i in range(1,num+1):
#     ch='A'
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print() 

# output
# A
# A B
# A B C
# A B C D
# A B C D E

# 10 WAP to print below menetion pattern.
# n='A'
# num=int(input("enter how many row"))
# for i in range(1, num+1):
#     for j in range(1,i+1):
#         print(n,end=' ')
#         n=chr(ord(n)+1)
#     print() 

# output
# A
# B C
# D E F
# G H I J
# K L M N O
        
        
# 11. WAP to print below menetion pattern.
# num=int(input("enter number of row:"))
# for i in range(1,num+1):
#     ch='A'
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+2)
#     print() 

# output
# A
# A C
# A C E
# A C E G
# A C E G I

# 12. WAP to print below menetion pattern.

# n = int(input("Enter how many rows you want: "))
# for i in range(1, n + 1):
#     ch='A'
#     print(" " * (n - i), end="")
#     for j in range(1, i +1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()
    
#   output  #
# A
# A B
# A B C
# A B C D
# A B C D E 
    
# 13. WAP to print below menetion pattern.
# n = int(input("Enter how many rows you want: "))
# ch='A'
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i +1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()  

# output
# A
# B C
# D E F
# G H I J
# K L M N O

#  14. WAP to print below menetion pattern./ /
# n = int(input("Enter how many rows you want: "))
# for i in range(1, n + 1):
#     ch='A'
#     print(" " * (n - i), end="")
#     for j in range(1, i +1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+2)
#     print()
# output
# A
# A C
# A C E
# A C E G
# A C E G I


# 15. WAP to print below menetion pattern.

# n=int(input("enter any number :"))
# i=1
# while i<=n:
#     print('*'*i)
#     i=i+1

# output
# *
# * *
# * * *
# * * * *
# * * * * *



# 16. WAP to print below menetion pattern.
# n=int(input("enter how many row:"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i=i+1
# output
#     *
#    **
#   ***
#  ****
# *****
  
  
  
#  17. WAP to print below menetion pattern.

# n=int(input("enter how many row: "))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i=i+1
# output 
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *


 #18. WAP to print below menetion pattern.
# n=int(input("enter any number :"))
# i=n
# while i>=1:
#     print('*'*i)
#     i=i-1
# output

# *****
# ****
# ***
# **
# *


# 19. WAP to print below menetion pattern.
# n=int(input("enter how many row:"))
# i=n
# while i>=1:
#     print(' '*(n-i)+'*'*i)
#     i=i-1
# output
# *****
#  ****
#   ***
#    **
#     *
   

#20. WAP to print below menetion pattern.
# n=int(input("enter how many row: "))
# i=n
# while i>=1:
#     print(' '*(n-i)+'* '*i)
#     i=i-1  

# output
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *


# 21. WAP to print below menetion pattern.
# n = int(input("Enter how many rows: "))
# i = 1
# while i <= n:
#     print('*' * i)
#     i=i+ 1
# i = n - 1
# while i >= 1:
#     print('*' * i)
#     i=i-1

# output
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



# 22. WAP to print below menetion pattern.
# n = int(input("Enter how many rows: "))
# i = 1
# while i <= n:
#     print(' ' * (n - i) + '*' * i)
#     i =i+ 1
# i = n - 1
# while i >= 1:
#     print(' ' * (n - i) + '*' * i)
#     i=i-1
# output
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# 23. WAP to print below menetion pattern.

# n=int(input("enter how many row: "))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i=i+1
# i=i-1
# while i>=1:
#     print(' '*(n-i)+'* '*i) 
#     i=i-1   

# output 
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *



# 24. WAP to print below menetion pattern.

# n=int(input("enter how many row:"))
# i=n
# while i>=1:
#     print(' '*(n-i)+'*'*i)
#     i=i-1
# i=i+2
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i=i+1   
#   output 
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****
   
# 25. WAP to print below menetion pattern.
# n=int(input("enter any number :"))
# i=n
# while i>=1:
#     print('*'*i)
#     i=i-1
# i=i+2
# while i<=n:
#     print('*'*i)
#     i=i+1  
  
# output
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

