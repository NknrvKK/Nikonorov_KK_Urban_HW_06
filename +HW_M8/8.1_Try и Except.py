'''
Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)
Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать
строковое представление этих двух данных вместе (в том же порядке). Во всех остальных
случаях выполнять стандартные действия.  '''
###___________V1__________
# def add_everything_up(a, b):
#     try:
#         return a + b
#     except:
#         return f'{a}{b}'

# print(add_everything_up(123.456, 'строка')) # 123.456строка
# print(add_everything_up('яблоко', 4215))    # яблоко4215
# print(add_everything_up(123.456, 7))        # 130.45600000000002


###___________V2__________
def add_everything_up(*args):
    sum = 0
    str = ''
    try:
        for i in args:
            sum += i
        print(sum)
    except:
        for i in args:
            str += f'{i}'
        print(str)

add_everything_up(123.456, 'строка', 123.456, 'строка', 123.456, 'строка', 123.456, 'строка')
### 123.456строка123.456строка123.456строка123.456строка
add_everything_up(123.45, 100, 123.45, 100, 123.4, 100, 123.45, 100) # 893.75




def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        for k in i:
            if isinstance(i, int or float):
                result += i
            else:
                incorrect_data += 1
                raise TypeError
    return result, incorrect_data

def calculate_average(numbers):
    sum = list(personal_sum(numbers))[0]
    try:
        list(personal_sum(numbers))[0] / (len(numbers) - list(personal_sum(numbers))[1])
    except ZeroDivisionError as exc:
        return 0



###_____Проверочный код:__________________________________________________________________________________

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать



