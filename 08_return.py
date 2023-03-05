
def sum_with_rage(min,max):
  sum = 0
  for x in range(min,max):
    sum += x
  return sum


result = sum_with_rage(2,7)
print(result)

result2 = sum_with_rage(result,result + 10)
print(result2)


