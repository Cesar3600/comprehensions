def my_divide(a, b):
   # Escribe tu solución 👇
   try:
    if a==0 or b==0:
      raise ZeroDivisionError('No se puede dividir por 0')
   except ZeroDivisionError as error:
      return error 
   return a/b

response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0

