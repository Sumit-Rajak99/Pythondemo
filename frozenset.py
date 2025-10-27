
# frozenset = collection of unique element 
# represent by frozenset({}) and with comma(,) sepereted by element
# unordered collection 
# indexing not supported
# sliceing not suppoerted
# mutable in nature 

# l=['10','20','30','python','java']
# fs=frozenset(l)
# print(fs, type(fs))


# inbuld function of python on frozenset

# print(sum(fs))
# print(max(fs))
# print(min(fs))


# print(len(fs))
# print(id(fs))
# print(type(fs))



# inbulid function in python on frozenset 

l=[10,20,30,'pyhton','java',40,50]
fs1=frozenset(l)
j=[50,40,30,'pyhton','java']
fs2=frozenset(j)
print(fs1,fs2)


# union

# print(fs1.union(fs2))

# intersection
# print(fs1.intersection(fs2))


# diffrence
# print(fs1.difference(fs2))


# .symmentic_diffrence 
# print(fs1.symmetric_difference(fs2))

# isdisjoint 

# print(fs1.isdisjoint(fs2))

# issubset /

# print(fs1.issubset(fs2))
# print(fs2.issubset(fs1))

# issuperse 

# print(fs1.issuperset(fs1))
# print(fs2.issuperset(fs1))