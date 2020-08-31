def my_func(x, y):
    if y == 0:
        print("1")
    elif y > 0:
        print("No. You must enter negative number.")
    else:
        y = y * (-1)
        result = 1 / (x ** y)
        return result
print(my_func(2, -2))
