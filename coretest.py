
# # num=int(input("enetr any number: "))
# # for i in range(2,num+1,2):
# #     sum=sum+i 
    
# # print(sum)    


# # num=int(input("enetr any numbet: "))
# # i=1
# # sum=0
# # while num>=i:
# #     sum=sum+i
# #     if i<=(num-1):
# #         print(i,end="+")
# #     else:
# #         print(i,end="=") 
# #     i=i+1
# # print(sum)           


# # num=int(input("enetr any number :" ))
# # i=1
# # multi=1
# # while i<=num:
# #     multi=multi*i
# #     if i<=(num-1):
# #         print(i,end="*")
# #     else:
# #         print(i,end="=")
# #     i=i+1
# # print(multi)            


# num=int(input("enetr any numbet: "))
# i=1
# sum=0
# while num>=i:
#     if i%2==0:
#         sum=sum+i
#         print(i,end="+")
#     else:
#         print(i,end="=") 
#     i=i+1
# print(sum)    
           
           
           
num = int(input("enter any number: "))
i = 1
sum = 0

while i <= num:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print(sum)
