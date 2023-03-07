
def get_population():
    keys = ['colombia','bolivia']
    values= [300,400]
    return keys,values

def population_by_country(data,country):
    return list(filter(lambda item : item['Country'] == country,data))

