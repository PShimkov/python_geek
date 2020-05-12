from time import sleep
from itertools import cycle

#Задача 1
class TrafficLight:
   def __init__(self):
       self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))
   def running(self):
       for color, sec in cycle(self.__color):
           print(color, '(wait {} sec)'.format(sec))
           sleep(sec)
traffic_light = TrafficLight()
traffic_light.running()
#Задача 2
class Road:
    def __init__(self, length, width, mass, heigh):
        self._length = length
        self._width = width
        self.mass = mass
        self.heigh = heigh

    def calc_mass(self):
        mass = self._length * self._width * self.mass * self.heigh / 1000
        print(mass, 'С‚')


 my_road = Road(20, 5000, 25, 5)
 my_road.calc_mass()

#Задача 3
 class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage = income["wage"]
        self.income_bonus = income["bonus"]

 class Position(Worker):

    def get_full_name(self):
         print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self.income_wage + self.income_wage)

 human_1 = Position("Gazman", "Ivanovich", "juniror", {"wage": 15000, "bonus": 1000})

 human_1.get_full_name()#
 human_1.get_total_income()
#Задача 4
 class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = bool(is_police)

    def go(self):
        print('Car {} is go'.format_map(self.name))

    def stop(self):
        print('Car {} is stop'.format_map(self.name))

    def turn(self, direction):
        print('Car {} direction {}'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)

 class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed limit")

 class WorkCar (Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed limit")

 class PoliceCar(Car):
    pass


 town_car = TownCar(60, "Blue", 'Audi', False)
 work_car = WorkCar(50, "Red", 'Mercedes', False)
 police_car = PoliceCar(110, "Black", 'Ford', True)

town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
work_car.turn('left')
town_car.turn('left')

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("draw now")


class Pen(Stationery):

    def draw(self):
        super().draw()
        print("Penceled")

class Pencil(Stationery):

    def draw(self):
        super().draw()
        print("Penciled")

class Handle(Stationery):

    def draw(self):
        super().draw()
        print("Handled")

pen = Pen(Pen)
pen.draw()
pencil = Pencil(Pencil)
pencil.draw()
handle = Handle(Handle)
handle.draw()