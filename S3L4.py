my_list = range(20, 241)
new_obj = (el for el in my_list if el % 21 == 0 or el % 20 == 0)
for el in new_obj:
    print(el)