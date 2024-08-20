"""
____________Генераторные сборки__________"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_len = [len(x) for x in first]
second_len = [len(y) for y in second]
# print(first_len) # [7, 7, 9]
# print(second_len) # [6, 5, 9]

###_________С функцией ЗИП_____________
zp = zip(first, second)
first_result = (abs(len(x[0])-len(x[1])) for x in
                zip(first, second) if len(x[0])!=len(x[1]))
### вычислили модуль разности 2-х длин попарно собранных
# слов из 2 списков через функцию зип

# print(zp)       # <zip object at 0x000001D030B68200>
print(list(zp)) # [('Strings', 'Строка'), ('Student',
# 'Урбан'), ('Computers', 'Компьютер')]
print(list(first_result)) # [1, 2]

###_________Без функции ЗИП_____________

second_result = (len(first[i])==len(second[i]) for i in range(0,3))
print(list(second_result)) # [False, False, True]