# # copy()=create new object with same element
# # clear()=remove all elements from given list
# # append()=add single element at last position
# # extend()=add multiple elements at last position
# # pop()=remove index targeted element by -default index is -1 that by remove last element 
# # remove()=remove targeted element from list
# # index()=return index no. against given element 
# # count()=findout frequency /occurece of any element
# # sort()=arrange in assending order
# # reverse()=reverse out all element from list
# # insert()=add element in  targeted position



# # copy 
# # l=[2,4,6,'python','java']
# # l1=l.copy()
# # print(l,l1,id(l),id(l1))


# # # clear
# # l.clear()
# # print(l,id(l))
# # # del l remove object from del 
# # print(l)



# # s='python'

# # print(s)
# # del s
# # print(s)

# # append()
# l=[2,4,6,'python','java']
# l.append('php')
# print(l)

# l.append([1,2,3,4])
# print(l)



# .exend()
# l=[2,3,4,5,6,'python']
# l.extend([12,34,56,'java'])
# print(l)
# l.extend('python')



# insert()

# l=[2,4,6,8]
# l.insert(0,100)
# print(l)
# # inetrveiw question
# l.insert(100,'python')
# print(l)

# l.insert(2,[12,34,24,34,23])
# print(l)



# pop()

# l=[2,4,6,8,'python']
# # print(l.pop())
# # print(l)


# # error genarate
# # print(l.pop(5))
# print(l.pop(2))
# print(l)	




# # remove()

# l=[2,4,6,8,'python',6]
# l.remove(6)
# print(l)



# index()
# l=[2,4,6,8,'python',6,6]

# first=l.index(6)
# sec_element=l.index(6,(first+1))
# # print(sec_element)
# print(l.index(6,(l.index(6)+1)))



# count()

# l=[1,2,4,3,2,4,2,3,42,2,2,2]
# print(l.count(0))


# # sort()
# l=[4,3,5,6,78,2,1]
# l.sort()
# print(l)



# revese()
# l=[4,3,5,6,78,2,1]
# l.reverse()
# print(l)

# decangin
l=[4,3,5,6,78,2,1]
l.sort(reverse=True)
print(l)