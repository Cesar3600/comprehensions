

set_countries  = {'col','mex','bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# ADD
set_countries.add('pe')
print(set_countries)


# UPDATE
set_countries.update({'ar','ecua','pe'})
print(set_countries)


# REMOVE
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

#set_countries.remove('cl')

set_countries.discard('cl')
print(set_countries)

set_countries.add('arg')
print(set_countries)


set_countries.clear()
print(set_countries)






