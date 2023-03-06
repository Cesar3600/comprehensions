'''
items = [
    {'product':'camisa', 'price':100},
    {'product':'pantalones', 'price':300},
    {'product':'pantalones 2', 'price':200}
]

prices = list(map(lambda item:item['price'], items))

print(prices)




def add_taxes(item):
  item['taxes'] = item['price'] * 0.19
  return item

response = list(map(lambda item :add_taxes(item),items))
print(response)

'''



#add_taxes(items)

#new_prices = list(map(lambda item : item['taxes'] = item['price'] * 0.19, items))
#print(new_prices)

'''
items = [
    {'product':'camisa', 'price':100},
    {'product':'pantalones', 'price':300},
    {'product':'pantalones 2', 'price':200}
]

def process(item):
  item['taxes'] = item['price'] * 0.18
  return item

new_item_v2 = list(map(lambda item : process(item), items))
print(new_item_v2)

'''

#################################################################

items = [
    {'product':'camisa', 'price':100},
    {'product':'pantalones', 'price':300},
    {'product':'pantalones 2', 'price':200}
]

igv = 0.18

def change_items(item):
    item['taxes'] = item['price'] * igv
    return item

items_with_igv = list(map(change_items,items))

print(items_with_igv)
print('#'*33)
print(items)