number = int(input("Enter number of elements: "))
i = 0
my_list = []
while i < number:
    my_list.append(input("Enter your list: "))
    i += 1

print(my_list)

el = 0
for el in range(1, len(my_list), 2):
    my_list[el-1], my_list[el] = my_list[el], my_list[el-1]
    el += 2

print(my_list)
