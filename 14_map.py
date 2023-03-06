########################
numbers = [1,2,3,4]

numbers_v2 =[]

for num in numbers:
    numbers_v2.append(num * 2)

print(numbers)
print(numbers_v2)

#########################

numbers_v3 = map(lambda num : num * 2, numbers)
print(list(numbers_v3))


##########################

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

results = map(lambda x,y: x+y,numbers_1,numbers_2)
print(list(results))
