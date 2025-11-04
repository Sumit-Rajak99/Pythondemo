while True:
    print("1 for + \n 2 for - \n 3 for * \n 4 for / \n 5 for 0ff")
    n=int(input("enter any one option:"))
    x=(1,2,3,4,5)
    if n in x:
        y=(1,2,3,4)
        if n in y:
            if n==1:
                tn=int(input("enter how many number want you add:"))
                l=[]
                for i in range(1,tn+1):
                    value=int(input("enter value:"))
                    l.append(value)
                sum=0
                for i in l:
                    sum=sum+i
                print(f'sum of given value {l} is {sum}')
            elif n==2:
                tn=int(input("enter how many number want you add:"))
                l=[]
                for i in range(1,tn+1):
                    value=int(input("enter value:"))
                    l.append(value)
                
                for i in l:
                    sub=0
                    sub=sub-i
                print(f'sub of given value {l} is {sub}')
                            
        else:
            break
      
    else:
        print("please enter valid option")