#№1
# from sys import argv
# script_name , vyr , stav , prem =argv
# zp = int(vyr)*int(stav)+int(prem)
# print(zp)
#№2
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# my_new_list = [el for elem, el in enumerate(my_list) if my_list[elem] > my_list[elem - 1]]
# print(my_new_list)
#№3
# list_1 = [el for el in range(20,240) if el % 20 ==0 or el % 21==0]
# print(list_1)
#№4
# list_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# list_2 = list(input('Введите список:'))
# new_list2 = [el for el in list_2 if list_2.count(el)==1]
# print(new_list2)
#№5
# from functools import reduce
# list_3 = list(range(100,1001))
# new_list3 = [el for el in list_3 if el % 2 == 0]
# def new_func(el1,el2):
#     return el1 * el2
# print(reduce(new_func,new_list3))
#№6.1
# import itertools
# for el in itertools.count (int(input('Начальное значение:'))):
#     print (el)
#     if el == 30:
#         break
#№6.2
# import itertools
# counter=1
# list_5 = [1,3,5,7,9]
# for el in itertools.cycle(list_5):
#     print (el)
#     counter += 1
#     if counter == 11:
#         break
#№7
# from math import factorial
# def generator (list_6):
#     for el in list_6:
#         yield factorial(el)
# n = int(input('Введите n:')) + 1
# list_6 = list(range(1,n))
# g = generator(list_6)
# print(g)
# for el in g:
#     print(el)