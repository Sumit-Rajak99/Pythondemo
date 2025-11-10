num=int(input("enter any number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("perfact number")
else:
    print("not")                