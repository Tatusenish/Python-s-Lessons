stop = True
sum = 0
while stop:
    user_list = (input("Enter numbers: ")).split()
    print(user_list)
    sum_part = 0
    for el in user_list:
        if el == "$":
            stop = False
            break
        else:
            sum_part = sum_part + int(el)
    print(sum_part)
    sum += sum_part
    print(sum)






