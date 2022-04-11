#№1
# class Data:
#     def __init__(self,day_month_year):
#         self.day = str(day_month_year)
#     @classmethod
#     def clsmeth(cls, day_month_year):
#         day = []
#         for i in day_month_year.split():
#             if i != '-': day.append(i)
#         return int(day[0]), int(day[1]), int(day[2])
#     @staticmethod
#     def proverka(day,month,year):
#         if 1<=day<=31 and 1<=month<= 12 and 2022 >= year >= 0:
#             return f'Дата верна'
#         else:
#             return f'Неправильная дата'
#     def __str__(self):
#         return f'Текущая дата {Data.clsmeth(self.day)}'
# day_1 = Data('15 - 7 - 2011')
# print(day_1)
# print(Data.clsmeth('11 - 11 - 2011'))
# print(Data.clsmeth('03 - 07 - 2021'))
# print(Data.proverka(32, 11, 2019))
# print(Data.proverka(11,7,2021))
#№2
# class Exc:
#     def __init__(self,delim,delit):
#         self.delim=delim
#         self.delit=delit
#     def dell(delim,delit):
#         try:
#             return delim/delit
#         except:
#             return 'Ошибка. Деление на ноль.'
# print(Exc.dell(5,0))
# print(Exc.dell(5,1))
#№3
# class Exc_1(Exception):
#     def __init__(self,*args):
#         self.list1=[]
#     def exc_1(self):
#         while True:
#             n = input('Введите число:')
#             try:
#                 n = int(n)
#                 self.list1.append(n)
#                 print(f'Мой список: {self.list1}')
#             except ValueError:
#                 print("Неверное значение")
#             finally:
#                 if n == 'stop':
#                     print(f'Список сформирован: {self.list1}')
#                     break
# try_except = Exc_1()
# print(try_except.exc_1())
#№4-5-6
# class SkladOrg:
#     def __init__(self,name,format,price,kolvo,strr,*args):
#         self.name=name
#         self.price=price
#         self.kolvo=kolvo
#         self.format=format
#         self.strr=strr
#         self.sklad=[]
#         self.sklad_ukompl=[]
#         self.my_ustr={'Устройство': self.name, 'формат': self.format,'цена': self.price, 'количество': self.kolvo}
#
#     def __str__(self):
#         return f'Устройство: {self.name}, формат: {self.format}, цена: {self.price}, количество: {self.kolvo},'
#
#     def priem(self):
#         try:
#             ustr_n = input(f'Название устройства: ')
#             ustr_pr = int(input(f'Цена устройства: '))
#             ustr_kol = int(input(f'Количество устройств: '))
#             ustr_for = input(f'Формат: ')
#             nov_ustr = {'Устройство': ustr_n, 'формат': ustr_for, 'цена': ustr_pr, 'количество': ustr_kol}
#             self.my_ustr.update(nov_ustr)
#             self.sklad.append(self.my_ustr)
#             print(f'Текущий список: \n {self.sklad}')
#         except:
#             return f'Неверные данные'
#         print(f'stop/Enter')
#         q = input(f'Добавить устройство: ')
#         if q == 'stop':
#             self.sklad_ukompl.append(self.sklad)
#             print(f'Устройства на складе: \n {self.sklad_ukompl}')
#             return f'Ввод окончен'
#         else:
#             return SkladOrg.priem(self)
# class Printer(SkladOrg):
#     def __init__(self,name,format,price,kolvo,strr):
#         super().__init__(name,format,price,kolvo,strr)
#     def print(self):
#         return f'Печать {self.strr} страниц'
# class Scaner(SkladOrg):
#     def __init__(self,name,format,price,kolvo,strr):
#         super().__init__(name,format,price,kolvo,strr)
#     def scan(self):
#         return f'Сканирование {self.strr} страниц'
# class Xerox(SkladOrg):
#     def __init__(self,name,format,price,kolvo,strr):
#         super().__init__(name,format,price,kolvo,strr)
#     def xerox(self):
#         return f'Копирование {self.strr} страниц'
# ustr_1 = Printer('hp','A4',2000, 5, 10)
# ustr_2 = Scaner('Canon','A4',1200, 5, 10)
# ustr_3 = Xerox('Xerox','A3',1500, 1, 15)
# print(ustr_1.print())
# print(ustr_2.scan())
# print(ustr_3.xerox())
# print(ustr_1.priem())
#№7
# class ComplexNum:
#     nums = 0
#     def __init__(self,re,im):
#         self.re=re
#         self.im=im
#         ComplexNum.nums += 1
#     def __str__(self):
#         return f"Комплексное число {self.re} + i*{self.im}"
#     def __add__(self,other):
#         return ComplexNum(self.re+other.re , self.im+other.im)
#     def __mul__(self, other):
#         return ComplexNum(self.re*other.re-self.im*other.im , self.re*other.im+self.im*other.re)
# a= ComplexNum(3,1)
# b = ComplexNum(4,2)
# print(a)
# print(a*b)
# print(a+b)