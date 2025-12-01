# def sum(n):
#     yield n*n 

# n=int(input("enetr any number :"))
# # print(sum(n))
# ans=sum(n)
# print(next(ans))    


# n=int(input("enetr any number :"))
# for i in range(1,n+1):
#     yield i
    
#  ans=i
#  print(next(ans))   



def gen_number(n):
    i=1
    while i<=n:
        yield i
        i=i+1
        
n=int(input("enter any number :"))
var=gen_number(n)
for i in var:
    print(i)
    