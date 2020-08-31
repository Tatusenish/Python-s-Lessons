seasons = {"winter": (1, 2, 12), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
user_date = int(input("Enter the date of month (1-12): "))
if user_date > 12:
    print("Error! It's not a month.")
for key in seasons.keys():
    if user_date in seasons[key]:
        print(key)
    else:
        break
