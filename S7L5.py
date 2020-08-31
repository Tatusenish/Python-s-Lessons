import json
with open("text7.txt", "r", encoding="utf-8") as my_file:
    income = {}
    common_income = 0
    average_incom = 0
    el = 0
    for line in my_file.readlines():
        print(line)
        entermed_list = line.split()
        print(entermed_list)
        firm_name = entermed_list[0]
        ownership_form = entermed_list[1]
        revenue = entermed_list[2]
        costs = entermed_list[3]
        income[firm_name] = int(revenue) - int(costs)
        print(income)
        if income.setdefault(firm_name) >= 0:
            common_income = common_income + income.setdefault(firm_name)
            el += 1
    if el != 0:
        average_incom = common_income / el
        average_incom = round(average_incom)
        print(f'Прибыль средняя: {average_incom}')
with open('text7.json', 'w') as new_file:
    json.dump(income, new_file)




