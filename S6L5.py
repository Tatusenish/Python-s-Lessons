from typing import List

with open("text6.txt", "r", encoding="utf-8") as my_file:
    result = {}
    for line in my_file.readlines():
        print(line)
        entermed_list = line.split()
        print(entermed_list)
        sub = entermed_list[0]
        lect = int(entermed_list[1])
        pract = int(entermed_list[2])
        lab = int(entermed_list[3])
        result[sub] = lect + pract + lab

    print(result)

