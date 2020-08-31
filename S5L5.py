with open("text5.txt", "w", encoding="utf-8") as my_file:
    number_list = input("Enter your numbers: ").split()
    print(number_list)
    sum_part = 0
    sum = 0
    for el in number_list:
        sum_part = sum_part + int(el)
    print(sum_part)
    sum += sum_part


    my_file.writelines(number_list)


