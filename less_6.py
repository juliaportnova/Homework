#№1
# from time import sleep
# class Trafficlight:
#     __tr_color = ['Red','Yellow','Green']
#     def switch(self):
#         i = 0
#         while i < 3:
#             print(f'{Trafficlight.__tr_color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(3)
#             i += 1
# Trafficlights = Trafficlight()
# Trafficlights.switch()
#№2
# class Road:
#     def __init__(self,_length,_width):
#         self._length = _length
#         self._width = _width
#     def massa(self,mas=25,tol=5):
#         return self._length * self._width * mas * tol /1000
# r = Road(20,5000)
# print(f'Масса асфальта: {r.massa()} т')
#№3
# class Worker:
#     name = None
#     surname = None
#     position = None
#     _income = None
#     def __init__(self,name,surname,position,wage,bonus):
#         self.name=name
#         self.surname=surname
#         self.position=position
#         self._income={"wage":int(wage),"bonus":int(bonus)}
# class Position(Worker):
#     def __init__(self,name,surname,position,wage,bonus):
#         super().__init__(name,surname,position,wage,bonus)
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#     def get_total_income(self):
#         return sum(self._income.values())
#         # return self._income.get('wage') + self._income.get('bonus')
# a = Position('Dima', 'Ivanov', 'Manager', 90000, 23000)
# print(a.get_full_name())
# print(a.get_total_income())
#№4
# class Car:
#     speed = None
#     color = None
#     name = None
#     is_police = None
#     def __init__(self,speed,color,name,is_police):
#         self.speed=speed
#         self.color=color
#         self.name=name
#         self.is_police=is_police
#     def car_go(self):
#         return f'{self.name} поехала'
#     def car_stop(self):
#         return f'{self.name} остановилась'
#     def car_turn(self,direction):
#         return f'{self.name} повернула {direction}'
#     def show_speed(self):
#         return f'Скорость {self.name} - {self.speed} км/ч'
# class TownCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
#     def show_speed(self):
#         print(f'Скорость {self.name} - {self.speed} км/ч')
#         if self.speed > 60:
#             return f'Допустимая скорость для {self.name} превышена'
# class SportCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
# class WorkCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
#     def show_speed(self):
#             print(f'Скорость {self.name} - {self.speed} км/ч')
#             if self.speed > 40:
#                 return f'Допустимая скорость для {self.name} превышена'
# class PoliceCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
# mazda = SportCar(90, 'красный', 'Mazda', False)
# honda = TownCar(70, 'черный', 'Honda', False)
# lada = WorkCar(30, 'белый', 'Lada', True)
# fiat = PoliceCar(80, 'голубой',  'Fiat', True)
# print(f'{mazda.car_stop}')
# print(f'{lada.car_go()} co скоростью {lada.show_speed()}')
# print(f'{lada.name} цвет {lada.color}')
# print(mazda.show_speed())
# print(honda.show_speed())
# print(fiat.show_speed())
# print(lada.show_speed())
#№5
# class Stationery:
#     title = None
#     def __init__(self,title):
#         self.title=title
#     def draw(self):
#         return f'Запуск отрисовки'
# class Pen(Stationery):
#     title = None
#     def __init__(self,title):
#         super().__init__(title)
#     def draw(self):
#         return f'Рисунок ручкой: {self.title}'
# class Pencil(Stationery):
#     title = None
#     def __init__(self,title):
#         super().__init__(title)
#     def draw(self):
#         return f'Рисунок карандашом: {self.title}'
# class Handle(Stationery):
#     title = None
#     def __init__(self,title):
#         super().__init__(title)
#     def draw(self):
#         return f'Рисунок маркером: {self.title}'
# pen = Pen('Дом')
# pencil = Pencil('Школа')
# handle = Handle('Семья')
# print(pen.draw())
print(pencil.draw())
print(handle.draw())