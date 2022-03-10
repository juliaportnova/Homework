#№1
# arg_1 = int(input('Введите первый аргумент:'))
# arg_2 = int(input('Введите второй аргумент:'))
# def my_del (arg_1,arg_2):
#     return arg_1 / arg_2
# if arg_2 == 0:
#     print('На ноль делить нельзя!')
# elif arg_2 != 0:
#     print(divmod(arg_1,arg_2))
#№2
# my_info = lambda name,fam,year,city,email,tel:f'{name} {fam} {year} {city} {email} {tel}'
# print(input('Введите имя:'),input('Введите fam:'),input('Введите year:'),input('Введите city:'),input('Введите mail:'),input('Введите tel:'))

# def my_inf(**kwargs):
#     return kwargs.values()
# print(my_inf(name=input('Введите имя:'),fam=input('Введите фамилию:'),year=input('Введите год рождения:'),city=input('Введите город проживания:'),mail=input('Введите e-mail:'),tel=input('Введите телефон:')))
#№3
# def my_func (a_1,a_2,a_3):
#     if a_1 >= a_3 and a_2 >= a_3:
#         return a_1 + a_2
#     elif a_1 > a_2 and a_1 < a_3:
#         return a_1 + a_3
#     else:
#         return a_2 + a_3
# print(my_func(int(input('first:')),int(input('second:')),int(input('third:'))))
#№4
# def my_step(x,y):
#     return x ** y
# print(my_step(float(input('x:')),int(input('y:'))))
#№5
# def my_sum():
#     my_sum = 0
#     stop = False
#     while stop == False:
#         global arguments
#         arguments = input('Введите числа или "s" для зaвершения:').split()
#         for n in arguments:
#             sum = 0
#             if arguments[n] == 'S':
#                 stop = True
#                 break
#             else:
#                 sum += arguments[n]
#     my_sum += sum
#     return my_sum
# print(my_sum())
# """как только не пыталась написать, так и не разобралась, как правильно сделать"""
#№6
# def int_func(args):
#    return args.title()
# print(int_func("ok hi good"))
"""7ое задание не особо поняла, что имелось ввиду, слова выводит и так и с пробелами, и через запятую"""


