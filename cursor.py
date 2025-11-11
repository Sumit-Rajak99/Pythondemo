cursomr position  
# two type 
# 1=tell()=it show current position of cursor 
# 2 seek()=throuhg this we moves our requred position  

# with open("a5.txt",'r+') as f:
#     print(f.tell())
#     data=f.read(10)
#     print(data)
#     print(f.tell()) 









# seek 
# sysntax      seek("no of moved bit")


# with open("n2.txt",'ab+') as f:
#     print(f.tell())
#     data=b"this is python class"
#     f.write(data)
#     print(f.tell())
#     data1=f.read()
#     print(data1)
#     f.seek(0,0)
#     print(f.tell())
#     data1=f.read(20)
#     print(data1)
#     print(f.tell())

# with open('n1.txt','rb+')as f:
#     print(f.tell())
#     f.read(10)
#     print(f.tell())
#     f.seek(-5,1)
#     print(f.tell())
    
    
    
    
    
with open('sumitrajakresumemsword.docx','rb+') as f:
    print(f.tell())
    data10=f.read(10)
    print(data10)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell())
    f.seek(10,1)
    print(f.tell())
    data5=f.read(5)
    print(data5)
    f.seek(-5,2)
    data5=f.read()
    print(data5)
        
    