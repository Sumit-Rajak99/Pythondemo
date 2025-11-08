# # l=[1,2,3,4,5,6,7,8]
# # print(list(map(lambda n: n*n,l)))

# # l=[1,2,3,4,5,6,7,8,9]
# # print(list(map(lambda n: 'even' if n%2==0 else 'odd',l)))


# # l=[1,2,3,4,5,6,7,8,9]
# # print(list(map(lambda n: 'odd' if n%2!=0 else 'even',l)))



# # filter with lamda 
# # l=[1,2,3,4,5,6,7,8,9]
# # print(list(filter(lambda n: n if n%2==0 else None,l)))



# # l=[1,2,3,4,5,6,7,8,9]
# # print(list(filter(lambda n: n if n%2!=0 else None,l)))



# # reduce with function 

# from functools import reduce
# # l=[1,2,3,4,5,5,6,6,9,77,87654,323456,765,43,56,654]
# # print(reduce(lambda x,y : x if x>y else y,l))


# l=[1,2,3,4,5,5,6,6,9,77,87654,323456,765,43,56,654]
# print(reduce(lambda x,y : x if x<y else y,l))