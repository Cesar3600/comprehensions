

# funcion tradicional
def increment(x):
  return x + 1;

result = increment(5)
print(result)

#funcion lambda
increment2 = lambda x: x + 1
print(increment2(12)) 




full_name = lambda name,last_name : f"{name.title()} {last_name.title()}"

print(full_name("catherine","contreras"))