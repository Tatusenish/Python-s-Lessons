user_list = input("Enter your sentence: ")
modify_string = user_list.split()
print(modify_string)
num = 1
for el in range(len(modify_string)):
    if len(modify_string[el]) <= 10:
        print(num, modify_string[el])
        num += 1
    else:
        print(num, (modify_string[el][0:10]))
        num += 1

