x = int(input("Enter any number: "))
count = 0

for i in range(1, x + 1):
    if x % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not prime")
