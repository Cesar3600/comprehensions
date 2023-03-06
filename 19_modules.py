'''
import sys, functools

print(sys.path)

import re

text = 'Mi numero de telefono 967007433, el codigo del pais es +52 y mi numero de la suerte es el 333 direccion calle trabajo 27A amazonas'
resolve = re.findall("[0-9]+",text)

print(resolve)

'''



'''
import time

timestamp = time.time()
print(timestamp)

'''



'''
import time

timelocal = time.localtime()
result = time.asctime(timelocal)
print(result)

'''



import collections

numbers = [1,1,2,3,4,5,3,4,32,5,21]

counter = collections.Counter(numbers)
print(counter)





