import random
'''
dict = {}
for i in range(1,5):
    dict[i] = i * 2

print(dict)


dict_2 = {i:i*2 for i in range(1,5)}

print(dict_2)
'''

'''
countries = ['col','mex','bol','pe']
population = {}

for country in countries:
    population[country] = random.randint(1,100)

print(population)


population_2 = { country: random.randint(1,100) for country in countries}
print(population_2)

'''

names = ['Charo','Delia','Karen', 'Mikaela']
ages=[19, 30, 24, 1]

family = {}
i=0
for name in names:
    family[name]=ages[i]
    i+=1
      
print(family)


family_2 = {name:ages[names.index(name)] for name in names}
print(family_2)



new_dic = {name:age for (name,age)in zip(names,ages)}
print(new_dic)

print(list(zip(names,ages)))












