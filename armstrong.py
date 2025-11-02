num=int(input("enter any number:"))
sum=0
count=0
y=x=num
while num>0:
    count=count+1
    num=num//10
while x>0:
    lastdigit=x%10
    sum=sum+lastdigit**count  
    x=x//10
if y==sum:
    print(f'{y} is armstrong number ')
else:
    print(f'{y} is not armstrong number')           