# syntex of index=index bdefualt it work on the positive direction
# 1.collection.index('element',start,stop)\ must be positive
# 2.collection.index('element')
# 3.collection.index('element',start)

s='python'
print(s.index('t'))
# print(s.index('t',3))
# print(s.index('t',2))
# print(s.index('t',1,2))

print(s.index('t',-1,-6))