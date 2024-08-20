###______________________________________________
###_________Метод __call__:______________________
#
from random import choice

class MysticBall:
    def __init__(self, *words: str):
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


