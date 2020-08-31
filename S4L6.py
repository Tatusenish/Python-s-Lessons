class Cars:
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car on a way"
    def stop(self):
        return "The car stopped"
    def turn(self, direction):
        return "The car go to " + direction

class TownCar(Cars):
    def __init__(self, name, speed, color, my_car = True):
        super().__init__(name, speed, color)
        self.my_car  = my_car

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

kia = TownCar('mustang', 150, 'black')
print(kia.name, kia.color, kia.speed, kia.is_police)
print(kia.go(), kia.turn('City'), kia.stop())
sport = SportCar('kia', 90, 'beige')
work1 = WorkCar('kia', 60, 'white', True)
work2 = WorkCar('renault', 90, 'blue', False)
police = PoliceCar('lada', 120, 'red')