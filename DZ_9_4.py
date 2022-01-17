class Car:
    """Auto"""

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'New car: {self.name}, color: {self.color}, police car: {self.is_police}')

    def going(self):
        print(f"{self.name} let's starting")

    def stopped(self):
        print(f"{self.name} let's stopped")

    def turn(self, direction):
        print(f'{self.name} повернула: {"направо" if direction == 0 else "направо"}')

    def show_speed(self):
        return f'{self.name} поехал со скоростью {self.speed} км\ч.'


class TownCar(Car):
    '''Городской автомобиль'''

    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed} км\ч. Превышение скорости!' \
            if self.speed > 60 else f'{self.name} поехал со скоростью {self.speed} км\ч'


class SportCar(Car):
    '''Спортивный автомобиль'''

    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed} км\ч. Превышение скорости!' \
            if self.speed > 60 else f'{self.name} поехал со скоростью {self.speed} км\ч'


class WorkCar(Car):
    '''Грузовой автомобиль'''

    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed} км\ч. Превышение скорости!' \
            if self.speed > 40 else f'{self.name} поехал со скоростью {self.speed} км\ч.'


class PoliceCar(Car):
    '''Полицейская машина'''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('Nissan', 'фиолетовый', 265)
police_car.going()
print(police_car.show_speed())
police_car.turn(0)
police_car.stopped()
print()

work_car = WorkCar('Mercedes-Benz', 'белый', 45)
work_car.going()
print(work_car.show_speed())
work_car.turn(0)
work_car.stopped()
print()

town_car = TownCar('Honda', 'салатовый', 55)
town_car.going()
print(town_car.show_speed())
town_car.turn(1)
town_car.stopped()
print()

sport_car = SportCar('Pagani', 'оранжевый', 198)
sport_car.going()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.stopped()
