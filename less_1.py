# №1
# a = 10
# b = 13
# print(a+b)
# c = "Julia"
# print(f'hi, {c}')
# myname = input()
# print('User name:', myname)
# age = input()
# print('Age:', age)
#№2
# timeseconds = int(input('Seconds:'))
# minutes = timeseconds % 3600 // 60
# seconds = timeseconds % 3600 % 60
# print(f'{timeseconds//3600} : {minutes} : {seconds}')

# import time
# n=int(input('Seconds:'))
# time_format = time. strftime("%H:%M:%S", time. gmtime(n))
# print("Time in preferred format :-",time_format)
#№3
# N1 = int(input('Число:'))
# N2 = N1 + N1 + N1 * 10 + N1 + N1 * 10 + N1 * 100
# print(f'n+nn+nnn={N2}')
#№4
#не поняла, почему написано "используйте цикл while", самую большую цифру через if нашла
# G1 = int(input('Целое число:'))
# hun = G1 // 100
# dec = G1 % 100 // 10
# ed = G1 % 10
# if hun >= dec and hun >= ed:
#     print (f'Cамая большая цифра: {hun}')
# elif dec >= hun and dec >= ed:
#     print(f'Cамая большая цифра: {dec}')
# elif ed >= hun and ed >= dec:
#     print(f'Cамая большая цифра: {ed}')
#№5+№6
# TR = int(input('Выручка:'))
# TC = int(input('Издержки:'))
# Pr = TR - TC
# R  = Pr / TR
# if Pr > 0:
#     print(f'Ваша прибыль составляет: {Pr}')
#     print(f'Рентабельность прибыли составляет: {R:.2f}')
#     SS = int (input('Численность сотрудников:'))
#     PSS = Pr / SS
#     print(f'Прибыль на одного сотрудника: {PSS:.2f}')
# elif Pr < 0:
#     print(f'Ваш убыток составляет: {Pr}')
#№7
# akm = int(input('Сколько километров пробежал спортсмен в первый день?'))
# bkm = int(input('Какого результата он должен достичь?'))
# day = 1
# while akm < bkm:
#    akm *= 110 / 100
#    day += 1
# print(f'На {day} день спортсмен достиг результата {bkm} км, пробежав {akm:.2f} км.')
