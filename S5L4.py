from functools import reduce

my_list = range(100, 1001)
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)


def my_func(prev_el, el):
    return el * prev_el


print(reduce(my_func, new_list))
