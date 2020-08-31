number_of_goods = int(input("Enter number of goods: "))
i = 1
goods = []
goods_assort = []
goods_analys = {}
while i <= number_of_goods:
    goods_name = input("Enter name: ")
    goods_price = input("Enter price: ")
    goods_count = input("Enter count: ")
    goods_measure = input("Enter measure: ")
    goods = (i, {"name": goods_name, "price": goods_price, "count": goods_count, "measure": goods_measure})
    goods_assort.append(goods)
    i += 1
    goods_analys = {["name"]: [], 'price': [], 'count': [], 'measure': []}
    goods_analys['name'].append(goods_name)
    goods_analys['price'].append(goods_price)
    goods_analys['count'].append(goods_count)
    goods_analys['measure'].append(goods_measure)
    goods_analys['measure'] = list(set(goods["name"]))
    goods_analys['price'] = list(set(goods["price"]))
    goods_analys['count'] = list(set(goods["count"]))
    goods_analys['measure'] = list(set(goods["measure"]))
    print(goods_analys)
