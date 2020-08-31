div1 = input("Enter a dividend: ")
div2 = input("Enter a divider: ")

result = 0

try:
    div1 = int(div1)
    div2 = int(div2)
    result = div1 / div2
    print(result)
except ValueError:
    print("Please, enter only integer-valued number")
except ZeroDivisionError:
    print("You can't divide by zero. Try again.")
