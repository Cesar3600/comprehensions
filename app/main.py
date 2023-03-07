import utils

key,values = utils.get_population()
print(key , values)



data = [
    {'Country':'Bolivia','Population':3000},
    {'Country':'Peru','Population':1500},
    {'Country':'Argentina','Population':2000},
    {'Country':'Colombia','Population':3500}
]

country = input('Tipea tu pais => ')

result = utils.population_by_country(data,country)
print(result)
