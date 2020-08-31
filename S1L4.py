from sys import argv
script_name, earning_time, hourly_rate, bonus = argv
earning_time = int(earning_time)
hourly_rate = int(hourly_rate)
bonus = int(bonus)
print(f"Salary is: {earning_time * hourly_rate + bonus}")
