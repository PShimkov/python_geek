##TASK 1
#class Data:
#    def __init__(self, day_month_year):
#        # self.day = day
#        # self.month = month
#        # self.year = year
#        self.day_month_year = str(day_month_year)
#
#    @classmethod
#    def method_class(cls, day_month_year):
#        my_date = []
#
#        for i in day_month_year.split():
#            if i != '-':
#                my_date.append(i)
#
#        return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#    @staticmethod
#    def method_static(day, month, year):
#
#        if 1 <= day <= 31:
#            if 1 <= month <= 12:
#                if 2019 >= year >= 0:
#                    return f'All right'
#                else:
#                    return f'Неправильный год'
#            else:
#                return f'Неправильный месяц'
#        else:
#            return f'Неправильный день'
#
#    def __str__(self):
#        return f'Текущая дата {Data.method_class(self.day_month_year)}'
#
#
#today = Data('05 - 06 - 2020')
#print(today)
#print(Data.method_static(1, 1, 20332))
#print(today.method_static(1, 1, 2001))
#print(Data.method_class('22 - 12 - 2010'))
#print(today.method_class('05 - 06 - 2020'))
#print(Data.method_static(5, 6, 2020))
#
##TASK 2
#
#class ExeptZero:
#
#    def __init__(self, upper_number, down_number):
#        self.upper_number = upper_number
#        self.down_number = down_number
#
#    @staticmethod
#    def my_func(upper_number, down_number):
#        try:
#            return (upper_number/down_number)
#        except:
#            print ("Деление на ноль")
#
#first_class = ExeptZero
#print(first_class.my_func(100, 0))
#print(first_class.my_func(100, 10))
#
#TASK 3

#class Error:
#    def __init__(self, *args): #не знаю как лучше сделать без args
#        self.my_list = []
#
#    def my_input(self):
#        while True:
#            try:
#                val = int(input('Введите значения и нажимайте Enter - '))
#                self.my_list.append(val)
#                print(f'Текущий список - {self.my_list} \n ')
#            except:
#                print(f"Недопустимое значение - строка и булево")
#                y_or_n = input(f'Попробовать еще раз? Y/N ')
#
#                if y_or_n == 'Y' or y_or_n == 'y':
#                    print(try_except.my_input())  #подмотрел решение потому, что хотел использовать в коде возврат к будущему экземпляру.
#                elif y_or_n == 'N' or y_or_n == 'n':
#                    return f'Вы вышли'
#                else:
#                    return f'Вы вышли'
## честно растерялся с этой задачей, поэтому такое знакомый код ... можете подсказать как лучше?
#try_except = Error(1)
#print(try_except.my_input())

from abc import ABC, abstractmethod

class Store:

    def __init__(self):
        self.position = input("position: ")
        self.units = input("unit: ")
        self.store = []
        self.my_unique = {'Место на складу:': self.position, 'Колличество': self.units}

    def test_type(self):
        try:
            self.position_1 = int(self.position)
            self.units_1 = int(self.units)
        except:
            return f'Ошибка ввода данных'

    def in_to_store(self):
        unique = {'Место на складу:': self.position, 'Колличество': self.units}
        self.my_unique.update(unique)
        self.store.append(self.my_unique)
        print(f'Текущий список: {self.store}')



    def __str__(self):
        return f"Место на складу: {self.position}, Количество: {self.units}"

class Tech(ABC):

    def __init__(self):
        self.name = input("name: ")
        self.price = input("price: ")
        self.maker = input("maker :")

    @abstractmethod
    def about_tech(self):
        pass

class Xerox(Tech):

    @property
    def about_tech(self):
        return f'Название: {self.name}, Цена: {self.price}, Производитель: {self.maker}'

class Printer(Tech):

    @property
    def about_tech(self):
        return f'Название: {self.name}, Цена: {self.price}, Производитель: {self.maker}'

class Scan(Tech):

    @property
    def about_tech(self):
        return f'Название: {self.name}, Цена: {self.price}, Производитель: {self.maker}'

a = Xerox()
b = Store()
print(a.about_tech, b.in_to_store())
