items = [
    {'product':'camisa', 'price':100},
    {'product':'pantalones', 'price':300},
    {'product':'pantalones 2', 'price':200}
]


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes,items))

print('New List'.upper())
print(new_items)
print('old List'.upper())
print(items)