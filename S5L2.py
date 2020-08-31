my_list = [8, 6, 6, 5, 3, 3, 3, 2, 1, 1]
print(my_list)
number = int(input("Enter your number: "))
for el in range(len(my_list)):
    if my_list[el] == number:
        my_list.insert(el + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
        break
    elif my_list[-1] > number:
        my_list.append(number)
        break
    elif my_list[el] > number and my_list[el + 1] < number:
        my_list.insert(el + 1, number)
        break

print(my_list)