# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий
# класс. Применить метод __new__.

'''               Дополнительно о работе метода __new__:
Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
Разберёмся, как происходит передача данных между ними на следующем примере:
class Example:
  def __new__(cls, *args, **kwargs):
  print(args)
    print(kwargs)
    return object.__new__(cls)

  def __init__(self, first, second, third):
  print(first)
  print(second)
    print(third)

ex = Example('data', second=25, third=3.14)

Работа __new__:
'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться
 под индексом 0 как единственный элемент кортежа.
second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные
аргументы. Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14
соответственно в словаре.

                    Передача данных из __new__ в __init__:
После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
В параметр first распакуется из args единственный аргумент 'data'.
В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
'''

class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление обьектов
del h2
del h3
print(House.houses_history)