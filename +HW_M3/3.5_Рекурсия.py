# Цель: применить знания о рекурсии в решении задачи.
#
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает
# произведение цифр этого числа.
#
# Пункты задачи:
# Напишите функцию get_multiplied_digits и параметр number в ней.
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в
# неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите
# первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не
# получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

# V1    (Без рекурсии)
# def get_multiplied_digits(number: int):
#     proizv_cifr = 1
#     while number != 0:
#         ost = number % 10
#         proizv_cifr *= ost
#         number = (number - ost) / 10
#     return int(proizv_cifr)
#
# print(get_multiplied_digits(12345))


# V2     (С рекурсией - в return будет сама функция - вызовет до определенного момента)
# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) ->
# -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
def get_multiplied_digits(number: int):
    str_number = str(number) # преобразуем вводимое число в строку
    first = int(str_number[0]) # записываем первую цифру числа в числовом формате
    while len(str_number) > 1: # далее пока еще длина числа более 1
        # перемножаем первую цифру текущего числа на последующие
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
print(get_multiplied_digits(123456)) # 720

