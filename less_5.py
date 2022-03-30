#№1
# with open ('my_file.txt','w') as obj:
#     while obj:
#         line = input('Enter:')
#         obj.writelines(f'{line}\n')
#         if line == '':
#             break
# with open ('my_file.txt','r',encoding='utf-8') as obj_2:
#     print(obj_2.readlines())
#№2
# my_list = ['Hello\n','Have a nice day\n','Good bye\n']
# with open ('m_file_2.txt','w') as obj_3:
#     obj_3.writelines(my_list)
# with open ('m_file_2.txt','r',encoding='utf-8') as obj_4:
#     ok=0
#     for line in obj_4:
#         ok += line.count('\n')
# print(f'Количество строк - {ok}')
# эта часть нормально работает, а следующая-нет
# with open('m_file_2.txt', 'r', encoding='utf-8') as obj_5:
#     for i in obj_5:
#         read = obj_5.readline()
#         print(len(read.split()))
#   не поняла, как количество слов посчитать, он считает только по одной строке, почему-то по второй и что он еще делает, я не пойму)
#№3
# from statistics import mean
# my_list_2 = ['Ivanov 35620.85\n','Petrov 37291.36\n','Sidorov 19241.87\n','Sobolev 15478.41\n','Kirova 33111.77\n','Grigorova 54515.99\n','Novikova 48246.77\n','Davydov 33456.75\n','Serov 17564.24\n','Antonova 41456.33\n','Leskova 11756.56\n']
# with open ('zp.txt','w') as obj_6:
#     obj_6.writelines(my_list_2)
# with open('zp.txt', 'r') as obj_6:
#     salaries = []
#     my_list_3 = obj_6.readlines()
#     print(f'Оклад меньше 20.000:')
#     for worker in my_list_3:
#       last_name , salary = worker.split()
#       salary = float(salary)
#       if salary < 20_000:
#         print(last_name)
#       salaries.append(salary)
# print(f'Cредний оклад: {mean(salaries):.2f}')
#№4
# my_voc = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
# new_voc = []
# with open ('numbers.txt','r') as obj_7:
#     for index in obj_7:
#         index = index.split(' ',1)
#         new_voc.append(my_voc[index[0]] +' '+index[1])
# print(new_voc)
# with open('numbers_2.txt', 'w', encoding='utf-8') as obj_8:
#     obj_8.writelines(new_voc)
#№5
# with open ('sum.txt','w') as obj_9:
#     line = input('Enter:')
#     obj_9.writelines(line)
# with open ('sum.txt','r') as obj_10:
#     numb = obj_10.read().split()
#     n = 0
#     for i in numb:
#         n += int(i)
# print(n)
#№6
# import re
# subject = {}
# with open ('school.txt','r',encoding='utf-8') as obj_11:
#     sch = obj_11.read().split('\n')
#     for i in sch:
#         res = re.sub('\(\w*\)','',i)
#         res_2 = re.sub('—','0',res)
#         res_3 = re.sub(':','',res_2)
#         subj , lect , pract , lab = res_3.split()
#         subject[subj] = int(lect) + int(pract) + int(lab)
# print(subject)
#№7
# import json
# profit_f = {}
# profit_sr = {}
# profit_new = 0
# prof_sr_new = 0
# m = 0
# with open ('firm.txt','r') as obj_12:
#     for line in obj_12:
#         name , firm , inc , izd = line.split()
#         profit_f[name] = int(inc) - int(izd)
#         if profit_f.setdefault(name) >= 0:
#             profit_new = profit_new + profit_f.setdefault(name)
#             m += 1
#     if m != 0:
#         prof_sr_new = profit_new / m
#         print(f'Cредняя прибыль: {prof_sr_new:.2f}')
#     profit_sr = {'average_profit': round(prof_sr_new)}
#     profit_f.update(profit_sr)
#     print(f'Прибыль компаний: {profit_f}')
# with open ('my_file.json','w') as write_json:
#     json.dump(profi.t_f,write_json)