
# nature number 
# def nature(n):
#     if n==0:
#         return
#     nature(n-1)
#     print(n)
# n=int(input("enetr any number: "))
# nature(n) 

# reverse number 
# def reverse(n):
#     if n==0:
#         return
#     print(n)
#     reverse(n-1)
# n=int(input("enetr any number :"))
# reverse(n)  

# even 
# def even(n):
#     if n==0:
#         return
#     even(n-1)
#     if n%2==0:
#         print(n*2)
# n=int(input("enetr any number :"))
# even(n)   



# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# n=int(input("enetr any number :"))
# print(sum(n))
         

def even_sum(n):
    if n==1:
        return 2*n-1
    return n-1*2+even_sum(n-1)
n=int(input("enetr any number :"))
print(even_sum(n))
      
       
    