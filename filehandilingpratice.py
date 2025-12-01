f=open("ram.txt","w+")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)

data="this is pratice\n "
f.write(data)
f.closed

data1="hy sid how are you\n"
data2="hy sid how are you\n"
data3="hy sid how are you\n"
data4="hy sid how are you\n"
f.writelines([data1,data2,data3,data4])
d="how"
d1="are "
d2="you"
f.writelines([d,d1,d2])


data=f.readline()
print(data)
f.close()

