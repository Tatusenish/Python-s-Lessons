class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def V_calculate(self):
        return self.V / 6.5 + 0.5

    def H_calculate(self):
        return self.H * 2 + 0.3

    @property
    def result_sum(self):
        return str(f'Ткани понадобится на пальто и костюм:  \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.V_calculate = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани понадобится на пальто:  {self.V_calculate}'


class Costume(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.H_calculate = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Ткани понадобится на костюм:  {self.H_calculate}'

coat = Coat(20, 10)
costume = Costume(3, 15)
print(coat)
print(costume)
print(coat.result_sum)
print(costume.result_sum)


