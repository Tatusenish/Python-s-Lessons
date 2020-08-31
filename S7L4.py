import functools
n = 5
my_list = range(n, n+1)
new_obj = (el for el in my_list if el == n)
for el in new_obj:
    print(new_obj)

def fact(n):
    yield n*n
print(fact(5))

