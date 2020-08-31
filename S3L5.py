with open("text3.txt", "r", encoding="utf-8") as my_file:
    suma = 0
    n = 0

    for i in my_file:
        namelist = i.split()
        salary = float(namelist[1])
        suma += salary
        n += 1
        if salary < 20000.00:
            print(namelist[0])

print("The average salary is: ", (suma/n))

