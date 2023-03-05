
# higher order function

def increment(x):
    return x + 1

def hight_ord_func(x,func):
    return x + func(x)


result = hight_ord_func(2,increment)
print(result)




increment_v2 = lambda x : x + 1
hight_ord_func_v2 = lambda x,func : x + func(x) 

result_v2 = hight_ord_func_v2(33, increment_v2)


print(result_v2)





