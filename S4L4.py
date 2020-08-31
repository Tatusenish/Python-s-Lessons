import random

my_list = []
for el in range(15):
    my_list.append(random.randint(0, 100))
print(my_list)
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_obj = (el for el in my_list if my_list.count(el) == 1)
for i in new_obj:
    print(i)
