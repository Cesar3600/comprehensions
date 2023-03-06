import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda total,num : total + num, numbers)
print(result)
