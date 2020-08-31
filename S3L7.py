class Box:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return f'The result {self.value * "*"}'

    def __add__(self, other):
        return Box(self.value + other.value)

    def __sub__(self, next):
        if (self.value - next.value) > 0: return self.value - next.value
        else:
            print('Negative!')

    def __mul__(self, next):
        return Box(int(self.value * next.value))

    def __truediv__(self, next):
        return Box(round(self.value // next.value))


    def make_order(self, box_in_row):
        row = ''
        for i in range(int(self.value / box_in_row)):
            row += f'{"*" * box_in_row} \\n'
        row += f'{"*" * (self.value % box_in_row)}'
        return row

box_1 = Box(12)
box_2 = Box(7)
print(box_1)
print(box_1 + box_2)
print(box_2 - box_1)
print(box_2.make_order(2))
print(box_1.make_order(4))
print(box_1 / box_2)

