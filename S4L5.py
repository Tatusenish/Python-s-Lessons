with open("text4.txt", "r", encoding="utf-8") as my_file:
    rename_list = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
    new_file = []
    i = 0
    for line in my_file.readlines():
        number_list = line.split()
        #print(number_list)
        for item in number_list:
            if item in rename_list:
                number_list[i] = rename_list[item]

        # for (offset, item) in enumerate(number_list):
        #     if rename_list.setdefault(item) is not None:
        #         number_list[offset] = rename_list.setdefault(item)
        print(number_list)
           # word = rename_list[number_list[0]]
        new_file.append(number_list[0] + " - " + number_list[1] + "-" + number_list[2])
with open("text4(new).txt", "w", encoding="utf-8") as my_file2:
    my_file2.writelines(new_file)
