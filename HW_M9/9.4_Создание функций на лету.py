"""
Создание функций на лету

"""
###_______Lambda-функция:___________________________
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# # l2 = list(map(lambda x: x, first))
# # print(l2) # ['М', 'а', 'м', 'а', ' ', 'м', 'ы',
# # # 'л', 'а', ' ', 'р', 'а', 'м', 'у']
#
# # list_1 = list(map(lambda x, y: x==y, first, second))
# # print(list_1)
# # [False, True, True, False, False, False, False, False, True,
# # False, False, False, False, False]
# ###______________________________________________
# ###_________Замыкание:___________________________
# """ !!!___Функции на лету___!!! - создание 1 функции
# прямо внутри другой. Замыкание в Пиитоне - функцио-
# нальный объект, кот-й запоминает значения во внешних
# областях, даже если они отсутствуют в памяти"""
#
# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         # *data_set - параметр принимающий неогранич
#         # количество данных любого типа
#         with open(file_name, "a", encoding='utf-8') as file:
#             for data in data_set:
#                 file.write(str(data) + '\n')
#
#     return write_everything
#
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже',
#                       'число', 5, 'в', 'списке'])
# txt_1 = open('example.txt', 'r', encoding='utf-8')
# str = txt_1.read()
# txt_1.close()
# print(str)

###______________________________________________
###_________Метод __call__:______________________

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = list(words) # выдает слова из списка
        # self.words = str(words)  # выдает буквы из слов из списка
        # self.words = tuple(words) # выдает слова из списка

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Ух ты', 'Баклажан')
print(first_ball())
print(first_ball())
print(first_ball())


# Примеры использования функции choice:

# line = 'abcdefg'
# # выбор случайного символа из строки `line`
# print(random.choice(line))
# # 'f'

#
# first_ball = ['Да', 'Нет', 'Наверное', 'Ух ты', 'Баклажан']
# print(choice(first_ball))
# Примеры использования функции choice:


