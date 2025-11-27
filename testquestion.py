# 1 wap to find factrial of any number

# num=int(input("enetr any number: "))
# i=1
# multi=1
# while num>=i:
#     multi=multi*i
#     i=i+1
# print(multi) 


# 2 wap  to count the total digit in a number

# num=4536
# i=1
# count=0
# while num>=i:
#     ans=num%10
#     count=count+1
#     num=num//10
#     i=i+1
    
# print(count)   



3    #  wap for age

# age=int(input("enter any number: ")) 

# if age>=0 and age<=12:
#     print("Child")
# elif age>=13 and age<=19:
#     print("Teenagar")
# elif age>=20 and age<=59:
#     print("adult")
# elif age>=60:
#     print("senior citizen")
# else:
#     print("please enter valid age");                
    
    
    
# 4 wap to count occeurnt of all charater within a stroing    # 

# s = input("Enter any string: ")

# count = {}

# for ch in s:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# for ch in count:
#     print(ch, "=", count[ch])



# 5 

# n = int(input("Enter how many rows you want: "))
# ch='A'
# for i in range(1, n + 1):
    
#     for j in range(1, (n-i)+2):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print() 


# 6 wap to check prime number or not

# num=int(input("enetr any number: "))
# count=0
# i=1
# while num>=i:
#      if num%i==0:
#         count=count+1
#      i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("not")    


7    # count and print how many time "football"  appears in list

# s = ["cricket", "football", "tennis", "football", "hockey"]
# count = 0

# for i in s:
#     if i=="football":
#         count=count+1
# print(count)   

# 8. find and print largest and minum number in  list without using max nand min

# l1 = [8, 2, 15, 19]

# min = l1[0]
# max = l1[0]

# for i in l1:
#     if i > max:
#         max = i
#     if i < min:
#         min= i

# print("Max =", max)
# print("Min =", min)



# 9wap to print kry of minium value from the following dictionary

# d = {"math":89,
#      "phy":80,
#      "chem":67,
#      "eng":76}

# smallest = min(d, key=d.get)

# print(smallest)


# 10 find comman elemne t in teo list

# l1=[10,20,30,40]
# l2=[30,40,50,60]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(i)
            
# print(l3)   
         


num=int(input("enter any number: "))
i=1
while num>i:
    print("*"*i)
    i=i+1
        
