'''
Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не
предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из:
длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка
находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь:
UrbaN ~ URBAN.
Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна
вызываться в остальных двух функциях.

Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).
'''
def count_calls(): # подсчитывающая вызовы остальных функций.
    global calls
    calls += 1
    return calls

def string_info(string): # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    print(len(string), string.upper(), string.lower())
    return len(string), string.upper(), string.lower()

# def is_contains(string, list_to_search): # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
#     count_calls()
#     print(string.upper() in list_to_search)
#     return bool
def is_contains (string, list_to_search):
    count_calls()
    print(string.upper() in [s.upper() for s in list_to_search])
    return string.upper() in [s.upper() for s in list_to_search]

calls = 0
string1 = 'Питер'
string2 = 'Как'
string3 = 'Звезда'
list_to_search1 = ['ПиТер', 'вЧера', 'сИял', 'каК', 'зВезда', '!']

string_info(string1), is_contains(string1, list_to_search1), print(calls)
string_info(string2), is_contains(string2, list_to_search1), print(calls)
string_info(string3), is_contains(string3, list_to_search1), print(calls)



