#№1
a = [3,5,2.75,'hello']
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(type(a[3]))
#№2
# b = list(input('Введите список:'))
# print(b)
# b[0],b[1] = b[1],b[0]
# b[2],b[3] = b[3],b[2]
# print(b)
#№3
# month = input('Месяц:')
# seasons = {"12":"зима","1":"зима","2":"зима","3":"весна","4":"весна","5":"весна","6":"лето","7":"лето","8":"лето","9":"осень","11":"осень","12":"осень"}
# print(seasons.get(month))

# month_2 = int(input('Месяц:'))
# seasons_2 = ['0','зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
# print(seasons_2[month_2])
#№4
# i = 0
# j = -1
# my_str = str(input('Words:'))
# for words in my_str:
#     i +=1
#     j +=1
#     print(f'{i}.{my_str.split()[j][0:10]}')
""" не поняла, почему он выполняет, что нужно, но при этом ругается, что не так? """
#№5
# my_list = [9,7,5,3,1]
# my_list.append(int(input('Введите число:')))
# my_list.sort(reverse=True)
# print(my_list)
#№6
list = []
nazv = input('Введите название:')
cena = input('Введите цену:')
kolvo = input('Введите количество:')
my_voc = {"название":nazv,"цена":cena,"количество":kolvo}
my_kort = (1,my_voc)
list.append(my_kort)
print(list)