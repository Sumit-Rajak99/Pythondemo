# def decore(fun_name):
# 2	    def inner(x,y):
# 3	        x=x+5
# 4	        y=y+10
# 5	        fun_name(x,y)
# 6	    return inner
# 7	    
# 8	@decore    
# 9	def add(x,y):
# 10	    print(x+y)
# 11	    
# 12	add(10,20)



# internal syntax 

# def outer_fun(function_name):
#     def innner_fun(parameter1):
#         modification on 
#         parameters
#         function_name(MODIFIER Parameters)
#     return innner

# def fun_name(parameter2):
#     perform opration on parameter2

# res=outer_fun(fun_name)
# res()


# note = total no. of parameter1= total no of parameter2




# jo sysnatax  jo ham ham padhage 

# def outer_function(fun_name):
#     def innner_fun(parmeter1):
#         modifaction on parameter1
#         fun_name(modification parameters)
        
#     return inner 
# @outer_function
# def fun_name(parameter1):
#     opration on parameter1
    
# res = fun_name(parameter)
# print(res)               