'''                      Задание "Раз, два, три, четыре, пять .... Это не всё?":

data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])  ]
                                              №0 - общий list
                    №0 - list     №1 - dict                                №2 - tuple
                №0, 1, 2 - int   №0, 1, 2 - int


Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

"А ЕСТЬ ЛИ УНИВЕРСАЛЬНОЕ РЕШЕНИЕ ДЛЯ ПОДСЧЁТА СУММЫ ВСЕХ ЧИСЕЛ И ДЛИН ВСЕХ СТРОК?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней
структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам -
универсального решения для таких структур он не нашёл.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

    Функция isinstance  (isinstance, classinfo)

    Функция isinstance('str', str) = True
    print(isinstance('str', str)) # True
    print(isinstance(2, str)) # False
    print(isinstance([1,2,3], list)) # True
'''

'''             Подсобка

# Для кортежа
def f1(t):
    sum = 0
    for i in t:
        if isinstance(i, tuple):
            sum += f1(i)
        elif isinstance(i, int):
            sum += i
    return sum
t = (1, 2, 3, 4, 5)
print(f1(t))

# Для словаря в списке
def f1(t):
    sum = 0
    for i in t:
        if isinstance(i, dict):
            for k in i.items(): # получаем список из данных dict_items([('qaw', 123), ('ret', 0)])
                sum += f1(k)
        elif isinstance(i, list):
            sum += f1(i)
        elif isinstance(i, set):
            sum += f1(i)
        elif isinstance(i, tuple):
            sum += f1(i)
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, int):
            sum += i
    return sum
d = [{'qaw': 123, 'ret': 0 }]
print(f1(d))


# print(calculate_structure_sum(d))
# print(d.items()) # dict_items([('qaw', 123), ('ret', 0)])
# print(d.values()) # dict_values([123, 0])
# print(d.keys()) # dict_keys(['qaw', 'ret'])
'''

def f1(args):
    sum = 0
    for i in args:
        if isinstance(i, list):
            sum += f1(i)
        elif isinstance(i, tuple):
            sum += f1(i)
        elif isinstance(i, set):
            sum += f1(i)
        elif isinstance(i, dict):       # либо если через i.items(), тогда :
            sum += f1(i.keys())         # for k in i.items():
            sum += f1(i.values())       #    sum += f1(k)
        elif isinstance(i, int):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
    return sum

data_structure = [ [1, 2, 3],  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}), "Hello", (  (),  [ { (2, 'Urban', ( 'Urban2', 35) ) } ] )  ]

print(f1(data_structure)) # 99

